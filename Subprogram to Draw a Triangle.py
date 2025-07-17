import turtle
t = turtle.Turtle()
t.speed(5) 
t.pensize(7)

# Create a subprogram to draw a triangle
def drawtriangle():
  for i in range(3):
    t.forward(100)
    t.left(120)
    
# Call the subprogram
drawtriangle()
