import requests as req
import json
from textblob import TextBlob as Blob
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_KEY = os.environ.get("NYT_API_KEY")
DATA_URL = 'https://api.nytimes.com/svc/archive/v1/%d/%d.json?api-key=%s'

def mainLogic():
	totalSentiment = 0
	for year in range(2016, 2017):
		for month in range(1, 13):
			data = getPage(DATA_URL % (year, month, API_KEY))
			for news in data['response']['docs']:
				leadPara = news['lead_paragraph']
				if leadPara != None:
					sentOfTitle = Blob(leadPara).sentiment
					totalSentiment += sentOfTitle.polarity
			print(totalSentiment)
			totalSentiment = 0

def getPage(url):
	res = req.get(url)
	if not res.ok:
		print('Could not download selected page!')
		return ''
	else:
		return json.loads(res.text)

if __name__ == '__main__':
	mainLogic()