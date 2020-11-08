# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 17:45:58 2020

@author: radwa
"""

red='#eb4b33'
blue='#1d364c'
yellow='#ecc307'
white='#fefcfc'
from tkinter import *
from tkinter.font import Font
import time

board = [' ' for x in range(10)]
score_cpu=0
score_player=0
def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
    

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


root=Tk()
root.title('Tic Tac Toe')
root.iconphoto(True, PhotoImage(file="tic-tac-toe.png"))
root.geometry('600x500')
canvas = Canvas(root, width=600, height=500,bg='#eb4b33')
def draw_canvas ():
	
	canvas.pack()

	bg=canvas.create_rectangle(0, 0, 600, 500, fill=red)
	v1 = canvas.create_rectangle(190, 20, 210, 480, fill=blue)
	v2 = canvas.create_rectangle(390, 20, 410, 480, fill=blue)
	h1 = canvas.create_rectangle(50, 160, 550, 180, fill=blue)
	h2 = canvas.create_rectangle(50, 320, 550, 340, fill=blue)
	myFont = Font(family="Verdana", weight = 'bold', size=40)
	
	score_p=canvas.create_text(50,450,text=str(score_player),font=myFont, fill=yellow)
	score_c=canvas.create_text(550,450,text=str(score_cpu),font=myFont, fill=white)


draw_canvas ()

def get_pos(eventorigin):
      global x,y
      x = eventorigin.x
      y = eventorigin.y
      comp=False
      player_w=False
      cpu_w=False
      if x<190 and y<160:
      	pos=1
      elif 210<x<390 and y<160:
      	pos=2
      elif 410<x and y<160:
      	pos=3
      elif x<190 and 180<y<320:
      	pos=4
      elif 210<x<390 and 180<y<320:
      	pos=5
      elif 410<x and 180<y<320:
      	pos=6
      elif x<190 and 340<y:
      	pos=7
      elif 210<x<390 and 340<y:
      	pos=8
      elif 410<x and 340<y:
      	pos=9
      else:
      	pos=0
      
      


      
      	      	  

      if isWinner(board,'X'):
      	        	  
      	  player_w=True      	  
      	  
      elif isWinner(board,'O'):
      	        	  
      	  cpu_w=True
      	  
      if spaceIsFree(pos) and cpu_w==False and player_w==False :
      	  insertLetter('X',pos)
      	  draw_x_o(pos,'x')
      	  comp=True

      if isWinner(board,'X'):
      	       	  
      	  player_w=True      	  
      	  
      elif isWinner(board,'O'):
      	        	  
      	  cpu_w=True
      if comp and player_w == False and pos!=0:      	  	  
      	  move = compMove()
      	  insertLetter('O',move)
      	  draw_x_o(move,'o')      	  
      	  comp=False
      
      if isBoardFull(board):
      	  
      	  out=canvas.create_text(300,470,text="Tie game, right click to restart !",font=myFont1, fill=white)      	       	  

      elif isWinner(board,'X'):
      	  
      	  draw_lines() 
      	  global score_player
      	  score_player+=1     	  
      	  player_w=True     	  
      	        	  
      elif isWinner(board,'O'):
      	   
      	  draw_lines()
      	  global score_cpu
      	  score_cpu+=1     	  
      	  cpu_w=True

      	  


      
      	  	
      
def get_won_pos(bo, le):
	if (bo[7] == le and bo[8] == le and bo[9] == le):
		return 3
	elif (bo[4] == le and bo[5] == le and bo[6] == le):
		return 2
	elif (bo[1] == le and bo[2] == le and bo[3] == le):
		return 1
	elif (bo[1] == le and bo[4] == le and bo[7] == le):
		return 4
	elif (bo[2] == le and bo[5] == le and bo[8] == le):
		return 5
	elif (bo[3] == le and bo[6] == le and bo[9] == le):
		return 6
	elif (bo[1] == le and bo[5] == le and bo[9] == le):
		return 7
	elif (bo[3] == le and bo[5] == le and bo[7] == le):
		return 8

myFont1 = Font(family="Verdana", weight = 'bold', size=15)			
def draw_lines():
	for let in ['X','O']:
		won_pos = get_won_pos(board,let)
		if won_pos==1:
			l=canvas.create_rectangle(50,80,550,85, fill='black')
			out=canvas.create_text(300,470,text="Right click to restart !",font=myFont1, fill=white)
		elif won_pos==2:
			l=canvas.create_rectangle(50,240,550,245, fill='black')	
			out=canvas.create_text(300,470,text="Right click to restart !",font=myFont1, fill=white)
		elif won_pos==3:
			l=canvas.create_rectangle(50,400,550,405, fill='black')
			out=canvas.create_text(300,470,text="Right click to restart !",font=myFont1, fill=white)
		elif won_pos==4:
			l=canvas.create_rectangle(120,20,125,480, fill='black')
			out=canvas.create_text(300,470,text="Right click to restart !",font=myFont1, fill=white)
		elif won_pos==5:
			l=canvas.create_rectangle(360,20,365,480, fill='black')
			out=canvas.create_text(300,470,text="Right click to restart !",font=myFont1, fill=white)
		elif won_pos==6:
			l=canvas.create_rectangle(480,20,485,480, fill='black')
			out=canvas.create_text(300,470,text="Right click to restart !",font=myFont1, fill=white)
		elif won_pos==7:
			l=canvas.create_polygon(50,20,55,20,550,480,545,480, fill='black')
			out=canvas.create_text(300,470,text="Right click to restart !",font=myFont1, fill=white)
		elif won_pos==8:
			l=canvas.create_polygon(545,20,550,20,55,480,50,480, fill='black')
			out=canvas.create_text(300,470,text="Right click to restart !",font=myFont1, fill=white)






def draw_x_o (pos,letter):	
	if pos==0 :
		pass
	if pos==1 and letter=='x':
		tl_x=[80,50]
		x1=canvas.create_polygon(tl_x[0],tl_x[1],tl_x[0]+20,tl_x[1],tl_x[0]+80,tl_x[1]+80,tl_x[0]+60,tl_x[1]+80,fill=yellow)
		x2=canvas.create_polygon(tl_x[0]+60,tl_x[1],tl_x[0]+80,tl_x[1]+0,tl_x[0]+20,tl_x[1]+80,tl_x[0],tl_x[1]+80,fill=yellow)
	if pos==1 and letter=='o':
		center_o=[120,90]
		o_out=canvas.create_oval(center_o[0]-40,center_o[1]-40,center_o[0]+40,center_o[1]+40,fill=white )
		o_in=canvas.create_oval(center_o[0]-25,center_o[1]-25,center_o[0]+25,center_o[1]+25,fill=red )

	if pos==2 and letter=='x':
		tl_x=[260,50]
		x1=canvas.create_polygon(tl_x[0],tl_x[1],tl_x[0]+20,tl_x[1],tl_x[0]+80,tl_x[1]+80,tl_x[0]+60,tl_x[1]+80,fill=yellow)
		x2=canvas.create_polygon(tl_x[0]+60,tl_x[1],tl_x[0]+80,tl_x[1]+0,tl_x[0]+20,tl_x[1]+80,tl_x[0],tl_x[1]+80,fill=yellow)
	if pos==2 and letter=='o':
		center_o=[300,90]
		o_out=canvas.create_oval(center_o[0]-40,center_o[1]-40,center_o[0]+40,center_o[1]+40,fill=white )
		o_in=canvas.create_oval(center_o[0]-25,center_o[1]-25,center_o[0]+25,center_o[1]+25,fill=red )

	if pos==3 and letter=='x':
		tl_x=[440,50]
		x1=canvas.create_polygon(tl_x[0],tl_x[1],tl_x[0]+20,tl_x[1],tl_x[0]+80,tl_x[1]+80,tl_x[0]+60,tl_x[1]+80,fill=yellow)
		x2=canvas.create_polygon(tl_x[0]+60,tl_x[1],tl_x[0]+80,tl_x[1]+0,tl_x[0]+20,tl_x[1]+80,tl_x[0],tl_x[1]+80,fill=yellow)
	if pos==3 and letter=='o':
		center_o=[480,90]
		o_out=canvas.create_oval(center_o[0]-40,center_o[1]-40,center_o[0]+40,center_o[1]+40,fill=white )
		o_in=canvas.create_oval(center_o[0]-25,center_o[1]-25,center_o[0]+25,center_o[1]+25,fill=red )




	if pos==4 and letter=='x':
		tl_x=[80,210]
		x1=canvas.create_polygon(tl_x[0],tl_x[1],tl_x[0]+20,tl_x[1],tl_x[0]+80,tl_x[1]+80,tl_x[0]+60,tl_x[1]+80,fill=yellow)
		x2=canvas.create_polygon(tl_x[0]+60,tl_x[1],tl_x[0]+80,tl_x[1]+0,tl_x[0]+20,tl_x[1]+80,tl_x[0],tl_x[1]+80,fill=yellow)
	if pos==4 and letter=='o':
		center_o=[120,250]
		o_out=canvas.create_oval(center_o[0]-40,center_o[1]-40,center_o[0]+40,center_o[1]+40,fill=white )
		o_in=canvas.create_oval(center_o[0]-25,center_o[1]-25,center_o[0]+25,center_o[1]+25,fill=red )

	if pos==5 and letter=='x':
		tl_x=[260,210]
		x1=canvas.create_polygon(tl_x[0],tl_x[1],tl_x[0]+20,tl_x[1],tl_x[0]+80,tl_x[1]+80,tl_x[0]+60,tl_x[1]+80,fill=yellow)
		x2=canvas.create_polygon(tl_x[0]+60,tl_x[1],tl_x[0]+80,tl_x[1]+0,tl_x[0]+20,tl_x[1]+80,tl_x[0],tl_x[1]+80,fill=yellow)
	if pos==5 and letter=='o':
		center_o=[300,250]
		o_out=canvas.create_oval(center_o[0]-40,center_o[1]-40,center_o[0]+40,center_o[1]+40,fill=white )
		o_in=canvas.create_oval(center_o[0]-25,center_o[1]-25,center_o[0]+25,center_o[1]+25,fill=red )

	if pos==6 and letter=='x':
		tl_x=[440,210]
		x1=canvas.create_polygon(tl_x[0],tl_x[1],tl_x[0]+20,tl_x[1],tl_x[0]+80,tl_x[1]+80,tl_x[0]+60,tl_x[1]+80,fill=yellow)
		x2=canvas.create_polygon(tl_x[0]+60,tl_x[1],tl_x[0]+80,tl_x[1]+0,tl_x[0]+20,tl_x[1]+80,tl_x[0],tl_x[1]+80,fill=yellow)
	if pos==6 and letter=='o':
		center_o=[480,250]
		o_out=canvas.create_oval(center_o[0]-40,center_o[1]-40,center_o[0]+40,center_o[1]+40,fill=white )
		o_in=canvas.create_oval(center_o[0]-25,center_o[1]-25,center_o[0]+25,center_o[1]+25,fill=red )



	if pos==7 and letter=='x':
		tl_x=[80,370]
		x1=canvas.create_polygon(tl_x[0],tl_x[1],tl_x[0]+20,tl_x[1],tl_x[0]+80,tl_x[1]+80,tl_x[0]+60,tl_x[1]+80,fill=yellow)
		x2=canvas.create_polygon(tl_x[0]+60,tl_x[1],tl_x[0]+80,tl_x[1]+0,tl_x[0]+20,tl_x[1]+80,tl_x[0],tl_x[1]+80,fill=yellow)
	if pos==7 and letter=='o':
		center_o=[120,410]
		o_out=canvas.create_oval(center_o[0]-40,center_o[1]-40,center_o[0]+40,center_o[1]+40,fill=white )
		o_in=canvas.create_oval(center_o[0]-25,center_o[1]-25,center_o[0]+25,center_o[1]+25,fill=red )

	if pos==8 and letter=='x':
		tl_x=[260,370]
		x1=canvas.create_polygon(tl_x[0],tl_x[1],tl_x[0]+20,tl_x[1],tl_x[0]+80,tl_x[1]+80,tl_x[0]+60,tl_x[1]+80,fill=yellow)
		x2=canvas.create_polygon(tl_x[0]+60,tl_x[1],tl_x[0]+80,tl_x[1]+0,tl_x[0]+20,tl_x[1]+80,tl_x[0],tl_x[1]+80,fill=yellow)
	if pos==8 and letter=='o':
		center_o=[300,410]
		o_out=canvas.create_oval(center_o[0]-40,center_o[1]-40,center_o[0]+40,center_o[1]+40,fill=white )
		o_in=canvas.create_oval(center_o[0]-25,center_o[1]-25,center_o[0]+25,center_o[1]+25,fill=red )

	if pos==9 and letter=='x':
		tl_x=[440,370]
		x1=canvas.create_polygon(tl_x[0],tl_x[1],tl_x[0]+20,tl_x[1],tl_x[0]+80,tl_x[1]+80,tl_x[0]+60,tl_x[1]+80,fill=yellow)
		x2=canvas.create_polygon(tl_x[0]+60,tl_x[1],tl_x[0]+80,tl_x[1]+0,tl_x[0]+20,tl_x[1]+80,tl_x[0],tl_x[1]+80,fill=yellow)
	if pos==9 and letter=='o':
		center_o=[480,410]
		o_out=canvas.create_oval(center_o[0]-40,center_o[1]-40,center_o[0]+40,center_o[1]+40,fill=white )
		o_in=canvas.create_oval(center_o[0]-25,center_o[1]-25,center_o[0]+25,center_o[1]+25,fill=red )


def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
            
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
            
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        
    return move


def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le)
     or (bo[4] == le and bo[5] == le and bo[6] == le)
      or(bo[1] == le and bo[2] == le and bo[3] == le)
       or(bo[1] == le and bo[4] == le and bo[7] == le)
        or(bo[2] == le and bo[5] == le and bo[8] == le)
         or(bo[3] == le and bo[6] == le and bo[9] == le)
          or(bo[1] == le and bo[5] == le and bo[9] == le)
           or(bo[3] == le and bo[5] == le and bo[7] == le))

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def reset_game(eventorigin):
	global board
	board = [' ' for x in range(10)]
	draw_canvas()


root.bind("<Button 1>",get_pos)

root.bind("<Button 3>",reset_game)

root.mainloop()




