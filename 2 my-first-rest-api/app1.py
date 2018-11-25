from flask import Flask

app = Flask(__name__)
stores = [
	{
		'name':'My WonderFul',
		'items':[
			{
				'name':'my Item',
				'price':15.99
			}
		]
	}
]

#POST /store data : {name:}
@app.route('/store',method=['POST'])
def create_store():
	pass

#Get /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
	pass

#Get /store
@app.route('/store')
def get_stores():
	pass

#POST /store/<string:name>/item {name:,price:}
@app.route('/store/<string:name>/item',method=['POST'])
def create_item_in_store(name):
	pass

#GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
	pass