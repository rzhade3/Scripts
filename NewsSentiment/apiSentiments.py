import requests as req
import json
from textblob import TextBlob as Blob

API_KEY = 'dba751dd13704051954b6791fc8b505f'
HEADLINES_URL = 'https://newsapi.org/v1/articles?source=%s&apiKey=%s'

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