import os
import tkinter as tk
from tkinter import PhotoImage
import threading
from reconstruct import main
import subprocess
from uploader import upload

upload()
def run_script1():
    try:
        global subprocess1
        subprocess1 = subprocess.Popen(["python", "reconstructor/reconstruct.py"])
    except Exception as e:
        label.config(text=f"Error: {str(e)}", fg="red")

def stop_button_click():
    try:
        subprocess1.terminate()
    except Exception as e:
        label.config(text=f"Error: {str(e)}", fg="red")

class LastPictureViewerApp:
    # upload()
    global flag
    def __init__(self, root):
        self.root = root
        self.root.title("Last Picture Viewer")

        self.folder_path = "reconstructor/images/results"
        self.create_widgets()

    def create_widgets(self):
        self.picture_label = tk.Label(self.root)
        self.picture_label.pack(padx=10, pady=10)

        self.show_button = tk.Button(self.root, text="Show Last Picture", command=self.show_last_picture)
        self.show_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text="stop generation", command=stop_button_click)
        self.stop_button.pack(pady = 10)  

    def get_last_picture(self):
        files = [f for f in os.listdir(self.folder_path) if os.path.isfile(os.path.join(self.folder_path, f))]
        image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        image_files.sort(key=lambda x: os.path.getmtime(os.path.join(self.folder_path, x)), reverse=True)

        if image_files:
            return os.path.join(self.folder_path, image_files[0])
        else:
            return None

    def show_last_picture(self):
        last_picture_path = self.get_last_picture()
        if last_picture_path:
            image = PhotoImage(file=last_picture_path)
            self.picture_label.config(image=image)
            self.picture_label.image = image
        else:
            self.picture_label.config(text="No pictures in the folder.")



def generated():
    root = tk.Tk()
    app = LastPictureViewerApp(root)
    root.title("AI Project")
    # root.configure(bg="#3E2723")
    window_width = 800
    window_height = 700  
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    label = tk.Label(root, text="Before exiting please click stop generation! ")
    label.pack()
    label1 = tk.Label(root, text="If you forget please terminate the code! ")
    label1.pack()

    root.mainloop()

def run_script2():
    generated()

if __name__ == "__main__":
    thread_script1 = threading.Thread(target=run_script1)
    thread_script1.start()
    run_script2()
    thread_script1.join()
