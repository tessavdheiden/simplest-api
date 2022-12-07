from fastapi.testclient import TestClient

# Import our app from main.py.
from main import app

# Instantiate the testing client with our app.
client = TestClient(app)


# Test with and without the query parameter
def test_api_get_item_query_parameter():
    r = client.get("/items/42")
    assert r.status_code == 200
    assert r.json() == {"fetch": "Fetched 1 of 42"}
    r = client.get("/items/42?count=10")
    assert r.status_code == 200
    assert r.json() == {"fetch": "Fetched 10 of 42"}


# Test a malformed URL
def test_api_malformed_url():
    r = client.get("/items")
    assert r.status_code != 200


def test_ingest_data():
    r = client.post(
        "/",
        json={"feature_1": 1.1, "feature_2": "my little pony"}
    )
    assert r.status_code == 200
    assert r.json() == {
        "feature_1": 1.1,
        "feature_2": "my little pony",
    }
