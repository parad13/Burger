from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

def test_add_inventory():
    # First get token
    response = client.post(
        "/token",
        data={"username": "test_user", "password": "test_password"}
    )
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Test adding inventory
    response = client.post(
        "/inventory/add",
        headers=headers,
        json={"item_name": "bun", "quantity": 5}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Inventory updated successfully"}

def test_get_available_burgers():
    # First get token
    response = client.post(
        "/token",
        data={"username": "test_user", "password": "test_password"}
    )
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Add all required ingredients
    ingredients = ["bun", "beef_patty", "lettuce", "tomato", "ketchup"]
    for item in ingredients:
        client.post(
            "/inventory/add",
            headers=headers,
            json={"item_name": item, "quantity": 3}
        )
    
    response = client.get("/burgers/available", headers=headers)
    assert response.status_code == 200
    assert response.json()["complete_burgers"] >= 3