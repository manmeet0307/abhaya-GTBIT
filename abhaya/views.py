from django.shortcuts import render

from django.shortcuts import render 
from django.http import HttpResponse
import json
import re 
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob 

class TwitterClient(object): 

	def __init__(self): 
		consumer_key = 'jC1OiEEo8fneSzhNyYmur6arl'
		consumer_secret = 'Aj9CULS7snOMMH9iUQfBv0F2lVltS96hAz9zJuCs1FuJLydHyR'
		access_token = '142971949-PUl04zwkrV36gRbJJFa43bRGBEryE1DQnQxPDIm9'
		access_token_secret = '7kYininJCf9yRDBXyqv6avytU7GP3icXqjL7bkdnjtFI0'
		negative="0"
		positive="0"
		neutral="0"
		negative_tweet="negative"
		positive_tweet="positans"
		try: 
			self.auth = OAuthHandler(consumer_key, consumer_secret) 
			self.auth.set_access_token(access_token, access_token_secret) 
			self.api = tweepy.API(self.auth) 
		except: 
 		   print("Error: Authentication Failed") 

	def clean_tweet(self, tweet): 
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()) 

	def get_tweet_sentiment(self, tweet): 
		analysis = TextBlob(self.clean_tweet(tweet)) 
		if analysis.sentiment.polarity > 0: 
			return 'positive'
		elif analysis.sentiment.polarity == 0: 
			return 'neutral'
		else: 
			return 'negative'

	def get_tweets(self, query, count = 10): 
		tweets = [] 

		try: 
			fetched_tweets = self.api.search(q = query, count = count) 

			for tweet in fetched_tweets: 
				parsed_tweet = {} 

				# saving text of tweet 
				parsed_tweet['text'] = tweet.text 
				# saving sentiment of tweet 
				parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text) 

				# appending parsed tweet to tweets list 
				if tweet.retweet_count > 0: 
					# if tweet has retweets, ensure that it is appended only once 
					if parsed_tweet not in tweets: 
						tweets.append(parsed_tweet) 
				else: 
				    tweets.append(parsed_tweet) 

			# return parsed tweets 
			return tweets 

		except tweepy.TweepError as e: 
	# print error (if any) 
			print("Error : " + str(e)) 

	def tweet(params): 
		# creating object of TwitterClient Class 
		api = TwitterClient() 
		# calling function to get tweets 
		tweets = api.get_tweets(query = params, count = 200) 

		# picking positive tweets from tweets 
		ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
		# percentage of positive tweets 
		positive=format(100*len(ptweets)/(len(tweets)+1)) 
		# picking negative tweets from tweets 
		ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
		# percentage of negative tweets 
		negative=format(100*len(ntweets)/(len(tweets)+1))
		# percentage of neutral tweets 
		neutral=format(100*(len(tweets)-len(ntweets)-len(ptweets))/(len(tweets)+1))
		# printing first 5 positive tweets 
		positive_tweet="Positive tweets:" 
		for tweet in ptweets[:10]: 
			positive_tweet=positive_tweet+tweet['text'] 

		negative_tweet="Negative tweets:" 
		for tweet in ntweets[:10]: 
			negative_tweet=negative_tweet+tweet['text']

		#print (positive_tweet, negative_tweet, neutral)

		return {'positive':positive, 'negative':negative,'neutral':neutral}

def home(request):
	return render(request,'abhaya/index.html')

def ToBeMom(request):
	return render(request,"abhaya/ToBeMom.html")

def GovtSchemes(request):
	return render(request,"abhaya/GovtSchemes.html")

def Diet(request):
	return render(request,"abhaya/diet.html")

def Excercise(request):
	return HttpResponse("Excercise")

def NearByHospitals(request):
	return render(request,"abhaya/map.html")

def videos(request):
	return render(request,"abhaya/videos.html")


def voice(request):
	return render(request,"abhaya/voice.html")
def analyse(request):
	ans=""
	typ="AVG"
	params={
				'positive':0,
				'negative':0,
				'neutral':0,
				'prod_typ':"AVG"
			}
	if(request.GET):
		if request.method == "GET":
			print(request.GET.get('name'))
			para=request.GET.get('name',None)
			ans=TwitterClient.tweet(para)
			print(ans)

			if(int(float(ans['positive']))>=50):
				typ="GOOD"
	
			params={
				'positive':ans['positive'],
				'negative':ans['negative'],
				'neutral':ans['neutral'],
				'prod_typ':typ,
			}

	return render(request,"abhaya/analyse.html",params)
