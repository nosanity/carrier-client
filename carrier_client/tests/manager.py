from unittest import TestCase
from carrier_client.manager import MessageManager
from carrier_client.exception import MessageManagerException

class TestManager(TestCase):

    def test_manager_port_validation(self):

        def create_message_manager(port):
            message_manager = MessageManager(
                topics=[],
                host="localhost",
                port=port
            )

        with self.assertRaises(MessageManagerException):
            create_message_manager(0)

        with self.assertRaises(MessageManagerException):
            create_message_manager(65535)
            
        try:
            create_message_manager(1)
        except MessageManagerException:
            self.fail("test_manager_port_validation() raised MessageManagerException unexpectedly!")

        try:
            create_message_manager(65534)
        except MessageManagerException:
            self.fail("test_manager_port_validation() raised MessageManagerException unexpectedly!")