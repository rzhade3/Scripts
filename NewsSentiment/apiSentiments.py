import requests as req
import json
from textblob import TextBlob as Blob

API_KEY = # Insert you own API Key for newsAPI here
HEADLINES_URL = 'https://newsapi.org/v1/articles?source=%s&apiKey=%s&sort=latest'

SOURCES_LIST = ['bloomberg', 'business-insider', 'cnbc', 'financial-times', 'fortune', 'the-economist', 'the-wall-street-journal']

def mainLogic():
	totalSentiment = 0
	for source in SOURCES_LIST:
		data = getPage(HEADLINES_URL % (source, API_KEY))
		for news in data['articles']:
			title = news['title']
			totalSentiment += Blob(title).sentiment.polarity
	print(totalSentiment)

def getPage(url):
	res = req.get(url)
	if not res.ok:
		print('Could not download selected page!')
		return ''
	else:
		return json.loads(res.text)

mainLogic()