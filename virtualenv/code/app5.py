from flask import Flask, request
from flask_restful import Resource,Api,reqparse
from flask_jwt import JWT,jwt_required

from security import authenticate,identity

app =Flask(__name__)
app.secret_key = 'jose'
api = Api(app)
jwt = JWT(app,authenticate,identity)
items = []

class Item(Resource):
	@jwt_required()
	def get(self,name):
		item = next(iter(filter(lambda x : x['name'] ==name, items)),None)
		return {'item':item}, 200 if item  else 404

	def post(self,name):
		if next(iter(filter(lambda x : x['name'] == name, items)),None):
			return {'message' : "An item '{}' already exist".format(name)},400
		data = request.get_json() #force=True then no need to pass contenttype
		item = {'name':name, 'price':data['price']}
		items.append(item)
		return item, 201

	def delete(self,name):
		global items
		items = list(filter(lambda x: x['name'] != name, items))
		return {'message':'Item deleted'}


	def put(self,name):
		parser = reqparse.RequestParser()
		parser.add_argument('price',
			type = float,
			required = True,
			help = 'This Field cannot be left blank!'
			)
		data = parser.parse_args()
		item = filter(lambda x : x['name'] ==name, items)
		if item == []:
			item = {'name':name,'price':data['price']}
			items.append(item)
		else:
			item[0].update(data)
		return item


class ItemList(Resource):
	def get(self):
		return {'items':items}

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
app.run(port=5000,debug=True)
		