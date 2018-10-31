import json
from carrier_client.message import OutgoingMessage 

from unittest import TestCase

class TestMessage(TestCase):
    def test_is_json(self):
        obj = OutgoingMessage(None, json.loads("{}"))
        message = obj.get_message()
        self.assertTrue(isinstance(message, dict))