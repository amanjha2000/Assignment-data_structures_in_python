# write a code to shuffle a give list randomaly whithout using any built-in shuffle function.

import random
def shuffle_list(input_list):
    for i in range (len(input_list)-1,0,-1):
        j = random.randint(0,i)
        input_list[i], input_list[j] = input_list[j],input_list[i]
        return input_list

number = [1,2,3,4,5]
print(shuffle_list(number))