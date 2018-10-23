import requests
from .message import Message

class EventHandler():

    def __init__(self, should_handle, handler):
        self._should_handle = should_handle
        self._handler = handler    

    def should_handle(self, message):
        return self._should_handle(message)

    def handle(self, message):
        self._handler(message)

class MessageManagerException(Exception):
    pass

class MessageManager():

    def __init__(self, topics, host, port, protocol="http", auth=""):
        self._topics = topics
        self._auth = auth
        self._host = host
        self._port = port
        self._protocol = protocol
        
        self._url = "{}://{}:{}".format(protocol, host, port)
        self._headers = {
            'Authorization': self._auth,
            'Content-Type': 'application/json'
        }
        self._event_handlers = []
        
    def register_event_handler(self, should_handle, handler):
        self._event_handlers.append(
            EventHandler(should_handle, handler)
        )

    def send_one(self, message):
        if not message:
            raise MessageManagerException("No message to send")
        if not isinstance(message, Message):
            raise MessageManagerException(
                "Expects for <class 'Message'> instance, but {} found".format(type(message))
            )
        payload = {
            'topic': message.get_topic(),
            'message': message.get_message()
        }
        try:
            url = "{}/produce/".format(self._url)
            r = requests.post(url, headers = self._headers, json=payload)
            if r.status_code == 200:
                if r.json() and r.json()['status'] == 'success':
                    # TODO
                    return {
                        'status': 'success',
                        'message': 'message was sent successfully'
                    }
                else:
                    # TODO
                    raise Exception("TODO")
            else:
                error = "{}; status={}; body={}".format(
                    "Error happened during message sending", r.status_code, r.text
                )
                raise MessageManagerException(error)
        except requests.RequestException as err:
            raise MessageManagerException(err)

    def send_many(self, messages=[]):
        pass

    def handle_message(self, message):
        for event_handler in self._event_handlers:
            if event_handler.should_handle(message):
                event_handler.handle(message)
