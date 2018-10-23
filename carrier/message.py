import json

class Message():

    def get_topic(self):
        return self._topic

    def get_message(self):
        return self._message    

class OutgoingMessage(Message):

    def __init__(self, topic, message):
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
        return json.loads(self._value)