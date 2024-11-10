class HttpResponse:
    def __init__(self, body: dict, status_code: dict) -> None:
        self.body = body
        self.status_code = status_code