#pgzero- to build a small game

import pgzrun

box= Rect((50,50),(150,100))     #(x,ycoordinates starting)(width,height)
box2=Rect((600,50),(100,100))
box3=Rect((300,100),(100,100))
box4=Rect((500,100),(150,100))
bvx=2
b2vx=-2
def draw():
    screen.fill('black')
    screen.draw.filled_rect(box,'yellow')
    screen.draw.filled_rect(box2,'purple')
    screen.draw.filled_rect(box3,'pink')
    screen.draw.filled_rect(box4,'green')

def update():
#    box.x+=2 #move box to the right
 #   box2.x-=2 #move box to left
    box3.y-=2
    box4.y+=2
    global bvx, b2vx
    box.x+=bvx
    box2.x+= b2vx
    if box.colliderect(box2):
            bvx= -bvx
            b2vx=-b2vx
            sounds.cling.play()
    if box.left<0:
            bvx=-bvx
            sounds.cling.play()
    if box2.right>800:
            b2vx=-b2vx
            sounds.cling.play()


pgzrun.go()