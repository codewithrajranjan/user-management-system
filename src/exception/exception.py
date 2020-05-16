class UserDefinedException(Exception):
    def __init__(self, code, message, data):
        self.code = code
        self.message = message
        self.data = data

    def get_code(self):
        return self.code

    def get_message(self):
        return self.message

    def get_data(self):
        return self.data


class DuplicateDocument(UserDefinedException):
    def __init__(self, code, message, data=None):
        super().__init__(code, message, data)


class NoDocumentFound(UserDefinedException):
    def __init__(self, code, message, data=None):
        super().__init__(code, message, data)
