"""Imports from Model"""
from model.product import ProductDB


class Product():
	def __init__(self):
		self.product = ProductDB()


	#Create a new product.
	def create(self, data):
		product = self.product
		exist = product.read_by_name(data["name"])
		if exist: 
			return f"Sorry, product with the name {data['name']} already registered."
		else:
			return product.create(data)


	#Read all products.
	def read(self):
		product = self.product
		return product.read() 


	#Read only product.
	def read_only(self, id_product):
		product = self.product
		return product.read_only(id_product)


	#Read only product by name.
	def read_by_name(self, name):
		product = self.product
		return product.read_by_name(name)


	#Update product.
	def update(self, id_product, data):
		product = self.product
		exist = product.read_by_name(data["name"])
		if exist:
			if exist["id"] == id_product:
				return product.update(id_product, data)
			else:
				return f"Sorry, product with the name {data['name']} already registered."
		else:
			return product.update(id_product, data)


	#Delete product.
	def delete(self, id_product):
		product = self.product
		return product.delete(id_product)