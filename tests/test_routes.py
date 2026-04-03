import unittest
from app import app

class TestRoutes(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_list(self):
        response = self.client.get("/accounts")
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        response = self.client.post("/accounts", json={"name": "John"})
        self.assertEqual(response.status_code, 201)

if __name__ == "__main__":
    unittest.main()
