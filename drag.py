import tkinter as tk


def on_drag_start(event):
    # Records the initial position of the widget being dragged
    global prev_x, prev_y
    prev_x = event.x
    prev_y = event.y


def on_drag_motion(event):
    # Calculates the distance moved by the mouse
    global prev_x, prev_y
    new_x = event.x
    new_y = event.y
    x_change = new_x - prev_x
    y_change = new_y - prev_y

    # Move the widget by the calculated distance
    canvas.move(widget_to_move, x_change, y_change)
    canvas.pack()

    # Update the previous position
    prev_x = new_x
    prev_y = new_y


root = tk.Tk()
root.title("Drag and Drop Example")

# canvas = tk.Canvas(root, width=400, height=300, bg='white')
# canvas.pack()

# # Create a rectangle to demonstrate drag and drop
# widget_to_move = canvas.create_rectangle(50, 50, 100, 100, fill='blue')
canvas = tk.Label(root, text='hello')

# Binding mouse events to enable drag and drop
canvas.bind('<ButtonPress-1>', on_drag_start)
canvas.bind('<B1-Motion>', on_drag_motion)

root.mainloop()
