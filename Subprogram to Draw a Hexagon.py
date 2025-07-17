import turtle
t = turtle.Turtle()
t.speed(5) 
t.pensize(7)

# Create a subprogram to draw a hexagon
def drawhexagon():
  for i in range(6):
    t.left(60)
    t.fd(100)
    
# Call the subprogram
drawhexagon()
