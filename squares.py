import turtle               # import the turtle module 
import math                 # import the math module

screen = turtle.Screen()    # open a turtle screen 
screen.bgcolor("yellow")    # set screen's background color

ted = turtle.Turtle()       # create a turtle; call it ted

sideLength = 300            #set length of first square's side to 300
squares_num= int(input("How many squares would you like me to draw? "))
truth = True 
while truth:
     if squares_num > 0:
          truth = False
     else:
          print("Invalid Input. Please Try Again.")
          squares_num= int(input("How many squares would you like me to draw? "))

for i in range(squares_num):
     for i in range(4):              # draw a square: do the following 4 times
          ted.forward(sideLength)    # draw a line 150 pixels long
          ted.left(90)               # turn left to be ready for next line
     ted.forward(sideLength/2)
     sideLength = sideLength/math.sqrt(2)
     ted.left(45)

screen.exitonclick()        # close screen when user clicks on it