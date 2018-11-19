import json
from unittest import TestCase
from json.decoder import JSONDecodeError
from jsonschema.exceptions import ValidationError
from carrier_client.message import IncomingMessage, OutgoingMessage 
from carrier_client.utils import validate_payload
from .utils import get_valid_payload, get_invalid_payload

class TestMessage(TestCase):

    def test_json_has_all_required_fields(self):
        self.assertEqual(
            validate_payload(get_valid_payload()), 
            None
        )
        with self.assertRaises(ValidationError):
            validate_payload(get_invalid_payload())

    def test_message_class_method_validate_payload(self):
        pass

    def test_create_from_bytes(self):
        trash = b"qwertyiop"
        json_without_fields = b"{}"
        payload = {}
        for key in ["topic", "partition", "offset", "key", "value", "timestamp"]:
            payload[key] = 1

        with self.assertRaises(JSONDecodeError):
            IncomingMessage.create_from_bytes(trash)

        with self.assertRaises(KeyError):
            IncomingMessage.create_from_bytes(json_without_fields)

        with self.assertRaises(AttributeError):
            IncomingMessage.create_from_bytes(json.dumps(payload))

        try:
            IncomingMessage.create_from_bytes(json.dumps(payload).encode())
        except Exception:
            self.fail("test_create_from_bytes() raised Exception unexpectedly!")

    def test_message_try_to_parse(self):
        pass