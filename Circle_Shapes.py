from turtle import Turtle, Screen
window=Screen()
A=Turtle("turtle")
A.speed("fast")

def draw_square():
   A.color("blue")
   A.shape("turtle")
   A.pensize(3)
   for _ in range(10):
    for i in range(4):
        A.forward(100)
        A.right(90)
    A.right(36)

def draw_circle():
    A.color("red")
    A.shape("square")
    A.pensize(5)
    for _ in range(10):
        A.circle(50)
        A.right(36)

def draw_star():
    A.color("green")
    A.shape("arrow")
    A.pensize(7)
    for _ in range(10):
        for i in range(5):
            A.forward(100)
            A.right(144)
        A.right(36)



def main():
    while True:
        inbox=window.textinput("Shape Drawer","Enter the shape you want to draw (square, circle, star) or type 'exit' to quit:\nادخل الشكل الذي تريد رسمه (مربع، دائره، نجمه) او اكتب 'خروج' للخروج:")
        if inbox is None: break
        A.clear()
        if inbox=="مربع" or inbox=="square":
            draw_square()
        elif inbox=="دائره" or inbox=="circle":
            draw_circle()
        elif inbox=="نجمه" or inbox=="star":
            draw_star()
        elif inbox=="exit" or inbox=="خروج":
            A.clear()
            A.hideturtle()
            window.bgcolor("cyan")
            A.color("black")
            A.write("click mouse to exit\n🏃انقر بالماوس للخروج", align="center", font=("Arial", 20, "normal"))
            window.exitonclick()
            break
    
main()