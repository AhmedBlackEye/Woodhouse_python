import turtle

def draw_petal(t):
    for i in range(10):
        t.forward(100)
        t.right(60)
        t.forward(100)
        t.right(120)
        t.forward(100)
        t.right(60)
        t.forward(100)
        t.right(12)
def run():
    s = turtle.getscreen()
    t = turtle.Turtle()
    turtle.bgcolor('#549ef2')
    turtle.title("Summer HW")
    t.shape("circle")
    t.pen(pensize=3, speed=4)
    draw_petal(t)

if __name__ == "__main__":
    run()