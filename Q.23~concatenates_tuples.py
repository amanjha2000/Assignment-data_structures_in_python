# write a code to concatenates two tuples. the functions should take two tuples as input and return 
# a new tuple containing element from both input tuples.

def concatenates_tuples(tuple1,tuple2):
    return tuple1 + tuple2
tuple_a = (1,2,3)
tuple_b = (4,5,6)
result = concatenates_tuples(tuple_a,tuple_b)

print(result)