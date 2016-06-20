import greeting
import dlfromyoutube
import adapter

from sys import platform as _pl

class Chris:
	def __init__(self):
		self.functionals = {
			"help" : self.printHelp,
			"greeting" : self.greet,
			"download" : self.download,
			"exit" : self.exit
		}

		self.details = {
			"greeting" : """\n\t--- I am a friendly person
\t--- So, I will say hello to you 
						 """,
			"download" : """\n\t--- I now can download a .mp3 file from youtube.com
\t--- Of course, I need to have a link from you!
						 """,
			"exit" : """\n\t--- If you want to me to go away :(
\t--- Enter this command :(
			"""
		}

		self.greet()
		print 'Let me know if you need anything!\n'

		command = None
		while command is not '> exit':
			command = raw_input('>> ')
			self.runCommand(command)

	def printHelp(self):
		print "\n## For now, what I could do are: "
		# print out list of commands and its details
		for key in self.details.keys():
			print key + self.details[key]
		print "## I am learning and improving myself! Support and Follow me!"

	def greet(self):
		greeting.greeting()

	def download(self):
		print "Give me a link and you will be allset?"
		url = raw_input(">> ")
		dlfromyoutube.printURLInfo(url)

	def runCommand(self, command):
		if command in self.functionals:
			self.functionals[command]()

	def exit(self):
		if _pl is "linux" or _pl is "linux2":
			os.exit()
		elif _pl is "darwin":
			os.exit()
		elif _pl is "win32":
			return

adapt = adapter.ServerAdapter()
adapt.reCommand("testing", "Y")
chris = Chris()

