'''
6 kyu
Solomon's Quest for the Temporal Crystal
Link - https://www.codewars.com/kata/59d7c910f703c460a2000034
'''

######################
# Aman's Approach #
######################

def solomons_quest(arr):
    x, y = 0, 0
    dilation = 0
    
    for li in arr:
        
        dilation += li[0]
        distance = li[2] * pow(2,dilation)
        
        if li [1] == 0:
            y += distance
        elif li[1] == 2:
            y -= distance
        elif li[1] == 1:
            x += distance
        else:
            x -= distance

    return [x,y]
    
    
######################
# Shubham's Approach #
######################
