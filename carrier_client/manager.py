import requests
from .message import OutgoingMessage
from .exception import MessageManagerException, ExceptionMessage

class EventHandler():

    def __init__(self, should_handle, handler):
        self._should_handle = should_handle
        self._handler = handler    

    def should_handle(self, message):
        return self._should_handle(message)

    def handle(self, message):
        self._handler(message)

class MessageManager():

    def __init__(self, topics, host, port, protocol="http", auth="", timeout=None):
        self._topics = topics
        self._auth = auth
        self._host = host
        self._port = port
        self._protocol = protocol
        
        self.validate_init_parameters()

        self._url = "{}://{}:{}".format(protocol, host, port)
        self._produce_url = "{}/produce/".format(self._url)

        self._headers = {
            'Authorization': self._auth,
            'Content-Type': 'application/json'
        }
        self._event_handlers = []
        self.timeout = timeout
        
    def validate_init_parameters(self):
        if self._port < 1 or self._port > 65534:
            raise MessageManagerException(
                ExceptionMessage.get_incorrect_port(self._port)
            )                 
        if self._protocol not in ['http', 'https']:
            raise MessageManagerException(
                ExceptionMessage.get_incorrect_protocol(self._protocol)
            )            

    def validate_handler_function(self, funcs):
        for func in funcs:
            if not callable(func):
                raise MessageManagerException(
                    ExceptionMessage.get_incorrect_handler(func)
                )

    def validate_outgoing_message(self, message):
        if not message:
            raise MessageManagerException(
                ExceptionMessage.get_message_not_found()
            )
        if not isinstance(message, OutgoingMessage):
            raise MessageManagerException(
                ExceptionMessage.get_incorrect_message_class(message)
            )
        if message.get_topic() not in self._topics:
            raise MessageManagerException(
                ExceptionMessage.get_incorrect_topic(message.get_topic(), self._topics)
            )            

    def register_event_handler(self, should_handle, handler):
        self.validate_handler_function([should_handle, handler])
        self._event_handlers.append(
            EventHandler(should_handle, handler)
        )

    def send_one(self, message, timeout=None):
        timeout = timeout or self.timeout
        self.validate_outgoing_message(message)
        data = {
            'topic': message.get_topic(),
            'payload': message.get_payload()
        }
        r = requests.post(self._produce_url, headers = self._headers, json=data, timeout=timeout)
        if r.status_code != 200:
            raise MessageManagerException(
                ExceptionMessage.get_carrier_exception(r)
            )

    def handle_message(self, message):
        # Trust to user that message is instance of IncomingMessage
        for event_handler in self._event_handlers:
            if event_handler.should_handle(message):
                event_handler.handle(message)


def check_kafka_status(host, port, protocol="http", auth="", timeout=None):
    url = "{}://{}:{}/api/check/".format(protocol, host, port)
    headers = {
        'Authorization': auth,
        'Content-Type': 'application/json'
    }
    try:
        resp = requests.post(url, headers=headers, timeout=timeout)
        return resp.status_code
    except requests.RequestException:
        return
