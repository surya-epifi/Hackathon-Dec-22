from ScammerHuntCore.models import *

KEYWORDSTOCHECKFROM = ['scam','fraud', 'money', 'bank', 'criminal', 'debited', 'extorsion', 'balance']
USERSTAGGEDTOCHECKFROM = ['police','dgim', 'delhipolice', 'mhPolice', 'goaPolice', 'cybercrime', 'dgp']
SENTENCESTOCHECKFROM = ['My account balance has been deducted ','Fraud calling number', 'Fraud whatsapp chat number', 'Cyber fraud group', 'Number of the scammer', 'Number of the scammer', 'Cyber crime', 'New fraud started', 'Online fraud', 'Against fraud of', 'ATM fraud', 'Claiming to be from the bank', 'Loot my money', 'Transfer money', 'Bank fraud', 'Cyber fraud', 'Action against this number', 'Fraud call from', 'Asked to transfer money', 'Asked me UPI pin', 'Victim of an online scam']




# TODO: Create weight array for each of the keywords and use that to calculate the score

SCOREWEIGHTAGEFORKEYWORDS = 5
SCOREWEIGHTAGEFORSENTENCES = 5
SCOREWEIGHTAGEFORUSERSTAGGED = 2
SCOREWEIGHTAGEFORREPEATEDTWEETIDS = 1
SCOREWEIGHTAGEFOROTHER = 1

ElEMENTWEIGHTAGEFORKEYWORDS = 0.9
ElEMENTWEIGHTAGEFORSENTENCES = 0.7
ElEMENTWEIGHTAGEFORUSERSTAGGED = 1.1

def mapName(n):
    return n.name.lower()

KEYWORDSTOCHECKFROM =  [keyword.name for keyword in Keywords.objects.all()]
USERSTAGGEDTOCHECKFROM =  [user.username for user in PriorityUser.objects.all()]
# print(KEYWORDSTOCHECKFROM)
# print(USERSTAGGEDTOCHECKFROM)

def get_score(mentioned_users, keywords, tweet_ids, reply_count, retweets_count, like_count):
    score = 0

    if len(keywords) > 0:
        score += getOccuranceScoreFor(elementTypeArray=keywords, referenceArray=KEYWORDSTOCHECKFROM, elementWeightage=ElEMENTWEIGHTAGEFORKEYWORDS, scoreWeightage = SCOREWEIGHTAGEFORKEYWORDS)
        print('Score for keywords')
        print(score)
        score += getOccuranceScoreFor(elementTypeArray=keywords, referenceArray=SENTENCESTOCHECKFROM, elementWeightage=ElEMENTWEIGHTAGEFORSENTENCES, scoreWeightage = SCOREWEIGHTAGEFORSENTENCES)
        print('Score for sentences')
        print(score)
        if score > SCOREWEIGHTAGEFORKEYWORDS:
            score = 5
    if len(mentioned_users) > 0:
        usersExistingScore = getOccuranceScoreFor(elementTypeArray=mentioned_users, referenceArray=USERSTAGGEDTOCHECKFROM, elementWeightage=ElEMENTWEIGHTAGEFORUSERSTAGGED, scoreWeightage=SCOREWEIGHTAGEFORUSERSTAGGED)
        if usersExistingScore > SCOREWEIGHTAGEFORUSERSTAGGED:
            usersExistingScore = SCOREWEIGHTAGEFORUSERSTAGGED
        score = score + usersExistingScore
    if len(tweet_ids) > 0:
        score += getTweetIdScore(tweet_ids=tweet_ids)
    if retweets_count > 0 or like_count > 0:
        score += SCOREWEIGHTAGEFOROTHER
    return score

def getTweetIdScore(tweet_ids):
    if len(tweet_ids) > 0:
        return SCOREWEIGHTAGEFORREPEATEDTWEETIDS

def getOccuranceScoreFor(elementTypeArray, referenceArray, elementWeightage, scoreWeightage):
    listWithNoDuplicates = [*set(elementTypeArray)]
    commonKeywordsCount = 0
    for word in listWithNoDuplicates:
        if word in referenceArray:
            commonKeywordsCount += 1
    
    #score = (commonKeywords/len(KEYWORDSTOCHECKFROM))*scoreWeightage
    score = (commonKeywordsCount*elementWeightage)
    return score

score = get_score(mentioned_users=['police'], keywords=['scam','fraud', 'money', 'bank','scam','fraud', 'money', 'bank'], tweet_ids=['23432432','3443243'],reply_count=4, retweets_count=2, like_count=2)
print(score)

#python3 ScammerHunt/ScammerHuntCore/controllers/processScore.py
