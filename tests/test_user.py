import unittest
from  app import app


class Test_user(unittest.TestCase):
	def setUp(self):
		self.client=app.test_client()

	def test_newuser(self):
		self.payload=dict(username="govan", password="govan1")
		response=self.client.post("/signup", data=self.payload, follow_redirects=True)
		self.assertEqual(response.status_code, 200)

	def test_user_login(self):
		self.payload=dict(username="govan", password="govan1")
		self.client.post("/signup", data=self.payload)
		response=self.client.post("/login", data=self.payload, follow_redirects=True)
		self.assertEqual(response.status_code, 200)