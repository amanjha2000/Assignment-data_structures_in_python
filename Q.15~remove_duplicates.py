# implement a code to find and remove duplicates from a list while preserving the original order of element.

def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

my_list = [1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 8, 8, 9, 9]
print(remove_duplicates(my_list))
