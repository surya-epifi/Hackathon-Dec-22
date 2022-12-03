
KEYWORDSTOCHECKFROM = ['scam','fraud', 'money', 'bank', 'criminal', 'debited', 'extorsion', 'balance']
USERSTAGGEDTOCHECKFROM = ['@police','@dgim', '@delhipolice', '@mhPolice', '@goaPolice', '@cybercrime', '@dgp']
# TODO: Create weight array for each of the keywords and use that to calculate the score

SCOREWEIGHTAGEFORKEYWORDS = 5
SCOREWEIGHTAGEFORUSERSTAGGED = 3
SCOREWEIGHTAGEFORREPEATEDTWEETIDS = 1
SCOREWEIGHTAGEFOROTHER = 1

def get_score(mentioned_users, keywords, tweet_ids, reply_count, retweets_count, like_count):
    score = 0

    if len(keywords) > 0:
        score += getOccuranceScoreFor(elementTypeArray=keywords, referenceArray=KEYWORDSTOCHECKFROM, scoreWeightage=SCOREWEIGHTAGEFORKEYWORDS)
    if len(mentioned_users) > 0:
        score += getOccuranceScoreFor(elementTypeArray=mentioned_users, referenceArray=USERSTAGGEDTOCHECKFROM, scoreWeightage=SCOREWEIGHTAGEFORUSERSTAGGED)
    if len(tweet_ids) > 0:
        score += getTweetIdScore(tweet_ids=tweet_ids)
    if retweets_count > 0 or like_count > 0:
        score += SCOREWEIGHTAGEFOROTHER
    return score

def getTweetIdScore(tweet_ids):
    if tweet_ids > 0:
        return SCOREWEIGHTAGEFORREPEATEDTWEETIDS

def getOccuranceScoreFor(elementTypeArray, referenceArray, scoreWeightage):

    listWithNoDuplicates = [*set(elementTypeArray)]
    commonKeywords = 0
    for word in listWithNoDuplicates:
        if word in referenceArray:
            commonKeywords += 1
    
    score = (commonKeywords/len(KEYWORDSTOCHECKFROM))*scoreWeightage
    return score

score = get_score(mentioned_users=['@police'], keywords=['scam','fraud', 'money', 'bank','scam','fraud', 'money', 'bank'], tweet_ids=[], retweets_count=2, like_count=2)
print(score)

#python3 ScammerHunt/ScammerHuntCore/controllers/processScore.py
