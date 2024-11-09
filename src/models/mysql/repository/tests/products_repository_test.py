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

def test_fin_product():
    
    with app.app_context():
        repo = ProductsRepository()
        
        id_product = 1
        
        product = repo.find_product_by_id(id_product)
        
        assert product != None