from flask import Flask, jsonify, request
import json


app = Flask(__name__)


# mockdata - normally DB
stores = [
    {
    'name': 'my store',
    'items': [
        {
        'name': 'banana',
        'price': 5
        }
    ]
    },
    {
    'name': 'eric',
    'items': [
        {
        'name': 'sarahs',
        'price': 5
        }
    ]
    }
]

# post - reciving

# POST /store data: {   name:}  create a store obj
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)


# POST a item in a store

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item(name):
    request_data = request.get_json()
    for s in stores:
        if s['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            s['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'waring':'store not found'})

# get - sending

# GET store by name
@app.route('/store/<string:name>')
def return_store(name):
    res = None
    for s in stores:
        if s['name'] == name:
            res = stores["name"].get()
    return jsonify({'store': res})




#GET all stores
@app.route('/store')
def all_stores():
    return jsonify({'stores':stores})

# GET all items in a store
@app.route('/store/<string:name>/item')
def all_items(name):
    res = None
    for s in stores:
        if s['name'] == name:
            res = s.get('items')
    return jsonify({'{}_items'.format(name):res})


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
