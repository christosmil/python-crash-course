"""
Testing your code
When you write a function or a class, you can also write tests for that code.
Testing proves that your code works as it's supposed to in the situations it's
designed to handle, and also when people use your programs in unexpected ways.
Writing tests gives you confidence that your code will work correcly as more
people begin to use your programs. You can also add new features to your
programs and know whether or not you've broken existing behavior by running your
tests. A unit test verifies that one specific aspect of your code works as it's
supposed to. A test case is a collection of unit tests which verify that your
code's behavior is correct in a wide variety of situtations.
"""

"""
Testing a function: a passing test
Python's unittest module provides tools for testing your code. To try it out,
we'll create a function that returns a full name. We'll use the function in a
regular program, and then build a test case for the function.
"""
# Building a test case with one unit test
import unittest
from full_names import get_full_name

class NamesTestCase(unittest.TestCase):
    """Tests for names.py."""

    def test_first_last(self):
        """Test names like Janis Joplin."""
        full_name = get_full_name('janis', 'joplin')
        self.assertEqual(full_name, 'Janis Joplin')

"""
Testing a function: A failing test
Failing tests are important; they tell you that a change in the code has
affected existing behavior. When a test fails, you need to modify the code so
the existing behavior still works.
"""
# Running the test
# Fixing the code
# Running the test

"""
Adding new tests
You can add as many unit tests to a test case as you need. To write a new test,
add a new method to your test case class.
"""
# Testing middle names
import unittest
from full_names_2 import get_full_name as get_full_name_2

class NamesTestCase2(unittest.TestCase):
    """Tests for names.py."""

    def test_first_last(self):
        """Test names like Janis Joplin."""
        full_name = get_full_name_2('janis', 'joplin')
        self.assertEqual(full_name, 'Janis Joplin')

    def test_middle(self):
        """Test names like David Lee Roth."""
        full_name = get_full_name_2('david', 'roth', 'lee')
        self.assertEqual(full_name, 'David Lee Roth')

"""
Testing a class
Testing a class is similar to testing a function, since you'll mostly be testing
your methods.
"""
# Building a testcase
import unittest
from accountant import Accountant

class TestAccountant(unittest.TestCase):
    """Tests for the class Accountant."""

    def test_initial_balance(self):
        acc = Accountant()
        self.assertEqual(acc.balance, 0)

        acc = Accountant(100)
        self.assertEqual(acc.balance, 100)

"""
The setUp() method
When testing a class, you usually have to make an instance of the class. The
setUp() method is run before every test. Any instances you make in setUp() are
available in every test you write.
"""
# Using setUp() to support multiple tests
import unittest
from accountant import Accountant as Acc2

class TestAccountant2(unittest.TestCase):
    """Test for the class Accountant."""

    def setUp(self):
        self.acc = Acc2()

    def test_initial_balance(self):
        self.assertEqual(self.acc.balance, 0)

        acc = Acc2(100)
        self.assertEqual(acc.balance, 100)

    def test_deposit(self):
        self.acc.deposit(100)
        self.assertEqual(self.acc.balance, 100)

        self.acc.deposit(100)
        self.acc.deposit(100)
        self.assertEqual(self.acc.balance, 300)

    def test_withdrawal(self):
        self.acc.deposit(1000)
        self.acc.withdraw(100)
        self.assertEqual(self.acc.balance, 900)


if __name__ == "__main__":
    unittest.main()