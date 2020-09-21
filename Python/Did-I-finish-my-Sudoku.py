'''
5 kyu
Did I Finish my Sudoku?
https://www.codewars.com/kata/53db96041f1a7d32dc0004d2
'''

######################
# Aman's Approach #
######################

def done_or_not(board): #board[i][j]
    
    vert = list(zip(*board))
    temp_list = [[] for c in range(9)]
    
    for i in range(len(board)):
        
        for j in board[i]:
            if board[i].count(j) > 1 or list(vert[i]).count(j) > 1:
                return "Try again!"
        
        var = 0
        for k in range(0,3):
            if i in range(0, 3):
                temp_list[k].extend(board[i][var:var+3])
                var += 3
            
            elif i in range(3, 6):
                temp_list[k+3].extend(board[i][var:var+3])
                var += 3
                
            else:
                temp_list[k+6].extend(board[i][var:var+3])
                var += 3
                
    for x in temp_list:
        
        if len(set(x)) < 9:
            return 'Try again!'
        
    else:
        return 'Finished!'


######################
# Shubham's Approach #
######################
