'''
4 kyu
Snail sort
Link - https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
'''

######################
# Aman's Approach #
######################

def snail(snail_map):
    
    temp_list = []
    while len(snail_map) > 0:
        
        temp_list += snail_map[0]
        del snail_map[0]

        if len(snail_map) > 0:
            
            for i in snail_map:
                temp_list += [i[-1]]
                del i[-1]

            
            if snail_map[-1]:
                temp_list += snail_map[-1][::-1]
                del snail_map[-1]

        
            for i in reversed(snail_map):
                temp_list += [i[0]]
                del i[0]

    return temp_list



######################
# Shubham's Approach #
######################
