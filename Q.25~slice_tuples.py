# create a code that takes a tuple . and two integers as input. the function should return a new
# tuple containing elements from the original tuple whithin the specified range of indices.

def slice_tuple(original_tuple, start_index, end_index):

    new_tuple = original_tuple[start_index:end_index]   
    return new_tuple


original_tuple = ('a', 'b', 'c', 'd', 'e', 'f')
start_index = 2
end_index = 5

print(slice_tuple(original_tuple, start_index, end_index))  
