import turtle as tu
import random as ra
import tkinter as tk
import math

def Meteors():
    tu.setup(1.0, 1.0)
    tu.screensize(1.0, 1.0)
    tu.bgcolor('black')
    tu.title("Meteors")

    t = tu.Pen()
    t.hideturtle()

    colors = ['pink', 'lightpink', 'deeppink']
    
    class Star():
        def __init__(self):
            self.r = ra.randint(50, 100)
            self.t = ra.randint(1,3)
            self.x = ra.randint(-2000, 1000)
            self.y = ra.randint(444, 999)
            self.speed = ra.randint(5,10)
            self.color = ra.choice(colors)
            self.outline = 1
        
        def star(self):
            t.pensize(self.outline)
            t.penup()
            t.goto(self.x, self.y)
            t.pendown()
            t.color(self.color)
            t.begin_fill()
            t.fillcolor(self.color)
            t.setheading(-30)
            t.right(self.t)
            t.forward(self.r)
            t.left(self.t)
            t.circle(self.r * math.sin(math.radians(self.t)), 180)
            t.left(self.t)
            t.forward(self.r)
            t.end_fill()
        
        def move(self):
            if self.y >= -500:
                self.y -= self.speed
                self.x += 2*self.speed
            else:
                self.r = ra.randint(50, 100)
                self.t = ra.randint(1,3)
                self.x = ra.randint(-2000, 1000)
                self.y = 444
                self.speed = ra.randint(5,10)
                self.color = ra.choice(colors)
                self.outline = 1
    
    Stars = []
    for i in range(100):
        Stars.append(Star())

    while True:
        tu.tracer(0)
        t.clear()
        for i in range(100):
            Stars[i].move()
            Stars[i].star()
        tu.update()
    tu.mainloop()


if __name__ == "__main__":
    Meteors()
