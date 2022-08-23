"""Imports from Model"""
from model.mark import MarkDB


class Mark():
	def __init__(self):
		self.mark = MarkDB()


	#Create a new mark.
	def create(self, data):
		mark = self.mark
		exist = mark.read_by_name(data["name"])
		if exist: 
			return f"Sorry, mark with the name {data['name']} already registered."
		else:
			return mark.create(data)


	#Read all marks.
	def read(self):
		mark = self.mark
		return mark.read() 


	#Read only mark.
	def read_only(self, id_mark):
		mark = self.mark
		return mark.read_only(id_mark)


	#Read only mark by name.
	def read_by_name(self, name):
		mark = self.mark
		return mark.read_by_name(name)


	#Update mark.
	def update(self, id_mark, data):
		mark = self.mark
		exist = mark.read_by_name(data["name"])
		if exist:
			if exist["id"] == id_mark:
				return mark.update(id_mark, data)
			else:
				return f"Sorry, mark with the name {data['name']} already registered."
		else:
			return mark.update(id_mark, data)


	#Delete mark.
	def delete(self, id_mark):
		mark = self.mark
		return mark.delete(id_mark)