from sqlalchemy import Column, Integer, String, Float, DECIMAL
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    quantity = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price}, quantity={self.quantity})>"
