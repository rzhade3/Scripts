from rapStructure import RapStructure

with open('Songs/DNA.txt', 'r') as f:
	text = f.read()

q = RapStructure(text)
print(q.minify())

# q = rapStructure(text)
# print(q.minify())