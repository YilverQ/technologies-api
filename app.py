#Import Flask module.
from flask import Flask, render_template
from flask import render_template, redirect, url_for #request, make_response, flash


#Imports all Blueprints
from api.mark import markAPI
from api.category import categoryAPI
from api.product import productAPI


#Flask Aplitacion.
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


#Register Blueprint in Flask aplication.
app.register_blueprint(markAPI)
app.register_blueprint(categoryAPI)
app.register_blueprint(productAPI)



"""Rutas"""
#----------------------------------------------

""" Working """
#Home
@app.route("/")
def index():
	return redirect(url_for('product'))


@app.route("/product")
def product():
	data = {"title":"product"}
	return render_template("index.html", data = data)


@app.route("/mark")
def mark():
	data = {"title":"mark"}
	return render_template("index.html", data = data)


@app.route("/category")
def category():
	data = {"title":"category"}
	return render_template("index.html", data = data)


#Play the aplication in localhost.
if __name__ == "__main__":
	app.run(debug = True, host = "127.0.0.1", port = 5000)