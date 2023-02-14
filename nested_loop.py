from turtle import *


pencolor('purple')
fillcolor('yellow')
pensize(5)


side=10

for i in range(side):
    fd(100)
    begin_fill()
    for i in range(side):
        fd(75)
        for i in range(side):
            fd(25)
            lt(360/side)
            dot(3)
        lt(360/side)     
    end_fill()
    rt(360/side)

hideturtle()
mainloop()