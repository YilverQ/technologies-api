import mysql.connector
from mysql.connector import Error


"""DAO = Data Access Object"""
class DAO:
	"""Connection with the database"""
	def __init__(self):
		try: #Try a connection.
			self.connection = mysql.connector.connect(
							host = "localhost",
							port = 3306,
							user = "root",
							password = "root",
							db = "contact") #Data for to connection.
			return self.connection
		except Error as ex: #In case of connection failure
			print("Sorry, an error has occurred")
			print(f"Error: {ex}")
			return ex