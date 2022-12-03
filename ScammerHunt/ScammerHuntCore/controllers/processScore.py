
keywords = ['','']

def get_score(mentioned_users, keywords, tweet_ids, reply_count, retweets_count, like_count):
    score = 0

    if len(keywords) > 0:
        score +=5
    if len(mentioned_users) > 0:
        score += 2
    if len(tweet_ids) > 0:
        score += 1
    if retweets_count > 0:
        score += 1
    elif like_count > 0:
        score += 1
    return score

score = get_score(mentioned_users=[], keywords=keywords, tweet_ids=[], retweets_count=2, like_count=3)
print(score)

#python3 ScammerHunt/ScammerHuntCore/controllers/processScore.py