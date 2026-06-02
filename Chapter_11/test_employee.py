# 11.3.1 Test employee
import pytest
from employee import Employee


@pytest.fixture

def employee():
    return Employee('Lisa', 'Lurig', 50000)

def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.salary == 55000


def test_give_custom_raise(employee):
    employee.give_raise(10000)
    assert employee.salary == 60000
    
    
    
    
 