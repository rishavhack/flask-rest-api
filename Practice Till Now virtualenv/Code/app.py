from flask import Flask, request
from flask_restful import Resource,Api,reqparse


app = Flask(__name__)

api = Api(app)
items = []

class Item(Resource):
	def get(self,name):
		for item in items:
			if item['name'] == name:
				return item
		return {'item':None},404

	def post(self,name):
		for i in range(0,len(items)):
			if items[i]['name'] == name:
				return {'message':"An item '{}' already exist".format(name)},400
		data = request.get_json()
		item = {'name':name, 'price':data['price']}
		items.append(item)
		return item,201

	def delete(self,name):
		global items
		for i in range(0,len(items)):
			if items[i]['name'] == name:
				del items[i]
				return {'message':'Item deleted'}
		return {'message':'Not Found'}

	def put(self,name):
		parser = reqparse.RequestParser()
		parser.add_argument('price',
			type = float,
			required = True,
			help = 'This Field cannot be left')
		data = parser.parse_args()
		for i in range(0,len(items)):
			if items[i]['name'] == name:
				items[i]['name'] = name;
				items[i]['price'] = data['price']
				return items[i]
		return {'message':'Not Found'}



class ItemList(Resource):
	def get(self):
		return {'items':items}

		

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/getItems')
app.run(port=5000,debug=True)