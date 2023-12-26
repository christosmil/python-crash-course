import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee."""

    def setUp(self):
        """Set up an instance of Employee and an amount of raise."""
        self.my_employee = Employee('donald', 'duck', 30_000)

    def test_give_default_raise(self):
        """Test the default salary raise."""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary, 35_000)

    def test_give_custom_raise(self):
        """Test a custom salary raise."""
        self.my_employee.give_raise(12_000)
        self.assertEqual(self.my_employee.annual_salary, 42_000)


if __name__ == "__main__":
    unittest.main()