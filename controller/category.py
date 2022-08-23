"""Imports from Model"""
from model.category import CategoryDB


class Category():
	def __init__(self):
		self.category = CategoryDB()


	#Create a new category.
	def create(self, data):
		category = self.category
		exist = category.read_by_name(data["name"])
		if exist: 
			return f"Sorry, category with the name '{data['name']}' already registered."
		else:
			return category.create(data)


	#Read all Categories.
	def read(self):
		category = self.category
		return category.read() 


	#Read only category.
	def read_only(self, id_category):
		category = self.category
		return category.read_only(id_category)


	#Read only category by name.
	def read_by_name(self, name):
		category = self.category
		return category.read_by_name(name)


	#Update category.
	def update(self, id_category, data):
		category = self.category
		exist = category.read_by_name(data["name"])
		if exist:
			if exist["id"] == id_category:
				return category.update(id_category, data)
			else:
				return f"Sorry, category with the name {data['name']} already registered."
		else:
			return category.update(id_category, data)


	#Delete category.
	def delete(self, id_category):
		category = self.category
		return category.delete(id_category)