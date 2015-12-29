import turtle

window = turtle.Screen()
window.bgcolor("yellow")

#Initialized first instance of class Turtle called brad
brad = turtle.Turtle()
brad.color('RED')
brad.speed(100)
brad.shape('turtle')

#Initialized second instance of class Turtle called angie
angie = turtle.Turtle()
angie.shape("arrow")
angie.color("red")
angie.setpos(100,100)
angie.speed(1000)
"""
def print_squares():
    for four_iter in range(0,4):    
        brad.forward(100)
        brad.right(90)
"""
def print_triangle():
    angie.right(6)
    for three_iter in range(0,3):
        angie.forward(100)
        angie.right(120)
        
for indef in range(0,60):
    if(indef%2 == 0):
        brad.color('RED')
    else:
        brad.color('BLUE')
    print_triangle()
    


print_triangle()
window.exitonclick()

        



