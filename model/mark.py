from model.connection import DAO


class MarkDB(DAO):
	"""CRUD-Mark"""
	###########################################
	#create.
	def create(self, data):
		"""
			data = {"name" : ""}
		"""
		insert = "Insert INTO Mark (name)"
		values = f"""VALUES ('{data["name"]}');"""
		sentence = insert + " " + values #Sentence SQL to execute.
		self.cursor.execute(sentence)
		self.connection.commit()
		return "Mark has registered successfully."


	#read.
	def read(self):
		self.cursor.execute("Select * FROM Mark;")
		return self.cursor.fetchall() #Get all row.


	#read_only.
	def read_only(self, name):
		sentence = f"""Select * FROM Mark WHERE name = '{name}';"""
		self.cursor.execute(sentence)
		return self.cursor.fetchone()


	#update.
	def update(self, id_mark, data):
		"""
			data = {"name" : ""}
		"""
		dataUpdate = f"""name = '{data["name"]}'"""
		sentence = f"""Update Mark SET {dataUpdate} WHERE id = {id_mark};"""
		self.cursor.execute(sentence) #Update all the row.
		self.connection.commit()
		return "Mark has updated successfully."


	#delete.
	def delete(self, id_mark):
		sentence = f"Delete FROM Mark WHERE id = {id_mark};"
		self.cursor.execute(sentence)
		self.connection.commit()
		return f"Mark {id_mark} has deleted successfully."