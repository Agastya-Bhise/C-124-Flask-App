from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
        "id": 1,
        "contact": "9473506937",
        "name": "John Doe",
        "done": False
    },
    {
        "id": 2,
        "contact": "7984736245",
        "name": "Jane Doe",
        "done": False
    }
]

@app.route("/get-contact")
def get_tasks():
    return jsonify({
        "data": contacts
    })

@app.route("/add-contact", methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "ERROR",
            "message": "Please provide the data in a correct format (JSON)."
        }, 400)
    contact = {
        "id": contacts[-1]["id"] + 1,
        "contact": request.json["contact"],
        "name": request.json["name"],
        "done": False
    }

    contacts.append(contact)
    return jsonify({
        "message": "Contact added successfully.",
        "status": "Success"
    })

if (__name__) == "__main__":
    app.run(debug = True)