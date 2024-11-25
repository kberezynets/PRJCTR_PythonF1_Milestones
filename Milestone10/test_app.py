# Write unit tests for your web server, for example:
# Tests for successful case
# Tests for incorrect inputs
# Tests for reading corrupted CSV file

# To make testing easier, separate logic into functions
# that can easily be unit-tested.

import unittest
from flask import Flask
from app import app


class FlaskAPITestCase(unittest.TestCase):

    def setUp(self):
        # Set up the test client
        self.app = app.test_client()
        self.app.testing = True

    # ---------- Tests for Successful Case ----------
    def test_get_DB(self):
        response = self.app.get('/DB')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_get_total_birthdays(self):
        birthdays = {"employees": [
                        {
                            "birthday": "1989-04-20",
                            "department": "HR",
                            "hiring date": "2022-02-03",
                            "id": 6,
                            "name": "Vincent Acosta"
                        }
                    ],
                "total": 1
            }
        response = self.app.get(
            '/birthdays?month=april&department=HR', json=birthdays
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, birthdays)

    # ---------- Test for Incorrect Inputs ----------
    def test_get_total_birthdays_incorrect_month_name(self):
        # Non-existent month name
        response = self.app.get('/birthdays?month=appril&department=HR') 
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json["error"], "Incorrect month name")

    # ---------- Test for reading corrupted CSV file
    def test_get_DB_incorrect_csv(self):
        response = self.app.get('/DB')
        self.assertEqual(response.status_code, 200)
        employees = response.get_json()
        
        self.assertIsInstance(employees, list)

        for employee in employees:
            self.assertIn("name", employee)
            self.assertNotEqual(employee["name"], "")
            self.assertIn("hiring date", employee)
            self.assertNotEqual(employee["hiring date"], "")
            self.assertIn("department", employee)
            self.assertNotEqual(employee["department"], "")
            self.assertIn("birthday", employee)
            self.assertNotEqual(employee["birthday"], "")

if __name__ == '__main__':
    unittest.main()
