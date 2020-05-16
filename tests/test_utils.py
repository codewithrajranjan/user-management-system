from unittest import TestCase
from src.helpers.utils import Utils


class TestUtils(TestCase):
    def test_parse_document_should_remap_id(self):
        document = {"_id": "test_id"}

        actual_document = Utils.parse_document(document)
        self.assertEqual("test_id", actual_document["id"])
        self.assertTrue("_id" not in document)