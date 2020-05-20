from app import flask_app
from flask import request, jsonify
from src.db.Permission import Permission


@flask_app.route("/api/v1.0/permission", methods=["POST"])
def create_permission():
    request_body = request.get_json(force=True) or {}
    name = request_body.get("name", None)
    if name is None:
        data_to_return = {
            "status": "error",
            "code": "PERMISSION_CREATION_FAILED",
            "message": "name is mandatory"}
        return jsonify(data_to_return), 400

    identifier = request_body.get("identifier", None)
    if identifier is None:
        data_to_return = {
            "status": "error",
            "code": "PERMISSION_CREATION_FAILED",
            "message": "identifier is mandatory"}
        return data_to_return, 400

    permission_id = Permission.create_permission(name, identifier)
    data_to_return = {"status": "success",
                      "code": "PERMISSION_CREATED",
                      "message": "permission successfully created",
                      "data": [{"id": permission_id}]}
    return data_to_return, 200
