
from ScammerHuntCore.models import *
from controllers.processScore import get_score

all_keywords = [ keyword.name for keyword in Keywords.objects.all()]

def record_data(phone_number, mentioned_users_in_tweet, reference_link, content, reply_count=0, retweet_count=0, like_count=0):
    # Create new data
    data, data_created = ScrapeData.objects.get_or_create(text_data=content, reference_link=reference_link,reference_link= reference_link, reply_count=reply_count, retweet_count=retweet_count, like_count=like_count, source="TWITTER")

    # Scammer
    scammer, scammer_created = Scammer.objects.get_or_create(phone_number=phone_number)
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
    tweets = ScrapeData.objects.filter(source__phone_number=phone_number)
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
    score = get_score(mentioned_users=mentioned_users, keywords=keyword_list, tweet_ids=tweet_ids, retweets_count=2, like_count=3)

    # Save
    data.save()

