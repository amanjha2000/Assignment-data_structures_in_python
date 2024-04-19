# develop a code that takes a tuple of integers as input.
# The function should return the maximumand minimum values from the tuple using tuple  unpacking.

def min_max_tuple(input_tuple):
    min_value = min(*input_tuple)
    max_value = max(*input_tuple)
    return min_value , max_value

number = (4,2,9,8,5,3,1)
print(min_max_tuple(number))