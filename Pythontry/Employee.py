import unittest

class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, raise_amount=5000):
        self.salary += raise_amount

class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("John", "Doe", 50000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 55000)

    def test_give_custom_raise(self):
        self.employee.give_raise(10000)#变化了然后存储
        self.assertEqual(self.employee.salary, 60000)

if __name__ == '__main__':
    unittest.main()
