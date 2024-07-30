import tkinter as tk

def button_clicked():
    print("Button clicked!")

# Create the main application window
root = tk.Tk()
root.title("Simple Interface")

# Create a label widget
label = tk.Label(root, text="Welcome to My Interface")
label.pack()

# Create a button widget
button = tk.Button(root, text="Click Me", command=button_clicked)
button.pack()

# Start the Tkinter event loop
root.mainloop()
