import json
import os

def get_data():
	#open file .JSON
	with open("data.json", "r") as json_file:
		return json.load(json_file)


def get_products():
	data = get_data()
	return data["Technologies"]


def get_product_name(find_product):
	data = get_data()
	for i in data["Technologies"]:
		if i["name"] == find_product:
			return i


def get_products_tag(tag_product):
	data = get_data()
	list_products = []
	for i in data["Technologies"]:
		if i["tag"] == tag_product:
			list_products.append(i)

	return list_products


def check_product_name(name):
	data = get_data()
	for i in data["Technologies"]:
		if i["name"] == name:
			return True

	return False


def add_product(product):
	data = get_data()
	data["Technologies"].append(product)
	with open("data.json", "w") as json_file:
		json.dump(data, json_file, indent = 4)

	return f"{product['name']} has added successfully!"


def update_product(product, name):
	data = get_data()
	for i in range(len(data["Technologies"])):
		if data["Technologies"][i]["name"] == name:			
			data["Technologies"][i] = product
			with open("data.json", "w") as json_file:
				json.dump(data, json_file, indent = 4)

			return "Product has updated successfully!"


def delete_product(name):
	data = get_data()
	for i in range(len(data["Technologies"])):
		if data["Technologies"][i]["name"] == name:
			data["Technologies"].pop(i)
			with open("data.json", "w") as json_file:
				json.dump(data, json_file, indent = 4)

			return "Product has deleted successfully!"


if __name__ == "__main__":
	data_prob = {
		"name" : "Samsung S8",
		"price" : 85,
		"tag" : "Phone",
		"trademark" : "Samsung",
		"type" : "Cellphone"
	}

	print(add_product(data_prob))