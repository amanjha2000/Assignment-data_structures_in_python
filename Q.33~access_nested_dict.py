# write a code to access avalue in nested dictionary.
# The function should take the dictionary and a list of keys as input, and return the corresponding value. 
#if any of the keys do not exist in the dictionary, the function should return none.

def access_nested_dict(nested_dict, keys):
    
    current_dict = nested_dict

    for key in keys:
        
        if key in current_dict:
            current_dict = current_dict[key]
        
        else:
            return None

    
    return current_dict


nested_dict = {"a": {"b": {"c": 1}}}
keys = ["a", "b", "c"]
print(access_nested_dict(nested_dict, keys))
