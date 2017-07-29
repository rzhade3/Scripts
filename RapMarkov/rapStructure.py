class RapStructure(object):

	def __init__(self, text):
		self.text = text

	def minify(self):
		return self.text.replace('\n', ' ')