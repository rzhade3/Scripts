import base_converter
import dotenv
from random import randints
import requests


base_url = 'https://www.reddit.com/dev/api'


def main():
	dotenv.load()
	API_KEY = dotenv.get('REDDIT_API_KEY')


def sample_users():
	user_no = base_converter(randint(0, 36**6), 36)
	res = requests.get(base_url + )
	print(r.text)


if __name__ == '__main__':
	main()