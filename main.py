from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from fastapi import FastAPI, Depends, HTTPException, Path
import models
from models import Product, ProductRequest
from database import engine, SessionLocal
import uvicorn

app = FastAPI()

# Create tables based on models.py
models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

# Routes
@app.get('/products', status_code=status.HTTP_200_OK)
async def read_all_products(db: db_dependency):
    return db.query(Product).all()

@app.get('/product/{product_id}', status_code=status.HTTP_200_OK)
async def get_product_by_id(db: db_dependency, product_id: int = Path(gt=0)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is not None:
        return product
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')

@app.post('/product', status_code=status.HTTP_201_CREATED)
async def create_product(db: db_dependency, product_request: ProductRequest):
    new_product = Product(**product_request.model_dump())

    db.add(new_product)
    db.commit()
    return db.query(Product).filter(Product.id == new_product.id).first()

@app.put('/product/{product_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_product(db: db_dependency, product_request: ProductRequest, product_id: int = Path(gt=0)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')
    
    # Update product fields from request
    for var, value in vars(product_request).items():
        setattr(product, var, value) if value else None

    db.commit()

@app.delete('/product/{product_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(db: db_dependency, product_id: int = Path(gt=0)):
    product = db.query(Product).filter(Product.id == product_id).first()

    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')
    
    db.delete(product)
    db.commit()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)