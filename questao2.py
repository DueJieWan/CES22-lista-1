import turtle


def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(360/n)




wn = turtle.Screen()
syrup = turtle.Turtle()
wn.bgcolor("lightblue")
wn.title("Questao 2")

draw_poly(syrup, 8, 50)

wn.mainloop()
