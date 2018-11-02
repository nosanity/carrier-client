class MessageManagerException(Exception):
    pass

class ExceptionMessage():
    
    @staticmethod
    def get_message_not_found():
        return "Message to send not found."

    @staticmethod
    def get_incorrect_protocol(protocol):
        return "Incorrect protocol, expects for 'http' or 'https', but {} found.".format(protocol)

    @staticmethod
    def get_incorrect_message_class(message):
        return "Incorrect message, expects for <class 'OutgoingMessage'> instance, but {} found.".format(type(message))

    @staticmethod
    def get_incorrect_topic(topic_to_send, available_topics):
        return "Passed topic '{}' to send, but only [{}] topics supported.".format(
            topic_to_send,
            ",".join([ "'{}'".format(topic) for topic in available_topics ])
        )

    @staticmethod
    def get_incorrect_topic_type(topic):
        return "Incorrect topic type, expects for <class 'str'> instance, but {} found.".format(type(topic))

    @staticmethod
    def get_carrier_exception(response):
        return "Carrier exception HTTP [{}], {}".format(response.status_code, response.text)

    @staticmethod
    def get_incorrect_handler(handler):
        return "Incorrect handler, expects for <class 'function'> instance, but {} found.".format(type(handler))

    @staticmethod
    def get_incorrect_payload_type(payload):
        return "Incorrect payload type, expects for <class 'dict'> instance, but {} found.".format(type(payload))

    @staticmethod
    def get_incorrect_json():
        return "Given message isn't a valid JSON"

    @staticmethod
    def get_incorrect_port(port):
        return "Incorrect port, expects port in ragne 1-65535 , but {} found.".format(port)        