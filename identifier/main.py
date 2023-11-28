import os
import tkinter as tk
from tkinter import PhotoImage
import threading
from identifier import main
import subprocess
from uploader import upload
from PIL import Image, ImageTk
from keras.preprocessing import *
from keras.models import load_model
from skimage.io import imread
from skimage.transform import resize
import numpy as np
import matplotlib.pyplot as plt
import random
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import pandas as pd
import imageio.v2 as imageio
import cv2

upload()
def run_script1():
    try:
        global subprocess1
        subprocess1 = subprocess.Popen(["python", "identifier/identifier.py"])
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

        self.folder_path = "identifier/images/results"
        self.create_widgets()
        
    def create_widgets(self):
        self.picture_label = tk.Label(self.root)
        self.picture_label.pack(padx=10, pady=10)

        self.text_label = tk.Label(self.root, text="This Is Identifier Lur")
        self.text_label.pack(pady=10)
        
        file_path = "identifier/config.txt"

        try:
            with open(file_path, "r") as file:
                file_content = file.read().strip()  # Strip any leading/trailing whitespace

            # Load the image
            img = Image.open(file_content)  # Adjust the size as needed
            self.photo = ImageTk.PhotoImage(img)

            # Display the picture
            self.picture_label = tk.Label(self.root, image=self.photo)
            self.picture_label.pack(padx=10, pady=10)
            
            labels = {0: 'Vincent_van_Gogh', 1: 'Edgar_Degas', 2: 'Pablo_Picasso', 3: 'Pierre-Auguste_Renoir', 4: 'Albrecht_Dürer', 5: 'Paul_Gauguin', 6: 'Francisco_Goya', 7: 'Rembrandt', 8: 'Alfred_Sisley', 9: 'Titian', 10: 'Marc_Chagall'}

            loaded_model = load_model('identifier/keras_model.h5')
            model = loaded_model
            import imageio
            import cv2
            train_input_shape = (224, 224, 3)
            random_image_file = file_content
            web_image = imageio.imread(random_image_file)
            web_image = cv2.resize(web_image, dsize=train_input_shape[0:2], )
            web_image = image.img_to_array(web_image)
            web_image /= 255.
            web_image = np.expand_dims(web_image, axis=0)

            prediction = model.predict(web_image)
            prediction_probability = np.amax(prediction)
            prediction_idx = np.argmax(prediction)

            
            print("Predicted artist =", labels[prediction_idx].replace('_', ' '))
            print("Prediction probability =", prediction_probability*100, "%")
            
            self.text_label = tk.Label(self.root, text="Your painting might be made by "+labels[prediction_idx].replace('_', ' '))
            self.text_label.pack(pady=10)
            
            self.text_label = tk.Label(self.root, text="The prediction accuracy: "+str(prediction_probability*100)+ " %")
            self.text_label.pack(pady=10)

        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")
            
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
    label = tk.Label(root, text="Kindly Terimante The Code If YOU DON'T WANT BURN YOUR PC")
    label.pack()
    root.mainloop()

def run_script2():
    generated()

if __name__ == "__main__":
    thread_script1 = threading.Thread(target=run_script1)
    thread_script1.start()
    run_script2()
    thread_script1.join()
