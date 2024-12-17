from pydantic import BaseModel, Field
from typing import Optional

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class UserInDB(BaseModel):
    username: str
    hashed_password: str

class InventoryItem(BaseModel):
    item_name: str = Field(..., description="Name of the inventory item")
    quantity: int = Field(..., gt=0, description="Quantity to add")

    class Config:
        schema_extra = {
            "example": {
                "item_name": "bun",
                "quantity": 5
            }
        }
