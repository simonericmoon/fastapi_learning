from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()

products = []

class Product(BaseModel):
    id: int
    name: str
    price: float
 
@app.get("/")
async def get_products():
    return products

@app.get("/products/{product_id}") #pathparameter
async def get_product(product_id: int):
    for product in products:
        if product.get("id") == product_id:
            return product
    return {"error": "Product not found"}

@app.put("/products/{product_id}")
async def update_product(product_id: int, product: Product):
    for index, p in enumerate(products):
        if p.get("id") == product_id:
            products[index] = product
            return {"sucess": "product updated successfully"}
    return {"error": "Product not found"}   

@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    for index, p in enumerate(products):
        if p.get("id") == product_id:
            products.pop(index)
            return {"sucess": "product deleted successfully"}
    return {"error": "Product not found"}

#if __name__ == "__main__": 
#    uvicorn.run(app, host="127.0.0.1", port=4444) # also runnable with uvicorn main:app --port 4444 --reload

@app.post("/products")
async def create_product(product: Product):
    products.append(product)
    return {"sucess": "product added successfully"}