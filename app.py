from flask import Flask
import model

app = Flask(__name__)


@app.route("/")
def index():
	return jsonify({"message" : "Hola Mundo, Esto es un API Con Flask",
					"message2": "Hola Internautas"})


@app.route("/products")
def products():
	products = model.get_products()
	return jsonify(products)


@app.route("/product/name/<string:name>")
def product_name(name):
	product = model.get_product_name(name.replace("&", " "))
	if product != None:
		return jsonify(product)
	
	return jsonify({"message" : "Sorry, Product Not Found!"})


@app.route("/products/tag/<string:tag>")
def products_tag(tag):
	products = model.get_products_tag(tag)
	if products != []:
		return jsonify(products)

	return jsonify({"message" : f"Sorry, We Don't Have Products With Tag {tag}"})


@app.route("/add_product", methods = ["POST"])
def add_product():
	new_product = {
		"name" : request.json["name"],
		"price" : request.json["price"],
		"tag" : request.json["tag"],
		"trademark" : request.json["trademark"],
		"type" : request.json["type"]
	}
	if not model.check_product_name(new_product["name"]):
		messsage = model.add_product(new_product)
		return jsonify({"message" : messsage})

	return jsonify({"message" : "Product has exist!"})



@app.route("/update_product/<string:product>", methods = ["PUT"])
def update_product(product):
	product = product.replace("&", " ")
	new_product = {
		"name" : request.json["name"],
		"price" : request.json["price"],
		"tag" : request.json["tag"],
		"trademark" : request.json["trademark"],
		"type" : request.json["type"]
	}
	if model.check_product_name(product):
		messsage = model.update_product(new_product, product)
		return jsonify({"message" : messsage})

	return jsonify({"message" : "Product not exist!"})


@app.route("/delete_product/<string:product>", methods = ["DELETE"])
def delete_product(product):
	product = product.replace("&", " ")
	if model.check_product_name(product):
		messsage = model.delete_product(product)
		return jsonify({"message" : messsage})

	return jsonify({"message" : "Product not exist!"})

#Prueba para hacerla local
if __name__ == "__main__":
	app.run(debug = True, port = 5000)