'''
5 kyu
Moving Zeros To The End
Link - https://www.codewars.com/kata/52597aa56021e91c93000cb0
'''

######################
# Aman's Approach #
######################

def move_zeros(array):
        
    temp_list = []
    count_of_zeros = array.count(0)
    for i in array:
        if i != 0 or i is False:
            temp_list.append(i)
    
    while len(temp_list) < len(array):
        temp_list.append(0)
        
    return temp_list


######################
# Shubham's Approach #
######################
