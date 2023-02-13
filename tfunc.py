from turtle import *
bgcolor('red')
def polygon(side,dist):
    pencolor('blue')
    for i in range(side):
        fd(dist)
        lt(360/side)
for i in range(3,11):
    polygon(i,100)

hideturtle()        #arrow gayab krne k liye
mainloop()