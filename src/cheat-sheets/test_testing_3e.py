"""
Testing your code
When you write a function or a class, you can also write tests for that code.
Testing proves that your code works as it's supposed to in the situations it's
designed to handle, and also when people use your programs in unexpected ways.
Writing tests gives you confidence that your code will work correctly as more
people begin to use your programs. You can also add new features to your
programs and know whether or not you've broken existing behavior by running your
tests. A unit test verifies that one specific aspect of your code works as it's
supposed to. A test case is a collection of unit tests which verify that your
code's behavior is correct in a wide variety of situations.
"""

"""
Testing a function: a passing test
The pytest library provides tools for testing your code. To try it out, we'll
create a function that returns a full name. We'll use the function in a regular
program, and then build a test case for the function.
"""
# Building a test case with one unit test
from full_names import get_full_name

def test_first_last():
    """Test names like Janis Joplin."""
    full_name = get_full_name('janis', 'joplin')
    assert full_name == 'Janis Joplin'

"""
Testing a function: a failing test
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
add a new function to your test file. If the file grows too long, you can add as
many files as you need.
"""
# Testing middle names
from full_names_2 import get_full_name as get_full_name_2

def test_first_last():
    """Test names like Janis Joplin."""
    full_name = get_full_name_2('janis', 'joplin')
    assert full_name == 'Janis Joplin'

def test_middle():
    """Test names like David Lee Roth."""
    full_name = get_full_name_2('david', 'roth', 'lee')
    assert full_name == 'David Lee Roth'

"""
Testing a class
Testing a class is similar to testing a function, since you'll mostly be testing
its methods.
"""
# Building a test case
from accountant import Accountant

def test_initial_balance():
    """Default balance should be 0."""
    accountant = Accountant()
    assert accountant.balance == 0

def test_deposit():
    """Test a single deposit."""
    accountant = Accountant()
    accountant.deposit(100)
    assert accountant.balance == 100

"""
Using fixtures
A fixture is a resource that's used in multiple tests. When the name of a
fixture function is used as an argument to a test function, the return value of
the fixture is passed to the test function. When testing a class, you often have
to make an instance of the class. Fixtures let you work with just one instance.
"""
import pytest
from accountant import Accountant as Acc2

@pytest.fixture
def accountant():
    accountant = Acc2()
    return accountant

def test_initial_balance_2(accountant):
    """Default balance should be 0."""
    assert accountant.balance == 0

def test_deposit_2(accountant):
    """Test a single deposit."""
    accountant.deposit(100)
    assert accountant.balance == 100

def test_withdrawal(accountant):
    """Test a deposit followed by withdrawal."""
    accountant.deposit(1_000)
    accountant.withdraw(100)
    assert accountant.balance == 900
