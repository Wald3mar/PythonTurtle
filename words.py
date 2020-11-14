import turtle

turtle.title('Word Turtle Program')
text = input().lower()
text_counter = len(text)
width = 100 * 2 + text_counter * 50 + (text_counter - 1) * 10
height = 300
