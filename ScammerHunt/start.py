from controllers.processData import contains_keyword, record_data
import snscrape.modules.twitter as sntwitter
import pandas as pd
from Util.utilities import *

def get_all_phone_numbers(tweet):
    mNumer = get_phone_number(tweet.content)
    
    for media in tweet.media:
        media_url = media.fullUrl
        #media_text = 
        #media_numbers


def is_scam_related_tweet(tweet):
    if len(get_all_phone_numbers(tweet)) > 0 :
        return True
    elif contains_keyword(tweet.content):
        return True
    else:
        return False
    

# TODO: include (place:b850c1bfd38f30e0)
# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('(phone OR number OR mobile OR no OR bank )(fraudster OR scammer OR cheat OR scam OR fraud OR loot ) (@CPMumbaiPolice  OR @cyberdost OR @noidapolice OR @uppolice OR @delhipolice OR @cybercrimeCID OR @mumbaipolice OR @dgpMaharashtra OR @mahaPolice OR @blrCityPolice OR @cybercellRaj OR @cybercellindia OR @DoT_India  OR @assampolice OR @wbpolice OR @kolkatapolice) (since:2022-11-05 until:2022-12-01)').get_items()):        
    if is_scam_related_tweet(tweet):
        phone_numbers = get_phone_number(tweet.content)
        for phone_number in phone_number:
            mentioned_users_in_tweet=tweet.mentionedUsers
            reference_link=tweet.url
            content=tweet.rawContent
            reply_count=tweet.replyCount
            retweet_count=tweet.retweetedTweet
            like_count=tweet.likeCount
            record_data(phone_number, mentioned_users_in_tweet, reference_link, content, reply_count, retweet_count, like_count)

