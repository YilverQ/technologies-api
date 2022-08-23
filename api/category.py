"""Imports from Flask"""
from flask import Blueprint
from flask import jsonify, request

"""Imports from Model"""
from controller.category import Category

"""Imports from helpers"""
from helpers.categoryRequest import data_request

#Blueprint aplication User.
categoryAPI = Blueprint("categoryAPI", __name__, url_prefix = "/api")


#Global object.
category = Category()

"""Routes"""
#----------------------------------------------
#Create a new category.
@categoryAPI.route("/category", methods = ["POST"])
def create():
	new_category = data_request(request.json) #Request data.
	message = {"Message" : "Creating a new Category..."}
	message["New category:"] = category.create(new_category)
	return jsonify(message)


#Get all categories.
@categoryAPI.route("/category", methods = ["GET"])
def read():
	message = {"Message" : "Complete List of Categories"}
	message["Categories:"] = category.read()
	return jsonify(message)


#Get only category.
@categoryAPI.route("/category/<int:id_category>", methods = ["GET"])
def read_only(id_category):
	message = {"Message" : f"Details data from category_id {id_category}"}
	message["Category:"] = category.read_only(id_category)
	return jsonify(message)


#Update category.
@categoryAPI.route("/category/<int:id_category>", methods = ["PUT"])
def update(id_category):
	new_category = data_request(request.json) #Request data.
	message = {"Message" : f"Updating data from id_category {id_category}..."}
	message["New Data:"] = category.update(id_category, new_category)
	return jsonify(message)


#Delete category.
@categoryAPI.route("/category/<int:id_category>", methods = ["Delete"])
def delete(id_category):
	message = {"Message" : category.delete(id_category)}
	return jsonify(message)