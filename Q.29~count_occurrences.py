# write a code thst takes a tupule and an element as input. 
# The function should return the count of occurrences of the given element in the tuple.

def count_occurrence(input_tuple,element):
    count = input_tuple.count(element)
    return count


numbers = (1,2,3,2,4,2,5)
print(count_occurrence(numbers,2))