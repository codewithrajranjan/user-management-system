from unittest import TestCase
import os


class TestDB(TestCase):
    def setUp(self) :
        os.environ["DATABASE_HOST"] = "192.168.0.10"

    def test_get_connection_should_return_a_valid_db_connection(self):
        from src.db.db import DB
        actual_value = DB.get_connection()
        col_ref = actual_value.get_collection("dummy-collection")
        col_ref.insert_one({"key": "value"})
        self.assertIsNotNone(actual_value)
