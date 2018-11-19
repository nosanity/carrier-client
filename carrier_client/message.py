import ast
import json
from .utils import validate_payload
from .exception import MessageManagerException, ExceptionMessage

class Message():

    def get_topic(self):
        return self._topic

    def get_payload(self):
        return self._payload    

class OutgoingMessage(Message):

    def validate(self, topic, payload):
        if type(topic) != str:
            raise MessageManagerException(
                ExceptionMessage.get_incorrect_topic_type(topic)
            )       
        if type(payload) != dict:
            raise MessageManagerException(
                ExceptionMessage.get_incorrect_payload_type(payload)
            )  
        validate_payload(payload)          

    def __init__(self, topic, payload):
        self.validate(topic, payload)
        self._topic = topic
        self._payload = payload

class IncomingMessage(Message):

    @classmethod
    def create_from_bytes(cls, bytes):
        # TODO implement validation (JSON, fields, payload format)
        data = json.loads(bytes.decode("utf-8"))
        instance = cls()
        instance._topic = data['topic']
        instance._partition = data['partition']
        instance._offset = data['offset']
        instance._key = data['key']
        instance._value = data['value']
        instance._timestamp = data['timestamp']
        return instance

    def try_to_parse(self):
        is_json = False
        try:
            payload = json.loads(self._value)
            is_json = True
        except ValueError:
            try:
                payload = ast.literal_eval(self._value)
                is_json = isinstance(payload, dict)
            except (ValueError, SyntaxError, TypeError):
                pass
        if not is_json:
            raise MessageManagerException(
                ExceptionMessage.get_incorrect_json()
            )
        return payload

    def get_payload(self):
        return self.try_to_parse()