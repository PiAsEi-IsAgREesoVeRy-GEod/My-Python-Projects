import turtle
t = turtle.Turtle()
t.speed(5) 
t.pensize(7)

# Create a subprogram to draw a square
def drawsquare():
  for i in range(4):
    t.forward(100)
    t.right(90)
# Call the subprogram
drawsquare()
