from ScammerHuntCore.models import *
import csv



with open('scammers_list.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Phone number", "Number of complaints reported", "Reference url", "Keywords", "Mentions", "Score", "Carrier", "Geocoder", "Timezone" , "Average sentiment score", ])
    
    scammers = Scammer.objects.all()
    for scammer in scammers:
        reported_tweets = ScrapeData.objects.filter(scammer=scammer)

        phone_number = scammer.phone_number  
        num_complaints_reported = reported_tweets.count()
        
        reference_urls = []
        score = 0
        total_sentiment_score = 0

        keywords = []
        mentions = []
        for reported_tweet in reported_tweets:
            # Keyword
            keyword_query = reported_tweet.keywords.all()
            for keyword in keyword_query:
                keywords.append(keyword.name)
            # Mentions
            mentions_query = reported_tweet.mentioned_users.all()
            for mention in mentions_query:
                mentions.append(mention.username)

            reference_urls.append(reported_tweet.reference_link)
            score = reported_tweet.score if reported_tweet.score > score else score
            total_sentiment_score += reported_tweet.sentiment_score
        avg_sentiment_score = total_sentiment_score / num_complaints_reported

        # Write
        print('Added recored for ', phone_number)

        keywords = list(set(keywords))
        mentions = list(set(mentions))
        
        writer.writerow([phone_number, num_complaints_reported, reference_urls, keywords, mentions, score , scammer.carrier, scammer.geocoder, scammer.timezone, avg_sentiment_score])