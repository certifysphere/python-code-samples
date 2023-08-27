from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app, origins="http://localhost:3001")  # Replace with your React app's URL

todos = [
    {"id": 1, "title": "Buy groceries"},
    {"id": 2, "title": "Do laundry"},
]

next_id = len(todos) + 1

# Get all todos
@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# Get a single todo by ID
@app.route('/api/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if todo:
        return jsonify(todo)
    return jsonify({"message": "Todo not found"}), 404

# Create a new todo
@app.route('/api/todos', methods=['POST'])
def create_todo():
    global next_id
    data = request.json
    new_todo = {"id": next_id, "title": data["title"]}
    todos.append(new_todo)
    next_id += 1
    return jsonify(new_todo), 201

# Update an existing todo
@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.json
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if todo:
        todo['title'] = data['title']
        return jsonify(todo)
    return jsonify({"message": "Todo not found"}), 404

# Delete a todo
@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t['id'] != todo_id]
    return jsonify({"message": "Todo deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
