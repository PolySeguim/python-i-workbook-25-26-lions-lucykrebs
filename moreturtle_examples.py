import turtle

screen=turtle.Screen
lucy = turtle.Turtle() #this is the instantiation call for the object screen
lucy.color("red")
lucy.shape("turtle")
lucy.circle(80)

# Move the turtle forward by 100 units lucy.forward(100)
lucy.forward(100)

# Turn the turtle to the right by 90 degrees
# Right90 is a nonfruitful function because it does not require a value, 
# it simply performs an action, which is to turn the turtle 90 degrees to the right

# Timer is in milliseconds
# "Up" is up arrow on keyboard

# Repeat the above steps to complete the square

# Keep the window open until clicked


subjects = ["English","Math","Science","Health","Economics"]
for subject in subjects:
    print("My favorite subject is: ", subject)

counter=0
while counter<= len(subjects):
    print("Counter: ", counter)
    counter=counter + 1


screen=turtle.Screen()
rainbow=turtle.Turtle()
screen=turtle.Screen()
rainbow.circle(50)

def rainbow():
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    for color in colors:
        rainbow.color(color)
        rainbow.forward(10)
        rainbow.circle(20)
        rainbow.forward(10)

screen.listen()
screen.mainloop()
turtle.done()

def backForth():
    lucy.forward(-300)
    lucy.speed(0)
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    for color in colors:
        lucy.color(color)
        lucy.pensize(3)
        lucy.forward(100)
        lucy.forward(-50)
