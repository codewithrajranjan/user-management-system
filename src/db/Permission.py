from src.db.db import DB
from src.exception.exception import DuplicateDocument, NoDocumentFound
from bson.objectid import ObjectId
from src.helpers.utils import Utils
from datetime import datetime


class Permission:
    collection_name = "permissions"

    @classmethod
    def create_permission(cls, name, identifier):
        conn = DB.get_connection()
        collection = conn.get_collection(cls.collection_name)
        existing_permission = collection.find_one({"identifier": identifier})
        if existing_permission is not None:
            raise DuplicateDocument(409, "permission exists with identifier : {}".format(identifier))

        document = {"name": name,
                    "identifier": identifier,
                    "created_at": datetime.utcnow()}

        result = collection.insert_one(document)
        inserted_id = result.inserted_id
        if inserted_id is not None:
            return str(inserted_id)
        return None

    @classmethod
    def get_permission_by_id(cls, permission_id):
        conn = DB.get_connection()
        collection = conn.get_collection(cls.collection_name)
        data_to_return = []

        permission = collection.find_one({"_id": ObjectId(permission_id)})
        if permission is None:
            raise NoDocumentFound(404, "No permission found with id : {}".format(permission_id))
        permission = Utils.parse_document(permission)
        data_to_return.append(permission)
        return data_to_return

    @classmethod
    def get_all_permission(cls):
        conn = DB.get_connection()
        collection = conn.get_collection(cls.collection_name)
        data_to_return = []
        all_document = collection.find({}).sort("created_at", -1)

        if all_document.count() == 0:
            raise NoDocumentFound(404, "No permission found")

        for each_document in all_document:
            data_to_return.append(Utils.parse_document(each_document))

        return data_to_return
