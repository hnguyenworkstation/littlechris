import greeting
import dlfromyoutube
import os

class Chris:
	def __init__(self):
		self.functionals = {
			"help" : self.printHelp,
			"greeting" : self.greet,
			"download" : self.download,
			"exit" : self.exit
		}

		self.details = {
			"greeting" : """
							> \t--- I am a friendly person
							> \t--- So, I will say hello to you 
						 """
		}

		self.greet()
		print '> Let me know if you need anything!'

		command = None
		while command is not '> exit':
			command = raw_input('> ')
			self.runCommand(command)

	def printHelp(self):
		for key in self.details.keys():
			print "> " + key

	def greet(self):
		greeting.greeting()

	def download(self):
		print "> Give me a link and you will be allset?"
		url = raw_input("> ")
		dlfromyoutube.printURLInfo(url)

	def runCommand(self, command):
		if command in self.functionals:
			self.functionals[command]()

	def exit(self):
		os.exit()




chris = Chris()

