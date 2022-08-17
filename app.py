#Import Flask module.
from flask import Flask


#Imports all Blueprints
from api.mark import markAPI
from api.product import productAPI


#Flask Aplitacion.
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


#Register Blueprint in Flask aplication.
app.register_blueprint(markAPI)
app.register_blueprint(productAPI)



"""Rutas"""
#----------------------------------------------

""" Working """
#Home
@app.route("/")
def index():
	return "Hola, desde Flask!"


#Play the aplication in localhost.
if __name__ == "__main__":
	app.run(debug = True, host = "127.0.0.1", port = 5000)