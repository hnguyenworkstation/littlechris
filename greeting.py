'''
	His name is LittleChris
	He is born at 5:00 PM, June 18, 2016
	Copy right: Hung Q Nguyen - 2016
'''
from datetime import datetime

def greeting():
	print "> Now: " + getTime()
	print "> -- Hello!\n> -- How are you doing today?!\n> -- I hope you have a good day!"

def getTime():
	time = datetime.now()
	return time.strftime("%d/%m/%Y %H:%M:%S")
