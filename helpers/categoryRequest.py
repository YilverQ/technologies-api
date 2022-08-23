#We attend the POST or PUT request to return a dictionary
def data_request(jsonData):
	new_category = {
		"name" : jsonData["name"]
	}
	return new_category