# write a code that takes a list of words as input and returns a dictionary 
# where the keys are unique words and the values are the frequencies of those words in the input list.

def word_frequencies(word_list):
    
    word_freq = {}

    
    for word in word_list:
        
        if word in word_freq:
            word_freq[word] += 1
        
        else:
            word_freq[word] = 1

    
    return word_freq


words = ["apple", "banana", "apple", "cherry", "banana", "cherry", "cherry"]
print(word_frequencies(words))
