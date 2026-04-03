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
