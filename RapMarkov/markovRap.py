import markovify as Markov

with open('corpusKDot.txt', 'r') as f:
	corp = f.read()

text_model = Markov.Text(corp)

for i in range(5):
	print(text_model.make_sentence(tries=10000).capitalize())