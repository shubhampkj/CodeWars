'''
6 kyu
Find the missing letter
Link - https://www.codewars.com/kata/5839edaa6754d6fec10000a2
'''

######################
# Aman's Approach #
######################

def find_missing_letter(chars):
    str = ""
    for i in range(len(chars) - 1):
        if abs(ord(chars[i]) - ord(chars[i+1])) != 1:
            str += chr(ord(chars[i]) + 1)
    
    return str
    

######################
# Shubham's Approach #
######################

