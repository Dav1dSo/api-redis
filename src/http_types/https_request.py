class HttpRequest:
    def __init__(self, body: dict = None, params: dict = None) -> None:
        self.__body = body
        self.__params = params