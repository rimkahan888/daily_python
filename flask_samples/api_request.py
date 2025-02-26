from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory list of todos (example data)
todos = [
    {"id": 1, "task": "Learn Flask", "done": False},
    {"id": 2, "task": "Build a REST API", "done": False},
]

def get_next_id():
    """Generate the next task ID."""
    return max(todo["id"] for todo in todos) + 1 if todos else 1

# GET all todos
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# GET a specific todo by ID
@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((todo for todo in todos if todo["id"] == todo_id), None)
    if todo:
        return jsonify(todo)
    return jsonify({"error": "Todo not found"}), 404

# POST a new todo
@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    if not data or "task" not in data:
        return jsonify({"error": "Task is required"}), 400
    new_todo = {
        "id": get_next_id(),
        "task": data["task"],
        "done": False,
    }
    todos.append(new_todo)
    return jsonify(new_todo), 201

# PUT update an existing todo
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json()
    todo = next((todo for todo in todos if todo["id"] == todo_id), None)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    todo["task"] = data.get("task", todo["task"])
    todo["done"] = data.get("done", todo["done"])
    return jsonify(todo)

# DELETE a todo
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo["id"] != todo_id]
    return jsonify({"message": "Todo deleted"})

if __name__ == '__main__':
    app.run(debug=True)


"""
Footnotes:
1. Importing Libraries:
   - We import Flask, request, and jsonify to set up the web application, handle incoming requests, and return JSON responses.
2. Initializing the App:
   - The Flask application is initialized with `app = Flask(__name__)`.
3. In-memory Data:
   - The `todos` list holds sample todo items, each represented as a dictionary with an `id`, `task`, and `done` status.
4. ID Generation:
   - The `get_next_id()` function calculates the next available ID by finding the maximum current ID and adding 1 (or starting at 1 if the list is empty).
5. GET All Todos:
   - The `/todos` route (GET) returns the full list of todos as JSON.
6. GET Specific Todo:
   - The `/todos/<int:todo_id>` route (GET) searches for a todo by its ID and returns it, or an error message with a 404 status if not found.
7. Creating a Todo:
   - The POST `/todos` route expects JSON data containing a "task". It validates the input, creates a new todo with a unique ID, appends it to the list, and returns the new todo with a 201 (Created) status.
8. Updating a Todo:
   - The PUT `/todos/<int:todo_id>` route updates an existing todo by replacing the "task" and "done" fields with new values from the request, while retaining the current values if not provided.
9. Deleting a Todo:
   - The DELETE `/todos/<int:todo_id>` route filters out the todo with the specified ID from the list and returns a confirmation message.
10. Running the App:
    - The `if __name__ == '__main__':` block starts the Flask development server in debug mode, which is useful during development for detailed error messages and auto-reloading.
"""
