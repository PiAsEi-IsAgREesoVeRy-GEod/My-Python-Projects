import turtle
t = turtle.Turtle()
t.speed(5) 
t.pensize(7)

# Create a subprogram to draw a pentagon
def drawpentagon():
  for i in range(5):
    t.left(72)
    t.fd(100)
    
# Call the subprogram
drawpentagon()
