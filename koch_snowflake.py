# Напишіть програму на Python, яка використовує рекурсію для створення фракталу «сніжинка Коха»
# за умови, що користувач повинен мати можливість вказати рівень рекурсії.


import turtle
import argparse


def draw_koch_curve(t, order, size):
    """Draw a Koch curve with given turtle t, order, and size."""
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            draw_koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(order, size=300):
    """Draw a Koch curve of a given order and size."""
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.color("blue")
    t.width(2)

    # set pen initial position on the window
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    # Draw the three sides of the Koch snowflake
    for _ in range(3):
        draw_koch_curve(t, order, size)
        t.right(120)

    window.mainloop()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Draw a Koch snowflake fractal.")
    parser.add_argument(
        "order",
        type=int,
        default=3,
        nargs="?",
        help="The order of the Koch curve (non-negative integer).",
    )
    args = parser.parse_args()

    if args.order < 0:
        print("Order must be a non-negative integer.")
    else:
        draw_koch_snowflake(args.order)

# Example usage:
# python koch_snowflake.py
# python koch_snowflake.py 2
