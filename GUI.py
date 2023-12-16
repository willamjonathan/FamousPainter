import tkinter as tk
from tkinter import ttk
import os
import subprocess
from PIL import Image, ImageTk
import sys

def button1_click():
    try:
        # subprocess.run(["python", "reconstructor/generated.py"])
        subprocess.run([sys.executable, "reconstructor/generated.py"])

        label.config(text="Painting generator is run", fg="green")
    except Exception as e:
        label.config(text=f"Error: {str(e)}", fg="red")

def button2_click():
    try:
        # subprocess.run(["python", "identifier/main.py"])
        subprocess.run([sys.executable, "identifier/identifier.py"])
        label.config(text="Painting identifier is run", fg="green")
    except Exception as e:
        label.config(text=f"Error: {str(e)}", fg="red")

# Create the main window
root = tk.Tk()
root.title("AI Project")

# Center the window on the screen
# window_width = 400
# window_height = 350  
window_width = 1000
window_height = 700 
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Update idletasks to ensure the window is properly centered
root.update_idletasks()

# Styling
style = ttk.Style()
style.configure("TButton", padding=10, font=("Helvetica", 12))

# Set background color to dark brown
root.configure(bg="#3E2723")

# Title label
title_label = tk.Label(root, text="Famous Painters", font=("Helvetica", 16), pady=10, bg="#3E2723", fg="white")
title_label.pack()

# Load and display an image
image_path = "painting1.jpg"  # Replace with the actual path to your image file
if os.path.exists(image_path):
    pil_image = Image.open(image_path)
    image = ImageTk.PhotoImage(pil_image)
    
    # Create a frame around the image
    frame = ttk.Frame(root, style="TFrame")
    frame.pack(pady=10)
    
    image_label = tk.Label(frame, image=image)
    image_label.pack()
button_frame = tk.Frame(root,bg = "#3E2723")
button_frame.pack(side=tk.TOP, padx=20, pady=10)

# Create and add buttons with updated names
button1 = ttk.Button(button_frame, text="Generator", command=button1_click, style="TButton")
button2 = ttk.Button(button_frame, text="Identifier", command=button2_click, style="TButton")

# Set button colors
style.map("TButton",
          foreground=[('pressed', 'black'), ('active', 'black')],
          background=[('pressed', '!disabled', 'black'), ('active', 'black')])



# Add padding and set grid layout
button1.pack(side=tk.LEFT, padx=20, pady=20)
button2.pack(side=tk.LEFT, padx=20, pady=20)

label = tk.Label(root, text="", font=("Arial", 12),bg = "#B5B5B5",fg="white")
label.pack(pady=20)
# Run the Tkinter event loop
root.mainloop()
