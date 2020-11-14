import turtle
import math

#screen and pen settings
turtle.bgcolor("#fcdf74")
turtle.pencolor("#8D65D8")
turtle.fillcolor("#5D24C8")
turtle.pensize(5)
turtle.title('Word Turtle Program')
turtle.penup()
turtle.hideturtle()

#input
text = (turtle.textinput("Turtle.Word", "Введите слово:")).lower()
text_counter = len(text)

#screen size and start position
width = 100 * 2 + text_counter * 70 + (text_counter - 1) * 20
height = 300
turtle.setup(width=width,height=height,startx=0,starty=0)
turtle.goto(((-text_counter)/2) * 70, 0)

#start programm 
for i in range(text_counter):
    if text[i] == 'a':
        turtle.goto(0, -50)
        cx = turtle.xcor()
        cy = turtle.ycor()
        turtle.pendown()
        #drawing
        x = math.degrees(math.atan(25/100))
        turtle.rt(x - 90)
        turtle.forward(math.sqrt(10625))
        turtle.right(90 - x)
        turtle.forward(20)
        turtle.right(90 - x)
        turtle.forward(math.sqrt(10625))
        turtle.right(90 + x)
        turtle.forward(15)
        turtle.right(90 - x)
        turtle.forward(25)
        turtle.left(90 - x)
        turtle.forward(26.5)
        turtle.left(90 - x)
        turtle.forward(25)
        turtle.right(90 - x)
        turtle.forward(15)
        turtle.penup()
        turtle.right(180)
        turtle.forward(15)
        turtle.left(90 - x)
        turtle.forward(40)
        turtle.pendown()
        turtle.forward(38)
        turtle.right(180 - 2 * x)
        turtle.forward(38)
        turtle.right(90 + x)
        turtle.forward(16)
        #end drawing
        turtle.penup()
        turtle.setpos(cx, cy)
        turtle.right(180)
        if i < text_counter - 1:
            turtle.goto(90, 0)
    if text[i] == 'b':
        turtle.pendown()
        turtle.left(90)
        turtle.forward(50)
#does not exit while not click
turtle.exitonclick()