import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Canım Annem")
screen.setup(width=800, height=600)


def draw_heart():
    heart = turtle.Turtle()
    heart.speed(3)
    heart.shape("turtle")
    heart.color("pink")
    heart.fillcolor("pink")
    heart.penup()
    heart.goto(0, -100)
    heart.pendown()

    heart.begin_fill()
    heart.left(50)
    heart.forward(133)
    heart.circle(50, 200)
    heart.right(140)
    heart.circle(50, 200)
    heart.forward(133)
    heart.end_fill()
    heart.hideturtle()


def write_text(message, font_size, color, x, y):
    text_turtle = turtle.Turtle()
    text_turtle.hideturtle()
    text_turtle.color(color)
    text_turtle.penup()
    text_turtle.goto(x, y)
    text_turtle.write(message, align="center", font=("Arial", font_size, "bold"))


draw_heart()


write_text("Canım Annem!", 35, "white", 0, -180)
write_text("Anneler Günün Kutlu Olsun 💖", 22, "white", 0, -240)

turtle.done()


