from turtle import *
speed(100)
screensize(1000, 1000)
pendown()
for i in range(20,-20):
    goto(i,0)
    print(i,0)
for i in range(20,-20):
    goto(0,i)
for y in range(10, -15, -1):
    if y != -2 or y != -3:
        x  =(((y ** 2) + (y*4)/2)-1)/4
penup()
done()
