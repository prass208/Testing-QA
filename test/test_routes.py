import json
import pytest


# Tambahkan decorator @pytest.fixture untuk mendapatkan klien
@pytest.fixture
def client(app):
    return app.test_client()


def test_product_detail_api(client):
    id = 1
    response = client.get(f"/api/products/{id}")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert id == data.get("id")


def test_product_api(client):
    response = client.get("/api/products")  # Ganti url ke endpoint yang benar
    assert response.status_code == 200
    # Periksa bahwa responsenya berupa list
    assert isinstance(json.loads(response.data), list)


def test_create_cart_api(client):
    # Simulasikan data untuk membuat cart
    cart_data = {
        "coupon_code": "DISCOUNT123",
        "shipping_fee": 10.0,
        "cart_items": [{"product_id": 1, "qty": 2}, {"product_id": 2, "qty": 1}],
    }
    response = client.post("/api/cart", json=cart_data)
    assert response.status_code == 200
    assert response.data == b"data created"  # Sesuaikan dengan respons yang seharusnya


def test_get_carts_api(client):
    response = client.get("/api/cart")
    assert response.status_code == 200
    assert isinstance(json.loads(response.data), list)


def test_delete_cart_api(client):
    # Simulasikan ID cart yang ingin dihapus
    cart_id_to_delete = 1
    response = client.delete(f"/api/cart/{cart_id_to_delete}")
    assert response.status_code == 200
    assert (
        response.data == f"cart-{cart_id_to_delete} deleted".encode()
    )  # Sesuaikan dengan respons yang seharusnya
