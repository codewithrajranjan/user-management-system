from src.db.db import DB


def clear_collection():
    db_connection = DB.get_connection()
    db_connection.drop_collection("permissions")
    db_connection.drop_collection("roles")
    db_connection.drop_collection("users")

