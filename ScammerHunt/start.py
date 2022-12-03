import snscrape.modules.twitter as sntwitter
import pandas as pd
from Util.utilities import *


# TODO: include (place:b850c1bfd38f30e0)
# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('(phone OR number OR mobile OR no OR bank )(fraudster OR scammer OR cheat OR scam OR fraud OR loot ) (@CPMumbaiPolice  OR @cyberdost OR @noidapolice OR @uppolice OR @delhipolice OR @cybercrimeCID OR @mumbaipolice OR @dgpMaharashtra OR @mahaPolice OR @blrCityPolice OR @cybercellRaj OR @cybercellindia OR @DoT_India  OR @assampolice OR @wbpolice OR @kolkatapolice) (since:2022-11-05 until:2022-12-01)').get_items()):        
    if len(get_phone_number(tweet.content)) > 0:
        print(get_phone_number(tweet.content))
        print(tweet)
    