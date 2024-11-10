from src.models.mysql.interfaces.ProductRepositoryInterface import (
    ProductsRepositoryInterface,
)
from src.models.redis.interfaces.redis_repository_interface import (
    RedisRepositoryInterface,
)
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse


class ProductFinder:
    def __init__(
        self,
        redis_repo: RedisRepositoryInterface,
        product_repo: ProductsRepositoryInterface,
    ) -> None:
        self.__redis_repo = redis_repo
        self.__product_repo = product_repo

    def find_by_name(self, http_request: HttpRequest) -> HttpResponse:
        product_id = http_request.params["product_id"]

        product = self.__find_in_cache(product_id)
        if not product:
            product = self.__find_in_sql(product_id)
            self.__insert_in_cache(product)

        return self.__format_response(product)

    def __find_in_cache(self, product_id: str) -> tuple:
        product_infos = self.__redis_repo.get_key(product_id)
        if product_infos:
            product_infos_list = product_infos.split(",")
            return {
                "product_id": product_id,
                "name": product_infos_list[0],
                "price": product_infos_list[1],
            }

        return None

    def __find_in_sql(self, product_id: str):
        product = self.__product_repo.find_product_by_id(product_id)
        if not product:
            raise Exception("Produto não encontrado")

        return product

    def __insert_in_cache(self, product) -> None:
        product_id = product.id
        value = f"{product.name},{product.price}"
        self.__redis_repo.insert_ex(product_id, value, ex=60)

    def __format_response(self, product) -> HttpResponse:
        return HttpResponse(
            status_code=200,
            body={
                "name": product.name,        
                "price": product.price,      
                "quantity": product.quantity 
            },
        )