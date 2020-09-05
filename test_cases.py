import os
import unittest
import json
from flaskr import create_app
from models import Account, setup_db


class AccountTestCase(unittest.TestCase):
    """This class represents the resource test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "bank"
        self.database_path = "postgres://{}:{}@{}/{}".format(
            'ahgarawani', 6898, 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_account = {
            'first_name': "Omar",
            'last_name': "Gaber",
            'balance': 5000
        }

    def tearDown(self):
        """Executed after each test"""
        pass

    # TODO add tests for endpoints and errors.

    def test_get_account_balance(self):
        res = self.client().get('/accounts/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['balance'])
    
    def test_404_non_existent_account(self):
        res = self.client().get('/accounts/1000000000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found!')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()



