import turtle
t = turtle.Turtle()
t.speed(5) 
t.pensize(7)

# Create a subprogram to draw a rectangle
def drawrectangle():
  for i in range(2):
    t.forward(200)
    t.right(90)
    t.fd(100)
    t.right(90)
    
    
# Call the subprogram
drawrectangle()
