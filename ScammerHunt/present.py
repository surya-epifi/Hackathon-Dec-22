from ScammerHuntCore.models import *
import csv



with open('scammers_list.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Phone number", "Number of complaints reported", "Reference url", "Score", "Average sentiment score"])
    
    scammers = Scammer.objects.all()
    for scammer in scammers:
        reported_tweets = ScrapeData.objects.filter(scammer=scammer)

        phone_number = scammer.phone_number  
        num_complaints_reported = reported_tweets.count()
        
        reference_urls = []
        score = 0
        total_sentiment_score = 0
        for reported_tweet in reported_tweets:
            reference_urls.append(reported_tweet.reference_link)
            score = reported_tweet.score if reported_tweet.score > score else score
            total_sentiment_score += reported_tweet.sentiment_score
        avg_sentiment_score = total_sentiment_score / num_complaints_reported

        # Write
        print('Added recored for ', phone_number)
        writer.writerow([1, phone_number, num_complaints_reported, reference_urls, score, avg_sentiment_score])