import turtle

# Set window size (adjust if needed)
turtle.setup(width=800, height=600)

# Create a turtle object
t = turtle.Turtle()

# Hide the turtle (optional)
t.hideturtle()

# Speed up drawing
t.speed(0)  # Set speed to fastest (no animation)

# Function to draw a circle
def draw_circle(x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(color)
    t.circle(radius)

# Function to check if a point is within the circle
def is_in_circle(x, y, center_x, center_y, radius):
    return (x - center_x)**2 + (y - center_y)**2 <= radius**2

# Function for boundary fill animation (recursive approach)
def boundary_fill_circle_animated(x, y, new_color, boundary_color, radius):
    colors = {}

    def fill(x, y):
        # Check if within circle and not already filled
        if not is_in_circle(x, y, 0, 0, radius) or (x, y) in colors:
            return

        colors[(x, y)] = new_color
        t.color(new_color)  # Set color directly (no pen down/up)
        t.dot(2)  # Draw a small dot for visualization (adjust size as needed)

        # Recursively fill neighbors (except boundary)
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if is_in_circle(nx, ny, 0, 0, radius) and colors.get((nx, ny)) != boundary_color:
                    fill(nx, ny)

    fill(x, y)
    turtle.update()  # Update the screen once after the entire fill

# Draw the black circle (boundary)
draw_circle(0, 0, 100, "black")

# Set the starting point (bottom of the circle) and color
x, y = 0, -100
new_color = "red"

# Perform boundary fill animation (no delay for faster fill)
boundary_fill_circle_animated(x, y, new_color, "black", 100)

# Keep the window open until closed manually
turtle.done()