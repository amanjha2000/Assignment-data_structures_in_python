# write a code to remove all occurences of a specific element from a list.

def remove_element(lst,element):
    return [i for i in lst if i != element]
print(remove_element([1,2,3,4,2,5],2))

