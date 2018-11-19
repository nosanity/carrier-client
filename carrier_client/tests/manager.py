from random import randint
from unittest import TestCase
from carrier_client.message import Message, OutgoingMessage
from carrier_client.manager import MessageManager, EventHandler
from carrier_client.exception import MessageManagerException
from .utils import get_valid_payload

default_topics = ["foo", "bar"]

def create_message_manager(port=None, protocol=None):
    if not port and port != 0:
        port = randint(1, 65000)
    if not protocol and protocol != 0:
        protocol = "http"
    return MessageManager(
        topics=default_topics,
        host="localhost",
        port=port,
        protocol=protocol
    )
     
class TestManager(TestCase):

    def test_manager_outgoing_message_validation(self):
        message_manager = create_message_manager()
        payload = get_valid_payload()
        outgoing_message = OutgoingMessage(default_topics[0], payload)
        outgoing_message_without_topic = OutgoingMessage("", payload)
        
        with self.assertRaises(MessageManagerException):
            message_manager.validate_outgoing_message(None)

        with self.assertRaises(MessageManagerException):
            message_manager.validate_outgoing_message(Message())

        with self.assertRaises(MessageManagerException):
            message_manager.validate_outgoing_message(outgoing_message_without_topic)

        try:
            message_manager.validate_outgoing_message(outgoing_message)
        except MessageManagerException:
            self.fail("test_manager_outgoing_message_validation() raised MessageManagerException unexpectedly!")

    def test_manager_hander_functions_validation(self):
        message_manager = create_message_manager()
        valid = lambda x: x
        invalid1, invalid2, invalid3, invalid4 = 1, "str", [], None

        try:
            message_manager.register_event_handler(valid, valid)
        except MessageManagerException:
            self.fail("test_manager_hander_functions_validation() raised MessageManagerException unexpectedly!")

        with self.assertRaises(MessageManagerException):
            message_manager.register_event_handler(valid, invalid1)

        with self.assertRaises(MessageManagerException):
            message_manager.register_event_handler(invalid2, valid)

        with self.assertRaises(MessageManagerException):
            message_manager.register_event_handler(valid, invalid3)

        with self.assertRaises(MessageManagerException):
            message_manager.register_event_handler(valid, invalid4)

        with self.assertRaises(MessageManagerException):
            message_manager.register_event_handler(invalid3, invalid4)

    def test_manager_protocol_validation(self):
        with self.assertRaises(MessageManagerException):
            create_message_manager(protocol=0)

        with self.assertRaises(MessageManagerException):
            create_message_manager(protocol="ftp")

        with self.assertRaises(MessageManagerException):
            create_message_manager(protocol="ws")

        try:
            create_message_manager(protocol="http")
        except MessageManagerException:
            self.fail("test_manager_protocol_validation() raised MessageManagerException unexpectedly!")

        try:
            create_message_manager(protocol="https")
        except MessageManagerException:
            self.fail("test_manager_protocol_validation() raised MessageManagerException unexpectedly!")

    def test_manager_port_validation(self):
        with self.assertRaises(MessageManagerException):
            create_message_manager(port=0)

        with self.assertRaises(MessageManagerException):
            create_message_manager(port=65535)       

        try:
            create_message_manager(port=1)
        except MessageManagerException:
            self.fail("test_manager_port_validation() raised MessageManagerException unexpectedly!")

        try:
            create_message_manager(port=65534)
        except MessageManagerException:
            self.fail("test_manager_port_validation() raised MessageManagerException unexpectedly!")