
import numpy as np
import sys

class Sudoku:
	def __init__(self):
		self.table = np.zeros((9,9), dtype='int32')
		self.library = {
			0 : "A",
			1 : "B",
			2 : "C",
			3 : "D",
			4 : "E",
			5 : "F",
			6 : "G",
			7 : "H",
			8 : "K"
		}

	def askforInput(self):
		print "I am going to ask you for the input like the format above! Enter 0 if it is empty"
		for y in range(9):
			for x in range(9):
				self.table[y,x] = raw_input("Enter value of %s-%s" % (self.library[y], x))


	def printSample(self):
		print "This is a format of the Sudoku Table"
		for row in range(15):
			if row is 0:
				for col in range(9):
					if col is 8:
						print '  %s' % (col + 1)
					else:
						sys.stdout.write('  %s' % (col + 1))
			elif row < 9:
				print self.library[row - 1]

	def printInputTable(self):
		print "This is what I see from what you entered ....!"
		empty = "----------+----------+-----------"
		emptyrow = 0
		for row in range(11):
			if row == 3 or row == 7:
				print empty
				emptyrow += 1
			else:
				n = row - emptyrow
				for num in range(9):
					if num == 2 or num == 5:
						sys.stdout.write('  %s |' % self.table[n,num])
					elif num == 8:
						print '  %s' % self.table[n,num]
					else:
						sys.stdout.write('  %s' % self.table[n,num])



