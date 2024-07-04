from pydantic import BaseModel, field_validator
from typing import Optional
from enum import Enum

class ProductCategory(Enum):
    FOOD = "food"
    ELECTRONICS = "electronics"
    CLOTHING = "clothing"

class Product(BaseModel):
    id: int
    name: str ="DEFAULTVALUE"
    price: float
    tags: list[str] = []
    description: Optional[str] = None
    category: ProductCategory

    @field_validator("price")
    def name_must_contain_space(cls, v):
        if v < 0:
            raise ValueError("price must be greater than 0")
        return v


product = Product(id=1, name="laptop", price=1000.0, tags=["electronics"], category="electronics")

product_dict = product.model_dump()
print(product_dict)

product2 = Product(**product_dict)
print(product2)