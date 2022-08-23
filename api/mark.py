"""Imports from Flask"""
from flask import Blueprint
from flask import jsonify, request

"""Imports from Model"""
from controller.mark import Mark

"""Imports from helpers"""
from helpers.markRequest import data_request

#Blueprint aplication User.
markAPI = Blueprint("markAPI", __name__, url_prefix = "/api")


#Global object.
mark = Mark()

"""Routes"""
#----------------------------------------------
#Create a new mark.
@markAPI.route("/mark", methods = ["POST"])
def create():
	new_mark = data_request(request.json) #Request data.
	message = {"Message" : "Creating a new Mark..."}
	message["New mark:"] = mark.create(new_mark)
	return jsonify(message)


#Get all marks.
@markAPI.route("/mark", methods = ["GET"])
def read():
	message = {"Message" : "Complete List of Marks"}
	message["Marks:"] = mark.read()
	return jsonify(message)


#Get only mark.
@markAPI.route("/mark/<int:id_mark>", methods = ["GET"])
def read_only(id_mark):
	message = {"Message" : f"Details data from id_mark {id_mark}"}
	message["Mark:"] = mark.read_only(id_mark)
	return jsonify(message)


#Update mark.
@markAPI.route("/mark/<int:id_mark>", methods = ["PUT"])
def update(id_mark):
	new_mark = data_request(request.json) #Request data.
	message = {"Message" : f"Updating data from id_mark {id_mark}..."}
	message["New Data:"] = mark.update(id_mark, new_mark)
	return jsonify(message)


#Delete mark.
@markAPI.route("/mark/<int:id_mark>", methods = ["Delete"])
def delete(id_mark):
	message = {"Message" : mark.delete(id_mark)}
	return jsonify(message)