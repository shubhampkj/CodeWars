'''
5 kyu
Dots and Boxes Validator
Link: https://www.codewars.com/kata/5d81d8571c6411001a40ba66
'''

######################
# Aman's Approach #
######################

import math
import copy


def hori_moves(ndim: 'int') -> 'list':
    
    temp = []
    for x in range(0, ndim ** 2, ndim):
        board = [i for i in range(x, x + ndim)]
        h_move = list(enumerate(board, start=x+1))
        h_move = [tuple(reversed(j)) for j in h_move]
        temp.extend(h_move[:-1])
        
    return temp


def box(h_moves: 'list', ndim: 'int') -> 'list':
    
    h_moves.sort()
    temp = []
    for i in h_moves:
        temp.append([i, (i[0], i[0] + ndim), (i[1], i[1]+ndim), (i[0] + ndim, i[1] + ndim)])
    
    no_of_boxes = (ndim * (ndim-2)) + 1   
    return temp[:no_of_boxes]
  

def player_change(p):
    return 'P2' if p == 'P1' else 'P1'
    
    
def dots_and_boxes(ar):
    
    players = {'P1' : 0, 'P2':0}
    p = 'P1'
    board_size = list(zip(*ar))[0] + list(zip(*ar))[1]
    max_num = max(board_size)
    ndim = math.sqrt(max_num + 1)
    h_moves = hori_moves(int(ndim))
    tot_box = box(h_moves, int(ndim))
    
    for i in ar:
        c = 0
        sorted_i = tuple(sorted(i))
        for j in tot_box:
            if sorted_i in j:
                j.remove(sorted_i)
            
            if j == []:
                players[p] += 1
                j.append('empty')
                c += 1
        
        if c >= 1:
            pass
        else:
            p = player_change(p)
        
    return (players['P1'], players['P2'])



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
