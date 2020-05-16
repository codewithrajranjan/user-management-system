class Utils:
    @classmethod
    def parse_document(cls, document):
        for key in document:
            if key == "_id":
                document["id"] = str(document["_id"])
                del document["_id"]

        return document
