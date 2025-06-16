from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017")
db = client.todo_db
collection = db.todo_items

@app.route("/submittodoitem", methods=["POST"])
def submit_todo():
    item_name = request.form.get("itemName")
    item_desc = request.form.get("itemDescription")

    if not item_name or not item_desc:
        return jsonify({"error": "Missing fields"}), 400

    item = {"name": item_name, "description": item_desc}
    collection.insert_one(item)

    return jsonify({"message": "Item saved"}), 200

if __name__ == "__main__":
    app.run(debug=True)
