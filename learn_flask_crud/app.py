from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory list of todos
todos = [
    {'id': 1, 'title': 'Learn Flask', 'done': False},
    {'id': 2, 'title': 'Build a CRUD app', 'done': False}
]

# Helper function to get a todo by id
def get_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            return todo
    return None

# READ: Get all todos
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify({'todos': todos})

# CREATE: Add a new todo
@app.route('/todos', methods=['POST'])
def create_todo():
    if not request.json or 'title' not in request.json:
        abort(400)  # Bad Request if no JSON or missing 'title'
    
    new_todo = {
        'id': todos[-1]['id'] + 1 if todos else 1,  # auto-increment id
        'title': request.json['title'],
        'done': False
    }
    todos.append(new_todo)
    return jsonify(new_todo), 201  # 201 Created

# UPDATE: Modify an existing todo
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = get_todo(todo_id)
    if not todo:
        abort(404)  # Not Found if the todo doesn't exist
    if not request.json:
        abort(400)
    
    # Validate input types if they exist
    if 'title' in request.json and not isinstance(request.json['title'], str):
        abort(400)
    if 'done' in request.json and not isinstance(request.json['done'], bool):
        abort(400)
    
    # Update fields, using existing values if not provided
    todo['title'] = request.json.get('title', todo['title'])
    todo['done'] = request.json.get('done', todo['done'])
    return jsonify(todo)

# DELETE: Remove a todo
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = get_todo(todo_id)
    if not todo:
        abort(404)
    todos.remove(todo)
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
