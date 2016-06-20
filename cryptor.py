'''
Cryptor that will encrypt and decrypt messages
SQL link and everything else .. before storing into SQL tables
'''
from Crypto.Cipher import AES

class Cryptor:
	def __init__(self):
		self.obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
		messages = "Hung Q Nguyen"
		encrypted = self.obj.encrypt(messages)	
		print encrypted
		decrypted = self.obj.decypt(encrypted)
		print decrypted