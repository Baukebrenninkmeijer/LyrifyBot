import sys, random, collections, os

# Since we split on whitespace, this can never be a word
NONWORD = "\n"

class Markov():

	def __init__(self, order=2):
		self.order = order
		self.table = collections.defaultdict(list)
		self.seen = collections.deque([NONWORD] * self.order, self.order)

	# Generate table
	def generate_table(self, filename):
		for line in open(filename): 
			for word in line.split():
				self.table[tuple(self.seen)].append(word)
				self.seen.append(word)
		self.table[tuple(self.seen)].append(NONWORD) # Mark the end of the file

	#table, seen = generate_table("gk_papers.txt")

	# Generate output
	def generate_output(self, max_words=100):
		self.seen.extend([NONWORD] * self.order) # clear it all
		for i in xrange(max_words):
			word = random.choice(self.table[tuple(self.seen)])
			if word == NONWORD:
				exit()
			print word,
			self.seen.append(word)


	def walk_directory(self, rootDir):
		for dirName, subdirList, fileList in os.walk(rootDir):
			print('Found directory: %s' % dirName)
			for fname in fileList:
				self.generate_table(os.path.join(dirName,fname))
				#print('\t%s' % fname)


m = Markov(order=3)

#m.walk_directory('./pres-speech')
m.walk_directory('./pres-speech/obama')
m.generate_output(max_words=100)