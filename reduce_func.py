from functools import reduce


# function that takes two values and return sum of it
def add_values(first_value, second_value):
    return first_value + second_value


numbers = [1, 2, 3, 4, 5]

""" reduce - It is used to perform a specific operation on a sequence of elements. 
           - It takes two arguments: the function to apply and the iterable"""
result = reduce(add_values, numbers)
print(result)
