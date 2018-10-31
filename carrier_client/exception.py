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
        return "Passed topic {} to send, but only [{}] topics supported.".format(
            topic_to_send,
            ",".join(available_topics)
        )

    @staticmethod
    def get_carrier_exception(response):
        return "Carrier exception HTTP [{}], {}".format(response.status_code, response.text)

    @staticmethod
    def get_incorrect_handler(handler):
        return "Incorrect handler, expects for <class 'function'> instance, but {} found.".format(type(message))

    @staticmethod
    def get_incorrect_json():
        return "Given message isn't a valid JSON"