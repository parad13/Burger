from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

SQLALCHEMY_DATABASE_URL = "sqlite:///./kitchen.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String, unique=True, index=True)
    quantity = Column(Integer)

Base.metadata.create_all(bind=engine)

class InventoryItem(BaseModel):
    item_name: str
    quantity: int

@app.post("/inventory/add")
def add_inventory(item: InventoryItem):
    db = SessionLocal()
    db_item = db.query(Inventory).filter(Inventory.item_name == item.item_name).first()
    
    if db_item:
        db_item.quantity += item.quantity
    else:
        db_item = Inventory(item_name=item.item_name, quantity=item.quantity)
        db.add(db_item)
    
    db.commit()
    db.refresh(db_item)
    db.close()
    return {"message": "Inventory updated successfully"}

@app.get("/burgers/available")
def get_available_burgers():
    db = SessionLocal()
    inventory = {item.item_name: item.quantity for item in db.query(Inventory).all()}
    db.close()
    
    return {
        "complete_burgers": min(
            inventory.get("bun", 0),
            inventory.get("beef_patty", 0),
            inventory.get("lettuce", 0),
            inventory.get("tomato", 0),
            inventory.get("ketchup", 0)
        )
    }
    