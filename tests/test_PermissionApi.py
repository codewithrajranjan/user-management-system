from unittest import TestCase
from utils import clear_collection
from app import flask_app
import json


class PermissionApi(TestCase):
    def setUp(self):
        self.app = flask_app.test_client()
        clear_collection()

    def test_create_permission_should_fail_when_name_is_not_present(self):
        request_body = json.dumps({})

        response = self.app.post("api/v1.0/permission", data=request_body, content_type="application/json")

        self.assertEqual(400, response.status_code)
        response_data = response.get_json()
        self.assertEqual("error", response_data["status"])
        self.assertEqual("PERMISSION_CREATION_FAILED", response_data["code"])
        self.assertEqual("name is mandatory", response_data["message"])

    def test_create_permission_should_fail_when_identifier_is_not_present(self):
        request_body = json.dumps({"name": "Subscribe Book"})
        headers = {"Content-Type": "application/json"}
        response = self.app.post("api/v1.0/permission", data=request_body, content_type="application/json")

        self.assertEqual(400, response.status_code)
        response_data = response.get_json()
        self.assertEqual("error", response_data["status"])
        self.assertEqual("PERMISSION_CREATION_FAILED", response_data["code"])
        self.assertEqual("identifier is mandatory", response_data["message"])

    def test_create_permission_should_be_success(self):
        request_body = json.dumps({"name": "Subscribe Book",
                                   "identifier": "subscribe_book"})
        response = self.app.post("api/v1.0/permission", data=request_body, content_type="application/jsonL")

        self.assertEqual(200, response.status_code)
        response_data = response.get_json()
        self.assertEqual("success", response_data["status"])
        self.assertEqual("permission successfully created", response_data["message"])
        self.assertEqual("PERMISSION_CREATED", response_data["code"])
        self.assertEqual(24, len(response_data["data"][0]["id"]))
