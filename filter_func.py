# function that checks if a value is even or odd
def is_even(value):
    if value % 2 == 0:
        return value


numbers = [1, 2, 3, 4, 5, 6, 7]
"""filter -  A built-in function that takes a function and iterable
          -  it filters some values based on that function condition"""
even_numbers = filter(is_even, numbers)

#convert filter object to list 
result = list(even_numbers)
print(result)



#Another way of doing above Code 
even_numbers_1 = filter(lambda value: value % 2 == 0, [10, 11, 12, 13, 14, 15, 16, 17, 18])

#convert filter object to list 
result_1 = list(even_numbers_1)
print(result_1)



