from ScammerHuntCore.controllers.processData import contains_keyword, record_data
import snscrape.modules.twitter as sntwitter
from ScammerHuntCore.util.utilities import *

def get_all_phone_numbers(tweet):
    # Text phone numbers
    phone_numbers = get_phone_number(tweet.rawContent)

    if tweet.media:
        for media in tweet.media:
            media_url = media.fullUrl
            tweet_content = imageToText(media_url)
            image_phone_numbers = get_phone_number(tweet_content)
            if len(image_phone_numbers) > 0 :
                print('Found these numbers in tweet Image. ', image_phone_numbers)
                phone_numbers += image_phone_numbers
    
    return phone_numbers

def is_scam_related_tweet(tweet, phone_numbers):
    if len(phone_numbers) > 0 :
        return True
    elif contains_keyword(tweet.rawContent):
        return True
    else:
        return False
    

# TODO: include (place:b850c1bfd38f30e0)
# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('(phone OR number OR mobile OR no OR bank )(fraudster OR scammer OR cheat OR scam OR fraud OR loot ) (@CPMumbaiPolice  OR @cyberdost OR @noidapolice OR @uppolice OR @delhipolice OR @cybercrimeCID OR @mumbaipolice OR @dgpMaharashtra OR @mahaPolice OR @blrCityPolice OR @cybercellRaj OR @cybercellindia OR @DoT_India  OR @assampolice OR @wbpolice OR @kolkatapolice) (since:2022-11-05 until:2022-12-01)').get_items()):        

    phone_numbers = get_all_phone_numbers(tweet)
    if is_scam_related_tweet(tweet, phone_numbers):
        print('Processing tweet:', tweet.url)
        
        for phone_number in phone_numbers:
            mentioned_users_in_tweet=tweet.mentionedUsers
            reference_link=tweet.url
            content=tweet.rawContent
            reply_count=tweet.replyCount
            retweet_count=tweet.retweetedTweet
            like_count=tweet.likeCount
            record_data(str(phone_number), mentioned_users_in_tweet, reference_link, content, reply_count, 0, like_count)
            print("Record added for ", reference_link)

