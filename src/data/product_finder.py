from src.models.mysql.interfaces.ProductRepositoryInterface import ProductsRepositoryInterface
from src.models.redis.interfaces.redis_repository_interface import RedisRepositoryInterface

class Productfinder:
    def __init__(self, redis_repo: RedisRepositoryInterface, product_repo: ProductsRepositoryInterface) -> None:
        self.__redis_repo = redis_repo
        self.product_repo = product_repo