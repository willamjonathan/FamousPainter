import tkinter as tk
from tkinter import filedialog
import shutil
import os

CONFIG_FILE = "identifier/config.txt"

class PhotoUploaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Project")

        self.photo_path = self.load_photo_path()

        self.create_widgets()

    def create_widgets(self):
        # Create a label to display the selected photo path
        self.path_label = tk.Label(self.root, text="Upload the painting first!")
        self.path_label.pack(pady=10)

        # Create a button to open the file dialog
        self.upload_button = tk.Button(self.root, text="Upload Photo", command=self.upload_photo)
        self.upload_button.pack(pady=10)

        # Create a button to use the selected photo path in another file
        self.use_button = tk.Button(self.root, text="Use Photo Path", command=self.use_photo_path)
        self.use_button.pack(pady=10)

    def load_photo_path(self):
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r") as file:
                return file.read().strip()
        return None

    def save_photo_path(self, path):
        with open(CONFIG_FILE, "w") as file:
            file.write(path)

    def upload_photo(self):
        file_path = filedialog.askopenfilename(title="Select a Photo", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])

        if file_path:

            repo_path = "identifier/images/upload"  
            os.makedirs(repo_path, exist_ok=True)
            photo_name = os.path.basename(file_path)
            dest_path = os.path.join(repo_path, photo_name)
            shutil.copyfile(file_path, dest_path)

            self.photo_path = dest_path
            self.path_label.config(text=f"Selected Photo Path: {self.photo_path}")
            self.save_photo_path(self.photo_path)

    def use_photo_path(self):
        if self.photo_path:
            print(f"Using Photo Path: {self.photo_path}")
        else:
            print("No photo selected.")


def upload():
        # Create the main window
    root = tk.Tk()
    root.title("AI Project")
    # Set background color to dark brown
    # root.configure(bg="#3E2723")
    app = PhotoUploaderApp(root)
            # Center the window on the screen
    window_width = 500
    window_height = 400  # Increased height to accommodate the title and image
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    root.mainloop()
