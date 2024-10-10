import unittest

from loan_methods.loan_rquirements import LoanContract
from loan_methods.loan_user import User

class MyTestCase(unittest.TestCase):
    def test_user_can_input_credentials(self):
        user = User("Timothy","Idowu")
        self.assertEqual(user._first_name, "Timothy")
        self.assertEqual(user._last_name, "Idowu")

    def test_user_can_input_correct_credentials(self):
        with self.assertRaises(ValueError):
            User("Tim1thy", "Idowu")

    def test_i_can_get_user_in_string_method(self):
        user = User("Timothy","Idowu")
        self.assertEqual(user._user_to_string(), "Timothy, Idowu")

    def test_user_can_input_requirements(self):
        user = User("Timothy","Idowu")
        requirements = LoanContract(user, 7000, 2)
        self.assertEqual(requirements.user._first_name,"Timothy")

    def test_To_Get_the_monthly_payment(self):
        user = User("Timothy","Idowu")
        requirements = LoanContract(user, 7000, 2)
        self.assertEqual(requirements.monthly_payment(),2.3643898043695103e-31)

    def test_to_get_full_payment(self):
        user = User("Timothy","Idowu")
        requirements = LoanContract(user, 7000, 2)
        self.assertEqual(requirements.total_payment(),5.674535530486824e-30)