from src.db.db import DB
from bson.objectid import ObjectId
from datetime import datetime
from src.exception.exception import DuplicateDocument, NoDocumentFound
from src.helpers.utils import Utils


class User:
    collection_name = "users"

    @classmethod
    def create_user(cls, name, email, roles, phone_number=None):
        connection = DB.get_connection()
        collection = connection.get_collection(cls.collection_name)
        existing_user = collection.find_one({"email": email})
        if existing_user is not None:
            raise DuplicateDocument(409, "User with email : {} already exits".format(email))
        roles = map(lambda x: ObjectId(x), roles)
        document = {"name": name,
                    "email": email,
                    "roles": list(roles),
                    "phone_number": phone_number,
                    "created_at": datetime.utcnow()}

        result = collection.insert_one(document)

        return str(result.inserted_id)

    @classmethod
    def get_user_by_id(cls, user_id):
        connection = DB.get_connection()
        collection = connection.get_collection(cls.collection_name)
        user = collection.find_one({"_id": ObjectId(user_id)})
        if user is None:
            raise NoDocumentFound(404, "user not found with id : {}".format(user_id))

        user = Utils.parse_document(user)
        return user

    @classmethod
    def get_all_user(cls):
        connection = DB.get_connection()
        collection = connection.get_collection(cls.collection_name)
        data_to_return = []
        all_user = collection.find({}).sort("created_at", -1)
        if all_user.count() == 0:
            raise NoDocumentFound(404, "No user found")
        for each_user in all_user:
            data_to_return.append(Utils.parse_document(each_user))

        return data_to_return
