
from ScammerHuntCore.models import *
from controllers.processScore import get_score

def record_data(phone_number, keywords, identifier, content):
    pass

def update_score(phone_number):
    
    score = get_score(mentioned_users=[], keywords=keywords, tweet_ids=[], retweets_count=2, like_count=3)
    pass

