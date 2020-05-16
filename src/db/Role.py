from datetime import datetime
from src.db.db import DB
from src.exception.exception import DuplicateDocument, NoDocumentFound
from bson.objectid import ObjectId
from src.helpers.utils import Utils


class Role:
    collection_name = "roles"

    @classmethod
    def create_role(cls, name, permissions):
        connection = DB.get_connection()
        collection = connection.get_collection(cls.collection_name)
        existing_role = collection.find_one({"name": name})
        if existing_role is not None:
            raise DuplicateDocument(409, "role with name : {} already exists".format(name))

        document_to_insert = {"name": name,
                              "permissions": permissions,
                              "created_at": datetime.utcnow()}

        result = collection.insert_one(document_to_insert)
        last_inserted_id = str(result.inserted_id)
        return last_inserted_id

    @classmethod
    def get_role_by_id(cls, role_id):
        data_to_return = []
        connection = DB.get_connection()
        collection = connection.get_collection(cls.collection_name)

        result = collection.find_one({"_id": ObjectId(role_id)})
        if result is None:
            raise NoDocumentFound(404, "No role found with id : {}".format(role_id))
        data_to_return.append(Utils.parse_document(result))
        return data_to_return

    @classmethod
    def get_all_role(cls):
        data_to_return = []
        connection = DB.get_connection()
        collection = connection.get_collection(cls.collection_name)

        all_roles = collection.find({}).sort("created_at", -1)
        if all_roles.count() is 0:
            raise NoDocumentFound(404, "No role found")
        for each_role in all_roles:
            data_to_return.append(Utils.parse_document(each_role))

        return data_to_return
