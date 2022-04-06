'''
Using JSON to represent a real dataset
'''


'''What a Single Tweet Looks like
{
   "tweet_id":570301130888122368,
   "airline_sentiment":"positive",
   "airline_sentiment_confidence":"0.3486",
   "negativereason_confidence":"0.0",
   "airline":"Virgin America",
   "name":"jnardino",
   "retweet_count":0,
   "text":"@VirginAmerica plus you've added commercials to the experience... tacky.",
   "tweet_created":"2015-02-24 11:15:59 -0800",
}
'''


#let's open the data
import json
fp = open('tweets.json','r')
data = json.load(fp)

print('How many tweets are there?', len(data))
print()



"""
count = {}

for tweet in data:
	sentiment = tweet['airline_sentiment']
	count[sentiment] = count.get(sentiment, 0) + 1

print(count)
"""





count = {}

for tweet in data:
	sentiment = tweet['airline_sentiment']
	created = int(tweet['tweet_created'].split(' ')[1].split(':')[0])

	count[(created,sentiment)] = count.get((created,sentiment), 0) + 1

#print it properly
for i in range(0,24):
	positive_perc = count[(i,'positive')]/(count[(i,'positive')] + count[(i,'neutral')] + count[(i,'negative')])
	print('Hour: ', i, 'Sentiment',positive_perc)


