import requests as req
import json
import time
from textblob import TextBlob as Blob
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_KEY = os.environ.get("HEADLINES_API_KEY")
HEADLINES_URL = 'https://newsapi.org/v1/articles?source=%s&apiKey=%s&sort=latest'

SOURCES_LIST = ['bloomberg', 'business-insider', 'cnbc', 'financial-times', 'fortune', 'the-economist', 'the-wall-street-journal']
data_file = 'data/data.json'

def mainLogic():
	totalSentiment = 0
	mostPositive = [0, '']
	mostNegative = [0, '']
	for source in SOURCES_LIST:
		data = getPage(HEADLINES_URL % (source, API_KEY))
		for news in data['articles']:
			title = news['title']
			sentOfTitle = Blob(title).sentiment
			totalSentiment += sentOfTitle.polarity

			if sentOfTitle.polarity > mostPositive[0]:
				mostPositive = [sentOfTitle.polarity, title]
			elif sentOfTitle.polarity < mostNegative[0]:
				mostNegative = [sentOfTitle.polarity, title]
	print(totalSentiment)
	print(mostPositive)
	print(mostNegative)
	with open(data_file, 'r') as f:
	    json_data = json.load(f)
	json_data[time.strftime("%d/%m/%Y %H:%M")] = totalSentiment
	with open(data_file, 'w') as f:
	    f.write(json.dumps(json_data))

def getPage(url):
	res = req.get(url)
	if not res.ok:
		print('Could not download selected page!')
		return ''
	else:
		return json.loads(res.text)

if __name__ == '__main__':
	mainLogic()