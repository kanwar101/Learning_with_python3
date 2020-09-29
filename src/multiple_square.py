import turtle

def draw_multiple_squares(t,sz):
    """Draw multiple squares"""
    for i in ['red', 'blue','green', 'orange']:
        t.color(i)
        t.forward(sz)
        t.right(90)


wn = turtle.Screen()
wn.bgcolor("yellow")
wn.title("Multiple Squares")

tess = turtle.Turtle()
tess.pensize(5)
size = 20

for i in range(15):
    draw_multiple_squares(tess, size)
    size += 5
    tess.forward(30)
    tess.right(20)


wn.mainloop()
