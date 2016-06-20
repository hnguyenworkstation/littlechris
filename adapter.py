'''
	Main way to get to littlechris's brain
'''

import mysql.connector
from datetime import datetime

class ServerAdapter:
	def __init__(self):
		self.config = {
		  'user': 'root',
		  'password': 'zonluzpocans',
		  'host': '104.131.29.183',
		  'database': 'littlebrain',
		  'raise_on_warnings': True,
		}

		try:
			self.conn = mysql.connector.connect(**self.config)
			self.cursor = self.conn.cursor()
			# print out message if we could connect to the server
			if self.conn.is_connected():
				print "My brain is working properly! I am ready!"
		except mysql.connector.Error as err:
			print "Cannot connect to the server"
			print "Something went wrong: {}".format(err)


	def reCommand(self, commandname, executed):
		now = datetime.now()
		# create query to insert data to commands
		query = "INSERT INTO commands "
                "(id, command, applied_date, executed)"
                "VALUES (%s, %s, %s, %s)"

        # create values to apply to the query
        values = ("NULL", commandname, now, executed )

        try:
        	self.cursor.execute(query, values)
        	self.conn.commit()
        	print "Successfully Recorded"
        except mysql.connector.Error as err:
			print "Something went wrong: {}".format(err)




