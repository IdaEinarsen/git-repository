# 11.3 Employee

# A template for employee's 

class Employee:
      def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

# Added behavior 

      def give_raise(self, amount=5000):
        self.salary += amount
