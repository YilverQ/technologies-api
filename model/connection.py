"""Imports to mysql"""
import mysql.connector
from mysql.connector import Error

"""Imports Environment"""
import os
from dotenv import load_dotenv
load_dotenv()

"""DAO = Data Access Object"""
class DAO:
	"""Connection with the database"""
	def __init__(self):
		try: #Try a connection.
			self.connection = mysql.connector.connect(
							host = os.getenv("HOST_DB"),
							port = os.getenv("PORT_DB"),
							user = os.getenv("USER_DB"),
							password = os.getenv("PASSWORD_DB"),
							db = os.getenv("NAME_DB")) #Data for to connection.
			self.cursor = self.connection.cursor(dictionary=True) #cursor is essential to execute SQL statements
		except Error as ex: #In case of connection failure
			print("Sorry, an error has occurred")
			print(f"Error: {ex}")