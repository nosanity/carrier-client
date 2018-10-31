import json
from .exception import MessageManagerException, ExceptionMessage

class Message():

    def get_topic(self):
        return self._topic

    def get_message(self):
        return self._message    

class OutgoingMessage(Message):

    def validate(self, message):
        try:
            json = json.loads(message)
        except ValueError:
            raise MessageManagerException(
                ExceptionMessage.get_incorrect_json()
            )
            # contains fields

    def __init__(self, topic, message):
        # TODO validate message format
        self._topic = topic
        self._message = message

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

    def get_message(self):
        # TODO check that it's json and it's in format
        return json.loads(self._value)