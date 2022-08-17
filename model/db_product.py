from model.connection import DAO


class UserDB(DAO):
	"""CRUD-User"""
	###########################################
	#Get all user from database.
	def read_users(self):
		self.cursor.execute("Select * from User;")
		return self.cursor.fetchall() #Obtiene todos las filas de la tabla. 


	#Create a new user with past data.
	def create_user(self, data):
		"""
			data = {
				"name" : "", "last_name" : "",
				"email": "", "password" : ""}
		"""
		insert	 = """Insert INTO User (name, last_name, email, password)"""
		values	 = f"""VALUES ('{data["name"]}', '{data["last_name"]}', '{data["email"]}', '{data["password"]}');"""
		sentence = insert + " " + values #'Sentence SQL to execute.
		self.cursor.execute(sentence)
		self.conexion.commit()
		return "User has registered successfully."


	#Update data to user with "idUser".
	def update_user(self, idUser, data):
		"""
			data = {
				"name" : "", "last_name" : "",
				"email": "", "password" : ""}
		"""
		dataUpdate = f"""name = '{data["name"]}', last_name = '{data["last_name"]}', email = '{data["email"]}', password = '{data["password"]}'"""
		sentence 	= f"Update User set {dataUpdate} WHERE id = {idUser}"; 
		self.cursor.execute(sentence) #Update all the row.
		self.conexion.commit()
		return "User has updated successfully."


	#Delete one row from table User.
	def delete_user(self, idUser):
		sentence = f"""Delete FROM User WHERE id = {idUser};"""
		self.cursor.execute(sentence) #Delete row.
		self.conexion.commit()
		return f"User {idUser} has deleted successfully."


	#Get a only user with email equal "email".
	def read_mail_user(self, email):
		sentence = f"Select * FROM User WHERE email = '{email}';"
		self.cursor.execute(sentence)
		return self.cursor.fetchone() #return user.


	#Get a only user by idUser.
	def read_id_user(self, idUser):
		sentence = f"Select * FROM User WHERE id = '{idUser}';"
		self.cursor.execute(sentence)
		return self.cursor.fetchone() #return user.