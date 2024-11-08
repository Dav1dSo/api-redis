from src.models.mysql.repository.products_repository import ProductsRepository
from factory import create_app

app = create_app()

def test_insert_product():
    
    with app.app_context():
        repo = ProductsRepository()
    
        data = {
            "name": "produto 1",
            "price": "123.30",
            "quantity": "4"
        }
        
        repo.insert_product(data)
        