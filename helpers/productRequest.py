#We attend the POST or PUT request to return a dictionary
def data_request(jsonData):
	new_product = {
		"name" : jsonData["name"],
		"price": jsonData["price"],
		"id_mark" : jsonData["id_mark"]
	}
	return new_product