from flask import Blueprint, jsonify, request

app = Blueprint("accounts", __name__)

accounts = []

@app.route("/accounts", methods=["GET"])
def list_accounts():
    return jsonify(accounts), 200

@app.route("/accounts", methods=["POST"])
def create_account():
    data = request.get_json()
    data["id"] = len(accounts) + 1
    accounts.append(data)
    return jsonify(data), 201

@app.route("/accounts/<int:id>", methods=["GET"])
def read_account(id):
    for acc in accounts:
        if acc["id"] == id:
            return jsonify(acc), 200
    return {}, 404

@app.route("/accounts/<int:id>", methods=["PUT"])
def update_account(id):
    for acc in accounts:
        if acc["id"] == id:
            acc.update(request.get_json())
            return jsonify(acc), 200
    return {}, 404

@app.route("/accounts/<int:id>", methods=["DELETE"])
def delete_account(id):
    global accounts
    accounts = [acc for acc in accounts if acc["id"] != id]
    return "", 204
