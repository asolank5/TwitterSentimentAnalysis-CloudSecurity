from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt
import json
import pandas as pd

def percentage(part, whole):
	return(100 * (float(part)/float(whole)))

consumerKey = "consumer key"
consumerSecret = "consumer Secret"
accessToken = "access token"
accessTokenSecret = "access token secret"


auth = tweepy.OAuthHandler(consumer_key=consumerKey, consumer_secret=consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

searchTerm = input("Enter the keyword:")
noOfKeywordSearch = int(input("Enter how many tweets to analyze:"))

tweets = tweepy.Cursor(api.search, q=searchTerm, lang="en").items(noOfKeywordSearch)

positive=0
negative=0
neutral=0
polarity=0
strTweetKeyword="Below are the tweeter analysis on the following keyword", searchTerm


f = open("tweetAnalysis.txt", "a")
f.write("\n")
f.write(str(strTweetKeyword))

for tweet in tweets:	
	analysis = TextBlob(tweet.text)
	polarity = analysis.sentiment.polarity
	print(polarity)
	if (analysis.sentiment.polarity ==0):
		neutral +=1
	elif (analysis.sentiment.polarity < 0.00):
		negative += 1
	elif (analysis.sentiment.polarity > 0.00):
		positive +=1	
	f.write("\n") 
	f.write(str(analysis))		
		
positive = percentage(positive, noOfKeywordSearch)
negative = percentage(negative, noOfKeywordSearch)
neutral = percentage(neutral, noOfKeywordSearch)


print(positive)
print(negative)
print(neutral)

positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral = format(neutral, '.2f')

if (polarity == 0):
	print("Neutral")
elif (polarity < 0):
	print("Negative")
elif (polarity > 0):
	print("Positive")
	
