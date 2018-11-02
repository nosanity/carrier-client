import json
from unittest import TestCase
from carrier_client.message import OutgoingMessage 
from carrier_client.utils import validate_payload

class TestMessage(TestCase):

    def test_json_has_all_required_fields(self):
        payload = {}
        payload["id"] = {}
        payload["type"] = ""
        payload["source"] = ""
        payload["title"] = ""
        payload["action"] = "create"
        payload["version"] = 1
        payload["timestamp"] = "2004-02-12T15:19:21+03:00"

        result = validate_payload(payload)
        
        self.assertEqual(result, None)