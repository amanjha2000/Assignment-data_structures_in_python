# write a code that takes a dictionary as input and returns a sorted version of based on the values. 
# You can choose whether to sort in ascending or descending order.

def sort_dict_by_values(input_dict):
    
    sorted_dict = dict(sorted(input_dict.items(), key=lambda item: item[1]))

    
    return sorted_dict


input_dict = {"apple": 5, "banana": 3, "cherry": 2}
print(sort_dict_by_values(input_dict))
