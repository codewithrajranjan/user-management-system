from unittest import TestCase
from utils import clear_collection
from src.db.Permission import Permission
from src.exception.exception import DuplicateDocument, NoDocumentFound


class TestPermission(TestCase):
    def setUp(self):
        clear_collection()

    def test_create_permission_should_create_permission(self):
        actual_response = Permission.create_permission("test-name", "identifier1")
        self.assertIsNotNone(actual_response)
        self.assertEqual(24, len(actual_response))

    def test_create_permission_should_throw_exception_when_identifier_already_exits(self):
        first_permission = Permission.create_permission("test-name", "identifier1")
        self.assertEqual(24, len(first_permission))
        self.assertRaises(DuplicateDocument, Permission.create_permission, "test-name2", "identifier1")

    def test_get_permission_by_id_should_be_success(self):
        permission_id = Permission.create_permission("test-name", "identifier1")

        permissions = Permission.get_permission_by_id(permission_id)
        self.assertTrue(len(permissions) > 0)
        first_permission = permissions[0]
        self.assertTrue(permission_id, first_permission["id"])
        self.assertTrue("test-name", first_permission["name"])
        self.assertTrue("identifier1", first_permission["identifier"])

    def test_get_permission_by_id_should_raise_exception(self):
        self.assertRaises(NoDocumentFound, Permission.get_permission_by_id, "5ebfab44d751a6ed494c361e")

    def test_get_all_permissions_should_be_success(self):
        Permission.create_permission("name", "identifier1")
        Permission.create_permission("name1", "identifier2")
        Permission.create_permission("name2", "identifier3")

        actual_response = Permission.get_all_permission()

        self.assertTrue(3, len(actual_response))
        first_document = actual_response[0]
        self.assertEqual("name2", first_document["name"])
        self.assertEqual("identifier3", first_document["identifier"])
        last_document = actual_response[2]
        self.assertEqual("name", last_document["name"])
        self.assertEqual("identifier1", last_document["identifier"])

    def test_get_all_permissions_should_raise_exception(self):

        self.assertRaises(NoDocumentFound, Permission.get_all_permission)
















