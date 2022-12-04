
from ScammerHuntCore.models import *
from ScammerHuntCore.controllers.processScore import get_score
from ScammerHuntCore.util.utilities import get_sentiment_score
from ScammerHuntCore.util.utilities import get_info_from

def contains_keyword(content):
    for keyword in Keywords.objects.all():
        keyword_name = keyword.name
        if keyword_name.lower() in content.lower():
            return True

    return False

def record_data(phone_number, mentioned_users_in_tweet, reference_link, content, reply_count=0, retweet_count=0, like_count=0):
    # Create new data
    data, data_created = ScrapeData.objects.get_or_create(text_data=content, reference_link=reference_link, reply_count=reply_count, retweet_count=retweet_count, like_count=like_count, source="TWITTER")
    
    # Sentiment
    data.sentiment_score = get_sentiment_score(content)

    # Scammer
    scammer, scammer_created = Scammer.objects.get_or_create(phone_number=phone_number)
    if scammer_created:
        timezone, carrier, geocoder = get_info_from("+91" + phone_number)
        scammer.timezone = timezone
        scammer.carrier = carrier
        scammer.geocoder = geocoder
        scammer.save()

    data.scammer.add(scammer)

    # Keywords
    keyword_list = []
    for keyword in Keywords.objects.all():
        keyword_name = keyword.name
        if keyword_name.lower() in content.lower():
            data.keywords.add(keyword)
            keyword_list.append(keyword_name)

    # Tweet ids
    tweet_ids = []
    tweets = ScrapeData.objects.filter(scammer__phone_number=phone_number)
    for tweet in tweets:
        if not data_created:
            tweet_ids.append(tweet.reference_link) 
    
    # Mentioned users
    mentioned_users = []
    for mentioned_user in mentioned_users_in_tweet:
        username = mentioned_user.username
        user = PriorityUser.objects.filter(username__icontains=username)
        if user:
            mentioned_users.append(username)
            data.mentioned_users.add(user)

    # Scores
    score = get_score(mentioned_users=mentioned_users, keywords=keyword_list, tweet_ids=tweet_ids, reply_count=reply_count, retweets_count=retweet_count, like_count=like_count)
    data.score = data.score if score < data.score else score

    # Save
    data.save()

