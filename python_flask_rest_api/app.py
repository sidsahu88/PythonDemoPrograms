from flask import Flask, jsonify, request

app = Flask(__name__)

items = [{"id": 1, "data": "apple"}, 
         {"id": 2, "data": "orange"},
         {"id": 3, "data": "banana"},
         {"id": 4, "data": "grapes"}]

@app.route('/')
def home():
    return 'Welcome to the Python REST API!'

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.get('/items/<int:item_id>')
def get_item_by_id(item_id):
    for item in items:
        if item['id'] == item_id:
            return jsonify(item)
    
    return jsonify({'error_msg':'user_id not found'}), 404

@app.post('/items/item')
def create_item():
    req_data = request.json
    item_id = len(items) + 1
    item = {'id':item_id, 'data': req_data['data']}
    items.append(item)
    return jsonify(item), 201

@app.delete('/items/<string:data>')
def delete_item(data):
    global items
    items = [item for item in items if item['data'] != data]
    return jsonify({'message': 'Item deleted successfully'}), 200

if __name__ == "__main__":
    app.run(port=8080, debug=True)