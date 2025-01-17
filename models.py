from database import Base
from sqlalchemy import Column, Integer, String, Float, Boolean
from pydantic import BaseModel, Field

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, primary_key=False, index=True)
    description = Column(String, index=False)
    price = Column(Float)
    is_available = Column(Boolean, default=True)

class ProductRequest(BaseModel):
    name: str = Field(min_length=1)
    description: str = Field(min_length=3, max_length=500)
    price: float = Field(gt=0)
    is_available: bool