import turtle

def draw_square(t, l):
    """Make turtle t draw a square of side l"""
    for i in range(4):
        t.forward(l)
        t.left(90)

        
wn = turtle.Screen()
syrup = turtle.Turtle()
wn.bgcolor("lightblue")
wn.title("Questao 1")
for i in range(5):
    draw_square(syrup, 20*(i))
    syrup.penup()
    syrup.goto([-10*i, -10*i])
    syrup.pendown()


wn.mainloop()