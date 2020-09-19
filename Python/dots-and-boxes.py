'''
5 kyu
Dots and Boxes Validator
Link: https://www.codewars.com/kata/5d81d8571c6411001a40ba66
'''

######################
# Shubham's Approach #
######################

moves = {}
def getBoardSize(ar):
    return int((max(list(zip(*ar))[0]+list(zip(*ar))[1])+1)**0.5)

def createBoard(ar):
    n = getBoardSize(ar)
    return [[(i*n +j) for j in range(n)] for i in range(n)]       

def isHorizontalLine(move):
    return abs(move[0]-move[1]) == 1

def isTopEdge(move, board, n):
    return isHorizontalLine(move) and move[0] in board[0]

def isBottomEdge(move, board, n):
    return isHorizontalLine(move) and move[0] in board[-1]

def isVerticalLine(move):
    return not isHorizontalLine(move)

def isLeftEdge(move, board, n):
    return isVerticalLine(move) and move[0] in [board[i][0] for i in range(n)]

def isRightEdge(move, board, n):
    return isVerticalLine(move) and move[0] in [board[i][-1] for i in range(n)]

def getAdjacentPoints(move, board, n):
    if isHorizontalLine(move):
        if not isTopEdge(move, board, n) and not isBottomEdge(move, board, n):
            topPoints = [move[0]-n, move[1]-n] + list(move)
            bottomPoints = [move[0]+n, move[1]+n] + list(move)
            return topPoints, bottomPoints
        if isTopEdge(move, board, n):
            bottomPoints = [move[0]+n, move[1]+n] + list(move)
            return bottomPoints, None
        if isBottomEdge(move, board, n):
            topPoints = [move[0]-n, move[1]-n] + list(move)
            return topPoints, None
    if isVerticalLine(move):
        if not isLeftEdge(move, board, n) and not isRightEdge(move, board, n):
            leftPoints = [move[0]-1, move[1]-1] + list(move)
            rightPoints = [move[0]+1, move[1]+1] + list(move)
            return leftPoints, rightPoints
        if isLeftEdge(move, board, n):
            rightPoints = [move[0]+1, move[1]+1] + list(move)
            return rightPoints, None
        if isRightEdge(move, board, n):
            leftPoints = [move[0]-1, move[1]-1] + list(move)
            return leftPoints, None

def addWinningScore(move, board, n):
    adPts1, adPts2 = getAdjacentPoints(move, board, n)
    #print(getAdjacentPoints(move, board, n))
    sq1 = 0
    sq2 = 0
    if adPts1:
        sq1 = 1 if all([
            moves.get((adPts1[0], adPts1[1])),
            moves.get((adPts1[1], adPts1[3])),
            moves.get((adPts1[3], adPts1[2])),
            moves.get((adPts1[2], adPts1[0])),
        ]) else 0
    if adPts2:
        sq2 = 1 if all([
            moves.get((adPts2[0], adPts2[1])),
            moves.get((adPts2[1], adPts2[3])),
            moves.get((adPts2[3], adPts2[2])),
            moves.get((adPts2[2], adPts2[0])),
        ]) else 0
    return sq1 + sq2

def dots_and_boxes(ar):
    n = getBoardSize(ar)
    board = createBoard(ar)
    score = [0,0]
    turn = 0
    
    for move in ar:
        moves[move] = False
        moves[tuple(reversed(move))] = False
        
    for move in ar:
        moves[move] = True
        moves[tuple(reversed(move))] = True
        addScore = addWinningScore(move, board, n)
        
        if addScore:
            score[turn] += addScore
        else:
            turn = 1 - turn
    
    return tuple(score)
