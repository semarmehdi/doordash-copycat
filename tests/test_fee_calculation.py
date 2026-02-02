import requests


def test_fee_calculation():
    payload = {"distance_km": 10, "weight_kg": 15}
    response = requests.post("http://localhost:8080/calculate-fee", json=payload)
    assert response.status_code == 200
    assert "delivery_fee" in response.json()
    assert response.json()["delivery_fee"] == 22.5
