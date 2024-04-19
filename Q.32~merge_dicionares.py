# write a code that takes two dictionaries as input and merges them into asingle dictionary. 
# If there are common keys,the values should be added together.

def merge_dictionaries(dict1, dict2):
    
    merged_dict = {}

    
    for key, value in dict1.items():
        merged_dict[key] = value

    
    for key, value in dict2.items():
        if key in merged_dict:
            
            merged_dict[key] += value
        else:
            
            merged_dict[key] = value

    
    return merged_dict


dict1 = {"apple": 5, "banana": 3, "cherry": 2}
dict2 = {"banana": 2, "cherry": 3, "date": 4}
print(merge_dictionaries(dict1, dict2))
