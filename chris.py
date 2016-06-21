import greeting
import dlfromyoutube
import adapter
import sudoku

from sys import platform as _pl

# Making Objects
adapt = adapter.ServerAdapter()
sudoku = sudoku.Sudoku()

class Chris:
	def __init__(self):
		self.options = {
			"help" : self.printHelp,
			"do" : self.printDoOptions,
		}

		self.methodList = {
			"help" : [],
			"do" : ["greeting", "download", "exit"]
		}

		self.doFunctionals = {
			"greeting" : self.greet,
			"download" : self.download,
			"exit" : self.exit
		}

		self.doDetails = {
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
			commandList = command.split(' ')
			if commandList[0] != "chris":
				print "Enter command with the following format: chris [options] [methods]"
			elif len(commandList) == 2:
				self.printOptions(commandList[1])
			else:
				self.runCommand(command[1], commandList[2])

	def printHelp(self):
		print "\n## For now, what I could do are: "
		# print out list of commands and its details
		for key in self.doDetails.keys():
			print key + self.doDetails[key]
		print "## I am learning and improving myself! Support and Follow me!"

	# print the options
	def printOptions(self, option):
		if option in self.options.keys():
			self.options[option]()
		else:
			print "Sorry! I am not able to do that, YET!"

	def printDoOptions(self):
		print "\n## Which that option, what I could do are: "
		# print out list of commands and its details
		for key in self.doDetails.keys():
			print key + self.doDetails[key]
		print "## I am learning and improving myself! Support and Follow me!"

	def greet(self):
		greeting.greeting()

	def download(self):
		print "Give me a link and you will be allset?"
		url = raw_input(">> ")
		dlfromyoutube.printURLInfo(url)

	def runCommand(self, option, command):
		if option in self.methodList.keys():
			if command in self.methodList[option]:
				self.doFunctionals[command]()
				# Record command entered to little chris
				adapt.reCommand(command, 'T')
			else:
				print "That method doesn't belong to this option!\n\t--- Try \"chris help\" to learn more about me"
				adapt.reCommand(command, 'F')
		else:
			print "I am not able to do that, for now!\n\t--- Try \"chris help\" to learn more about me"
			adapt.reCommand(command, 'F')

	def exit(self):
		if _pl is "linux" or _pl is "linux2":
			os.exit()
		elif _pl is "darwin":
			os.exit()
		elif _pl is "win32":
			return

chris = Chris()

