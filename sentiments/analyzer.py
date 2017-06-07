import nltk

class Analyzer():
	"""Implements sentiment analysis."""
	def __init__(self, positives, negatives):
		"""Initialize Analyzer."""
		self.pos = self.read_file(positives)
		self.neg = self.read_file(negatives)

	def read_file(self, file_name):
		
		fileop = open(file_name, 'r')
		# Skip comments
		delim = ';'
		
		line = fileop.readline()
		
		while delim in line:
			line = fileop.readline()

		# read file and save the words in list
		line_list = self.strip_newline(fileop.readlines())
		
		fileop.close()

		return line_list

	def strip_newline(self, word_list):

		stripped_list = []
		for item in word_list:
			stripped_list.append(item.rstrip('\n'))

		return stripped_list

	def analyze(self, text):
		"""Analyze text for sentiment, returning its score."""
		tokenizer = nltk.tokenize.TweetTokenizer()
		tokens = tokenizer.tokenize(text)
	 	
		score = []
		for item in tokens:
			item_l = item.lower()
			
			if item_l in list(self.neg):
				score.append(-1)     
			elif item_l in list(self.pos):
				score.append(1)
			else:
				score.append(0)
		
		return sum(score)
