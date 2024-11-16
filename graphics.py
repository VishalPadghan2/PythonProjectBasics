import turtle as r
import colorsys as sm
r.tracer(2)
r.bgcolor("lightblue")
r.pensize(10)
n=10
h=0
for i in range(5):
    for i in range(2):
        c=sm.hsv_to_rgb(h,1,1)
        h+=1/n
        r.color(c)
        r.circle(49+i*5,90)
        r.forward(10)
        r.left(20)
    r.right(10)
r.done()

