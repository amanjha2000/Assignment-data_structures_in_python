# Write a code that takes two tuples input and returns new tuple containing elements that are 
# common to both input tuples.

def find_common_elements(tuple1,tuple2):
    set1 = set(tuple1)
    set2 = set(tuple2)
    common_elements = set1.intersection(set2)
    return tuple(common_elements)

tuple_a = (1,2,3,4,5)
tuple_b = (4,5,6,7,8)
print(find_common_elements(tuple_a,tuple_b))