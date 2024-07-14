class MathHelper:
    # Class variable
    pi = 3.14159

    def __init__(self, value):
        self.value = value

    def square(self):
        return self.value * self.value

    @classmethod
    def circle_area(cls, radius):
        return cls.pi * radius * radius

    @staticmethod
    def sqrt(number):
        return number ** 0.5

# Creating an instance of MathHelper
helper = MathHelper(10)

# Accessing the object's attribute
print(helper.value)

# Modifying the object's attribute
helper.value = 20
print(helper.value)

# Using an instance method
print(helper.square())

# Using a class method
print(MathHelper.circle_area(5))

# Using a static method
print(MathHelper.sqrt(16))