import turtle
import random

# Initialize the turtles
dad = turtle.Turtle()
mom = turtle.Turtle()
victor = turtle.Turtle()
eva = turtle.Turtle()

# Initialize the screen
screen = turtle.Screen()
screen.title('Family Race')
screen.setup(width=800, height=400)

# Starting positions and names
start_x = -350
start_y_positions = [100, 50, -50, -100]
turtles = [dad, mom, victor, eva]
colors = ['red', 'blue', 'green', 'purple']
names = ['Dad', 'Mom', 'Victor', 'Eva']  # Names for each turtle

# Customize turtles, move them to the start line, and display names
for i, turtle_obj in enumerate(turtles):
    turtle_obj.shape('turtle')
    turtle_obj.color(colors[i])
    turtle_obj.penup()
    turtle_obj.goto(start_x, start_y_positions[i])
    # Display name next to the turtle
    turtle_obj.write(names[i], move=False, align="left", font=("Arial", 8, "normal"))

# Define the finish line
finish_line = 350

# Race Logic
race_on = True
while race_on:
    for turtle_obj in turtles:
        # Move each turtle forward by a random amount
        turtle_obj.forward(random.randint(1, 10))

        # Check for a turtle crossing the finish line
        if turtle_obj.xcor() >= finish_line:
            race_on = False
            winning_color = turtle_obj.color()[0]  # Get the turtle's color
            print(f"The winner is the {winning_color} turtle!")
            break

screen.mainloop()  # Keep the window open
