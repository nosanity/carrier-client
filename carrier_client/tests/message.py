import json
from unittest import TestCase
from carrier_client.message import OutgoingMessage 
from carrier_client.utils import validate_payload

class TestMessage(TestCase):

    """
    def test_is_json(self):
        payload_from_bytes = json.loads(b"{\"key\":\"value\"}")

        outgoing_message = OutgoingMessage("", payload_from_bytes)
        payload_from_message = outgoing_message.get_payload()

        self.assertTrue(isinstance(payload_from_message, dict))
    """

    def test_json_has_all_required_fields(self):
        payload = {}
        payload["id"] = {}
        payload["type"] = ""
        payload["source"] = ""
        payload["action"] = "create"
        payload["version"] = 1
        payload["timestamp"] = "2004-02-12T15:19:21+03:00"

        result = validate_payload(payload)
        
        self.assertEqual(result, None)