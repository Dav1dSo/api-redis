from factory import db
from src.models.mysql.interfaces.ProductRepositoryInterface import ProductsRepositoryInterface
from src.models.mysql.entities.products import Product
import logging
class ProductsRepository(ProductsRepositoryInterface):
        
    def find_product_by_id(self, product_id: int) -> dict:
        product = db.session.query(Product).filter(Product.id == product_id).first()
        return product
    
    def insert_product(self, body: dict) -> None:
        try:
            nome = body["name"]
            price = body["price"]
            quantity = body["quantity"]
            
            new_product = Product(
                name=nome,
                price=price,
                quantity=quantity
            )
            
            db.session.add(new_product)
            
            db.session.commit()
            
        except Exception as err:
            db.session.rollback()
            logging.error(f"ERROR: {type(err)} - {err}")
            raise Exception("Error ao inserir produto!")