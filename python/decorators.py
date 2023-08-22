def double_result(func):
    def wrapper(x):
        result = func(x)
        return result * 2
    return wrapper

@double_result
def square(x):
    return x ** 2

@double_result
def cube(x):
    return x ** 3

print(square(5))  # Output: 50 (5^2 * 2)
print(cube(2))    # Output: 16 (2^3 * 2)
