class HttpResponse:
    def __init__(self, body: dict, status_code: dict) -> None:
        self.__body = body
        self.__params = status_code