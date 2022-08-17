from model.connection import DAO


class ProductDB(DAO):
	"""CRUD-Product"""
	###########################################
	#create.
	def create(self, data):
		"""
			data = {"name" : "", "price" : "", "id_mark" = ""}
		"""
		insert = "Insert INTO Product (name, price, id_mark)"
		values = f"""VALUES ('{data["name"]}', '{data["price"]}', '{data["id_mark"]}');"""
		sentence = insert + " " + values #Sentence SQL to execute.
		self.cursor.execute(sentence)
		self.connection.commit()
		return "Product has registered successfully."


	#read.
	def read(self):
		self.cursor.execute("Select * FROM Product;")
		return self.cursor.fetchall() #Get all row.


	#read_only.
	def read_only(self, name):
		sentence = f"""Select * FROM Product WHERE name = '{name}';"""
		self.cursor.execute(sentence)
		return self.cursor.fetchone()


	#update.
	def update(self, id_product, data):
		"""
			data = {"name" : "", "price" : "", "id_mark" = ""}
		"""
		dataUpdate = f"""name = '{data["name"]}', price = '{data["price"]}', id_mark = '{data["id_mark"]}'"""
		sentence = f"""Update Product SET {dataUpdate} WHERE id = {id_product};"""
		self.cursor.execute(sentence) #Update all the row.
		self.connection.commit()
		return "Product has updated successfully."


	#delete.
	def delete(self, id_product):
		sentence = f"Delete FROM Product WHERE id = {id_product};"
		self.cursor.execute(sentence)
		self.connection.commit()
		return f"Product {id_product} has deleted successfully."