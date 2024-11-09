from abc import ABC, abstractmethod

class ProductsRepositoryInterface(ABC):
    
    @abstractmethod
    def find_product_by_id(self, product_id: int) -> dict: pass
    
    @abstractmethod
    def insert_product(self, body: dict) -> None: pass