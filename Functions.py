# 1. Basic Function Definition
def greet():
    print("Hello, World!")

greet()  # Calling the function

# 2. Function with Parameters
def add(a, b):
    return a + b

print(add(5, 3))  # Outputs: 8

# 3. Function with Return Value
def multiply(x, y):
    return x * y

result = multiply(2, 4)
print(result)  # Outputs: 8

# 4. Function with Default Arguments
def power(number, exponent=2):
    return number ** exponent

print(power(3))  # Outputs: 9 (since exponent defaults to 2)
print(power(3, 3))  # Outputs: 27

# 5. Variable Scope
def scope_test():
    function_scope_variable = "I am local to scope_test."
    print(function_scope_variable)

scope_test()
# print(function_scope_variable)  # This would raise an error because the variable is not accessible outside the function.

# 6. Recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # Outputs: 120

# 7. Lambda Functions
square = lambda x: x * x
print(square(5))  # Outputs: 25

# Explanation:
# 1. `greet` function demonstrates the simplest form of a function.
# 2. `add` function shows how to pass parameters and return a result.
# 3. `multiply` function is another example of parameters and return values.
# 4. `power` function introduces default arguments, making them optional.
# 5. `scope_test` demonstrates the local scope of variables within functions.
# 6. `factorial` function shows how to implement recursion for calculating factorial.
# 7. `square` lambda function shows a concise way to define simple functions.