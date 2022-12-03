import snscrape.modules.twitter as sntwitter
import pandas as pd

# Created a list to append all tweet attributes(data)
attributes_container = []

# Creating list to append tweet data to
attributes_container = []
# TODO: include (place:b850c1bfd38f30e0)
# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('(phone OR number OR mobile OR no OR bank )(fraudster OR scammer OR cheat OR scam OR fraud OR loot ) (@CPMumbaiPolice  OR @cyberdost OR @noidapolice OR @uppolice OR @delhipolice OR @cybercrimeCID OR @mumbaipolice OR @dgpMaharashtra OR @mahaPolice OR @blrCityPolice OR @cybercellRaj OR @cybercellindia OR @DoT_India  OR @assampolice OR @wbpolice OR @kolkatapolice) (since:2022-11-05 until:2022-12-01) (place:b850c1bfd38f30e0)').get_items()):    
    print(tweet)    
    attributes_container.append([tweet.user.username, tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])
    
# Creating a dataframe to load the list
tweets_df = pd.DataFrame(attributes_container, columns=["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"])