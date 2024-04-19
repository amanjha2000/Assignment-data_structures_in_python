# write a code to perform basic string compression using the count of repeted characters.

def compress_string(s):
    count = 1
    result = ""
    result += s[0]
    for i in range(len(s)-1):
        if(s[i] == s[i+1]):
            count+=1
        else:
            if(count > 1):
                result += str(count)
            result += s[i+1]
            count = 1
    if(count > 1):
        result += str(count)
    return result


s = 'aaabbcccc'
print(compress_string(s))
