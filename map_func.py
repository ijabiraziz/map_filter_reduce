# take a digit and return square of it.
def square(digit) -> int:
    return digit * 2


numbers = [1, 2, 3, 4, 5]
# print(numbers)
""" map - A built-in function that takes a function and itrables as arguments,
        - And applies specific function to each of the iterable values """
squared_numbers = map(square, numbers)

result = list(squared_numbers)
print(result)


# The above task can be more concise and more efficient, i.e,
add_two_1 = map(lambda x: x + 2, [1, 2, 3, 4, 5])

result_1 = list(add_two_1)
print(result_1)
