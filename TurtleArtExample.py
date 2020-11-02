import turtle
from TurtleShapes import *
import random as r
turtle.colormode(255)
turtle.ht()


    

turtle.title("Create a rectangle")
choice = turtle.textinput("Pick a Shape:", "Pick a shape to build:")

if choice == "rec":
    while True:
        length = r.randint(50,200)
        width = r.randint(50,200)
        draw_rectangle(length, width)
elif choice == "leaf":
    #while True:
        draw_leaf(1)
        

        
        
    
else:
    turtle.title("No you broke it")
    turtle.done()
