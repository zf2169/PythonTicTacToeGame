# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 02:51:31 2017

@author: qn_li
"""

###Tic Tac Toe Game
from IPython.display import clear_output
def display():
    '''
    display the whole game board
    '''
    clear_output()
    global board
    print(board[0]+' | '+board[1]+' | '+board[2])
    print('---------')
    print(board[3]+' | '+board[4]+' | '+board[5])
    print('---------')
    print(board[6]+' | '+board[7]+' | '+board[8])

def win():
    '''
    judge whether the situation on the game board shows the winner
    '''
    global board
    for i in range(0,7,3):
        if board[i]==board[i+1]==board[i+2]=='x' or board[i]==board[i+1]==board[i+2]=='o':
            return(True)
    for j in range(0,3):
        if board[j]==board[j+3]==board[j+6]=='x' or board[j]==board[j+1]==board[j+2]=='o':
            return(True)
    if board[0]==board[4]==board[8]=='x' or board[2]==board[4]==board[6]=='x':
        return(True)
    if board[0]==board[4]==board[8]=='o' or board[2]==board[4]==board[6]=='o':
        return(True)
    return(False)

def player(num):
    '''the process for one player choose the position and check the validity'''
    global board
    global s
    mark=['','x','o']
    while True:
        try:
            p=int(input('Player{} choose your position[1-9]:'.format(num)))-1
        except ValueError:
            print('Please input a number[1-9]')
            continue

        if p not in range(9):
            print('Please input a number[1-9]')
            continue
        
        # if the place is occupied, the player should choose another place
        if p in s:
            print('Choose another place!')
            continue
        else:
            board[p]=mark[num]
            break
    display()
    s.add(p)

def play():
    global board
    global s
    board= [" "]*9
    s=set([])
    while(True):
        player(1)
        if win():
            print('Player1 Wins!')
            break
    
        if len(s)==9:
            print('Tie!')
            break
    
        player(2)
        if win():
            print('Player2 Wins!')
            break
        
        if len(s)==9:
            print('Tie!')
            break
    # ask the player want to play once more
    another= (input('Do you want play once more? [y/n]:').lower())[0]
    # if the input is not y/n, do the input progress again
    while (another!='y' and another!='n'):
        another= (input('Do you want play once more? [y/n]:').lower())[0]
    if (another=='y'):
        play()
    else:
        return('Thank you for playing the game!')

play()

