from model.connection import DAO


class CategoryDB(DAO):
	"""CRUD-Category"""
	###########################################
	#create.
	def create(self, data):
		"""
			data = {"name" : ""}
		"""
		insert = "Insert INTO Category (name)"
		values = f"""VALUES ('{data["name"]}');"""
		sentence = insert + " " + values #Sentence SQL to execute.
		self.cursor.execute(sentence)
		self.connection.commit()
		return "Category has registered successfully."


	#read.
	def read(self):
		self.cursor.execute("Select * FROM Category;")
		return self.cursor.fetchall() #Get all row.


	#read_only.
	def read_only(self, id_category):
		sentence = f"""Select * FROM Category WHERE id = '{id_category}';"""
		self.cursor.execute(sentence)
		return self.cursor.fetchone()


	#read_by_name.
	def read_by_name(self, name):
		sentence = f"""Select * FROM Category WHERE name = '{name}';"""
		self.cursor.execute(sentence)
		return self.cursor.fetchone()


	#update.
	def update(self, id_category, data):
		"""
			data = {"name" : ""}
		"""
		dataUpdate = f"""name = '{data["name"]}'"""
		sentence = f"""Update Category SET {dataUpdate} WHERE id = {id_category};"""
		self.cursor.execute(sentence) #Update all the row.
		self.connection.commit()
		return "Category has updated successfully."


	#delete.
	def delete(self, id_category):
		sentence = f"Delete FROM Category WHERE id = {id_category};"
		self.cursor.execute(sentence)
		self.connection.commit()
		return f"Category {id_category} has deleted successfully."