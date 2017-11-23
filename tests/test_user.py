import unittest
from  app import app


class Test_user(unittest.TestCase):
	def setUp(self):
		self.client=app.test_client()


	def test_newuser(self):
		self.payload=dict(username="govan", password="Govan1234", conf_password="Govan1234")
		response=self.client.post("/signup", data=self.payload, follow_redirects=True)
		self.assertEqual(response.status_code, 200)

	def test_signup_existing_user(self):
		self.payload=dict(username="govan", password="Govan1234", conf_password="Govan1234")
		self.client.post("/signup", data=self.payload, follow_redirects=True)
		response=self.client.post("/signup", data=self.payload, follow_redirects=True)
		self.assertEqual(response.data, "user already exists")

	def test_signup_short_password(self):
		self.payload=dict(username="govan", password="Govan", conf_password="Govan")
		response=self.client.post("/signup", data=self.payload, follow_redirects=True)
		self.assertEqual(response.data, "password should be more than eight characters and contain a capital letter and number")

	def test_signup_password_without_capital(self):
		self.payload=dict(username="govan", password="govan1234", conf_password="govan1234")
		response=self.client.post("/signup", data=self.payload, follow_redirects=True)
		self.assertEqual(response.data, "password should be more than eight characters and contain a capital letter and number")

	def test_signup_password_without_number(self):
		self.payload=dict(username="govan", password="Govangovan", conf_password="Govangovan")
		response=self.client.post("/signup", data=self.payload, follow_redirects=True)
		self.assertEqual(response.data, "password should be more than eight characters and contain a capital letter and number")

	def test_user_login(self):
		self.payload=dict(username="govan", password="Govan1234", conf_password="Govan1234")
		self.client.post("/signup", data=self.payload)
		response=self.client.post("/login", data=self.payload, follow_redirects=True)
		self.assertEqual(response.status_code, 200)

	def test_user_login_invalid_credentials(self):
		self.payload=dict(username="govan", password="Govan1234", conf_password="Govan1234")
		self.client.post("/signup", data=self.payload)
		self.payload=dict(username="govan", password="Password1")
		response=self.client.post("/login", data=self.payload, follow_redirects=True)
		self.assertEqual(response.data, "username or password does not exist")
