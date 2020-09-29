import turtle

def draw_square(t, sz):
    """function to draw square"""
    for i in range(4):
        t.forward(sz)
        t.right(90)

wn = turtle.Screen()
wn.bgcolor("yellow")
wn.title("Alex the Turtle")

alex = turtle.Turtle()
draw_square(alex, 100)

wn.mainloop()