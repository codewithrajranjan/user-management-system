from unittest import TestCase
from src.db.Role import Role
from src.exception.exception import DuplicateDocument, NoDocumentFound
from utils import clear_collection


class TestRole(TestCase):
    def setUp(self):
        clear_collection()

    def test_create_role_should_create_role(self):
        permission_list = ["permission1", "permission2", "permission3"]

        role_id = Role.create_role("student", permission_list)

        self.assertEqual(24, len(role_id))
        self.assertTrue("str", type(role_id))

    def test_create_role_should_raise_exception(self):
        permission_list = ["permission1", "permission2", "permission3"]
        Role.create_role("student", permission_list)
        self.assertRaises(DuplicateDocument, Role.create_role, "student", permission_list)

    def test_get_role_by_id_should_get_role(self):
        permission_list = ["permission1", "permission2", "permission3"]
        role_id = Role.create_role("student", permission_list)

        actual_role = Role.get_role_by_id(role_id)
        self.assertEqual(1, len(actual_role))
        actual_role = actual_role[0]
        self.assertEqual("student", actual_role["name"])
        self.assertEqual(permission_list, actual_role["permissions"])
        self.assertEqual(24, len(actual_role["id"]))

    def test_get_role_by_id_should_raise_exception_when_no_role_is_present(self):
        role_id = "5ebfab44d751a6ed494c361e"
        self.assertRaises(NoDocumentFound, Role.get_role_by_id, role_id)

    def test_get_all_role_should_be_success(self):
        Role.create_role("role1", ["permission1"])
        Role.create_role("role2", ["permission2"])
        Role.create_role("role3", ["permission3"])

        all_roles = Role.get_all_role()

        self.assertEqual(3, len(all_roles))
        first_role = all_roles[0]
        last_role = all_roles[2]
        self.assertEqual("role3", first_role["name"])
        self.assertEqual(["permission3"], first_role["permissions"])
        self.assertEqual("role1", last_role["name"])
        self.assertEqual(["permission1"], last_role["permissions"])

    def test_get_all_role_should_raise_exception_when_no_role_is_found(self):

        self.assertRaises(NoDocumentFound, Role.get_all_role)








