from src.models.mysql.interfaces.ProductRepositoryInterface import (
    ProductsRepositoryInterface,
)
from src.models.redis.interfaces.redis_repository_interface import (
    RedisRepositoryInterface,
)
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class ProductCreator:
    
    def __init__(
        self,
        redis_repo: RedisRepositoryInterface,
        product_repo: ProductsRepositoryInterface,
    ) -> None:
        self.__redis_repo = redis_repo
        self.__product_repo = product_repo
    
    def create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body

        print(f"Request body: {body}")

        if not isinstance(body, dict):
            raise ValueError("Invalid body format")

        required_keys = ["name", "price", "quantity"]
        for key in required_keys:
            if key not in body:
                raise ValueError(f"Missing required field: {key}")

        name = body["name"]
        price = body["price"]
        quantity = body["quantity"]

        self.__insert_product_in_sql(body)
        self.__insert_product_in_cache(name, price, quantity)

        return self.__format_response()

    def __insert_product_in_sql(self, body: dict) -> None:
        self.__product_repo.insert_product(body)

    def __insert_product_in_cache(self, name: str, price: str, quantity: int) -> None:
        product_key = name
        value = f"{price}, {quantity}"
        self.__redis_repo.insert_ex(product_key, value, ex=60)

    def __format_response(self) -> HttpResponse:
        return HttpResponse(
            status_code=201, body={"msg": "Produto inserido com sucesso!"}
        )

