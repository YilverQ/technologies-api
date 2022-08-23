"""Imports from Flask"""
from flask import Blueprint
from flask import jsonify, request

"""Imports from Model"""
from controller.product import Product

"""Imports from helpers"""
from helpers.productRequest import data_request

#Blueprint aplication User.
productAPI = Blueprint("productAPI", __name__, url_prefix = "/api")


#Global object.
product = Product()

"""Routes"""
#----------------------------------------------
#Create a new product.
@productAPI.route("/product", methods = ["POST"])
def create():
	new_product = data_request(request.json) #Request data.
	message = {"Message" : "Creating a new Mark..."}
	message["New product:"] = product.create(new_product)
	return jsonify(message)


#Get all marks.
@productAPI.route("/product", methods = ["GET"])
def read():
	message = {"Message" : "Complete List of Marks"}
	message["Products:"] = product.read()
	return jsonify(message)


#Get only product.
@productAPI.route("/product/<int:id_product>", methods = ["GET"])
def read_only(id_product):
	message = {"Message" : f"Details data from id_product {id_product}"}
	message["Product:"] = product.read_only(id_product)
	return jsonify(message)


#Update product.
@productAPI.route("/product/<int:id_product>", methods = ["PUT"])
def update(id_product):
	new_product = data_request(request.json) #Request data.
	message = {"Message" : f"Updating data from id_product {id_product}..."}
	message["New Data:"] = product.update(id_product, new_product)
	return jsonify(message)


#Delete product.
@productAPI.route("/product/<int:id_product>", methods = ["Delete"])
def delete(id_product):
	message = {"Message" : product.delete(id_product)}
	return jsonify(message)