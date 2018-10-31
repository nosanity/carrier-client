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
        data = json.loads(bytes.decode("utf-8"))
        instance = cls()
        instance._topic = data['topic']
        instance._partition = data['partition']
        instance._offset = data['offset']
        instance._key = data['key']
        instance._value = data['value']
        instance._timestamp = data['timestamp']
        return instance

    def validate(self):
        try:
            payload = json.loads(self._value)
        except ValueError:
            raise MessageManagerException(
                ExceptionMessage.get_incorrect_json()
            )

    def get_payload(self):
        self.validate()
        return json.loads(self._value)