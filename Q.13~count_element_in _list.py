# create a code to count the occuernces of each element in a list and return a dictonary
 #with element as keys and their counts as values.

from collections import Counter
def count_element(lst):
    return dict (Counter (lst))


lst = ['apple','banana','apple','orange','banana','banana']
print(count_element(lst))