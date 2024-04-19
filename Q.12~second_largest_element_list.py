# implement a code to find the second largest number in a given list of interger.

def second_largest(lst):
    lst = list (set(lst))
    if len(lst) < 2:
        return None
    lst.sort()
    return lst[-2]
print(second_largest([1,2,3,4,5]))
print(second_largest([5,5,5,5,5]))