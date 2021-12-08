#import
import pygame as pg
import random
import emoji
#initialization
pg.init()
l=1000
w=800
#creating windows
size=(l,w)
windows=pg.display.set_mode(size)
pg.display.set_caption('Snake')

#setting boxes of size 100x100
column=100
row=80
#define a class to position or locate the snake's head and body
class place:
    row=0
    column=0
    def __init__(self,row,column):
        self.row=row
        self.column=column 
    #creating snake's body by copying the column and rows
    def replace(self):
        return place(row=self.row,column=self.column)
    
#setting the size of the windows or the boxes within, the food is a box and the snake consists of different adjacent boxes
def rect(place,color):
    adjl=l/column
    adjw=w/row
    left=place.column*adjl
    up=place.row*adjw

    pg.draw.rect(windows,color,(left,up,adjl,adjw))
pass
#generate the head and the body in the center of the window
head=place(row=int(row/2),column=int(column/2))
head_Color=(0,255,255)
snakes=[
    place(row=head.row,column=head.column+1),
    place(row=head.row,column=head.column+2),
    place(row=head.row,column=head.column+3)
]
#refresh food and prevent it from overlapping with snake's body and head
def new_food():
    while 1:
        pos=place(row=random.randint(0,row-1),column=random.randint(0,column-1))
        is_coll=False
        #head overlap
        if head.row==pos.row and head.column==pos.column:
            is_coll=True
        for snake in snakes:
            if snake.row==pos.row and snake.column==pos.column:
                is_coll=True
                break
        if not is_coll:
            break

    return pos


food=new_food()
food_color=(0,255,255)

#body before movement


#intiial direction of the snake, set to left
direct='left'


#Loop, set time, end loop
quit=True
time=pg.time.Clock()
while quit:
#events
    for event in pg.event.get():
        
        if event.type==pg.QUIT:
            quit=False
        elif event.type==pg.KEYDOWN:
            #track movement key to indicate the direction
            print(event)
            #use arrows and the classice WASD to indicate directions for the snake
            if event.key==1073741906 or event.key==119:
                if direct=='left' or direct=='right':
                    direct='up'
            elif event.key==1073741905 or event.key==115:
                if direct=='left' or direct=='right':
                    direct='down'
            elif event.key==1073741904 or event.key==97:
                if direct=='up' or direct=='down':
                    direct='left'
            elif event.key==1073741903 or event.key==100:
                if direct=='up' or direct=='down':
                    direct='right'
    
    #Consumption: if head and food overlap
    eat=(food.row==head.row and food.column==head.column)

    #refresh food same code from above, randomly generate
    if eat:
        food=new_food()

    #snake body, old head added to body as it moves
    #new head created, old tail deleted as it moves
    snakes.insert(0,head.replace())
#delete tail if it did not eat
    if not eat:
        snakes.pop()                
#direction
    if direct=='left':
        head.column=head.column-1
    elif direct=='right':
        head.column=head.column+1
    elif direct=='up':
        head.row=head.row-1
    elif direct=='down':
        head.row=head.row+1

    #wall
    death=False
    if head.column<0 or head.row<=0 or head.column>=column or head.row>=row:
        death=True
    #self
    for snake in snakes:
        if head.column==snake.column and head.row==snake.row:
            death=True
            break
    if death:
        print("Dead")
        quit=False
#graph/frame
    pg.draw.rect(windows,(255,255,255),(0,0,l,w))

#head
    for snake in snakes:
        rect(snake,(128,128,128))
    rect(head,head_Color)
    rect(food,food_color)



#basic graph/shape as squares begin with square boxes as food and snake's head&body    
    pg.display.flip()
#fps
    time.tick(20)
    

