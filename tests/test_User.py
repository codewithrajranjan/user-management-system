from unittest import TestCase
from src.exception.exception import DuplicateDocument, NoDocumentFound
from utils import clear_collection
from src.db.User import User


class TestUser(TestCase):
    def setUp(self):
        clear_collection()

    def test_create_user_should_be_success(self):
        roles = ["5ebfab44d751a6ed494c361e", "5ebfab44d751a6ed494c3612"]
        user_id = User.create_user("test-name", "test@gmail.com", roles, phone_number="test-phone")

        self.assertEqual(24, len(user_id))

    def test_create_user_should_raise_exception_when_email_is_duplicate(self):
        roles = ["5ebfab44d751a6ed494c361e", "5ebfab44d751a6ed494c3612"]
        user_id = User.create_user("tes    t-name", "test@gmail.com", roles, phone_number="test-phone")

        self.assertRaises(DuplicateDocument, User.create_user, "test-name", "test@gmail.com", roles)

    def test_get_user_by_id_should_be_success(self):
        roles = ["5ebfab44d751a6ed494c361e", "5ebfab44d751a6ed494c3612"]
        user_id = User.create_user("test-name", "test@gmail.com", roles, phone_number="phone-number")

        actual_user = User.get_user_by_id(user_id)

        self.assertTrue(len(actual_user) > 0)
        self.assertEqual(user_id, actual_user["id"])
        self.assertEqual("test-name", actual_user["name"])
        self.assertEqual("test@gmail.com", actual_user["email"])
        self.assertEqual("phone-number", actual_user["phone_number"])

    def test_get_user_by_id_should_raise_exception_for_invalid_user(self):
        user_id = "5ebfab44d751a6ed494c361e"
        self.assertRaises(NoDocumentFound, User.get_user_by_id, user_id)

    def test_get_all_user_should_be_success(self):
        roles = ["5ebfab44d751a6ed494c361e", "5ebfab44d751a6ed494c3612"]
        User.create_user("name1", "email@gmail.com", roles, phone_number="phone1")
        User.create_user("name2", "email2@gmail.com", roles)
        User.create_user("name3", "email3@gmail.com", roles)

        all_user = User.get_all_user()
        self.assertEqual(3, len(all_user))
        first_user = all_user[0]
        third_user = all_user[2]
        self.assertEqual("name3", first_user["name"])
        self.assertEqual("email3@gmail.com", first_user["email"])
        self.assertEqual("name1", third_user["name"])
        self.assertEqual("email@gmail.com", third_user["email"])

    def test_get_all_user_should_raise_exception(self):
        self.assertRaises(NoDocumentFound, User.get_all_user)








