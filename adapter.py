
import mysql.connector

class ServerAdapter:
	def __init__(self):
		self.config = {
		  'user': 'root@104.131.29.183',
		  'password': 'zonluzpocans',
		  'host': 'localhost',
		  'database': 'littlebrain',
		  'raise_on_warnings': True,
		}

		try:
			self.cnx = mysql.connector.connect(**config)
			print "Connected to server successfully!"
		except Exception as e:
			print "Cannot connect to the server"
