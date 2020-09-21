'''
7 kyu
Mumbling
Link - https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
'''

######################
# Aman's Approach #
######################

def accum(s):
    
    s_upd = list(enumerate(s, start=1))
    return "-".join(list(map(lambda x: (x[0] * x[1]).capitalize(), s_upd)))
    
    
######################
# Shubham's Approach #
######################
