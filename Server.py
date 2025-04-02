from flask import Flask, jsonify, request


app = Flask(__name__)

data = [
    {'id': 1, 'name': 'item1'},
    {'id': 2, 'name': 'item2'},
]


@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)


@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in data if item['id'] == item_id), None)     #Fast Approach
    # item = [item for item in data if item['id'] == item_id]               #Slow Approach
    if item:
        return jsonify(item)
    return jsonify(({'message': 'Item not found'})), 404


@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.get_json()
    new_item['id'] = len(data) + 1
    data.append(new_item)
    return jsonify(new_item), 201


@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    updated_item = request.get_json()
    for index, item in enumerate(data):
        if item['id'] == item_id:
            updated_item['id'] = item_id
            data[index] = updated_item
            return jsonify(data)
    return jsonify({'Message': "Item not found!!!"})

# @app.route('/items/<int:item_id>', methods= ['DELETE'])
# def delete_item(item_id):
#     global data
#     data = [item for item in data if item['id']!=item_id]
#     return jsonify(data)


@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    for item in data:
        if item['id'] == item_id:
            data.remove(item)
            return jsonify(data)
    return jsonify({'Message': 'Item not found!'})


if __name__ == '__main__':
    app.run(debug=True)