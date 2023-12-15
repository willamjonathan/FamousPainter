from tkinter import *
from tkinter import ttk, filedialog, messagebox
import tkinter.font as font
from PIL import Image, ImageTk
import shutil
import os
import subprocess
import sys
import threading
from keras.preprocessing import *
from keras.models import load_model
import numpy as np

import imageio
import cv2

CONFIG_FILE = "reconstructor/config.txt"
CONFIG_FILE2 = "identifier/config.txt"

def buttonreconstruct_click():
    try:
        # subprocess.run(["python", "reconstructor/generated.py"])
        subprocess.run([sys.executable, "reconstructor/generated.py"])
        print('painting reconstructor is running')
    except Exception as e:
        print("error:buttonreconstruct ", str(e))


def buttonidentifier_click():
    try:
        # subprocess.run(["python", "identifier/main.py"])
        subprocess.run([sys.executable, "identifier/main.py"])
        print('painter identifier is running')
    except Exception as e:
        print("error: buttonidentifier ", str(e))

def run_reconstructor_script():
    try:
        global subprocess1
        subprocess1 = subprocess.Popen([sys.executable, "reconstructor/reconstruct.py"])
    except Exception as e:
        print("error: recon subprocess1", str(e))

def stop_processrecon():
    try:
        subprocess1.terminate()
    except Exception as e:
        print("error: stop recon", str(e))

def run_identify_script():
    try:
        global subprocess2
        subprocess2 = subprocess.Popen([sys.executable, "identifier/identifier.py"])
    except Exception as e:
        print("error: stop identify", str(e))
def stop_processident():
    try:
        subprocess2.terminate()
    except Exception as e:
        print("error: identify subprocess2", str(e))
        

def cleanPage(root):
    for widget in root.winfo_children():  
        widget.destroy()  

def landingPage(root):
    cleanPage(root)
    global myFont
    myFont = font.Font(family="Helvetica")
    # Add image file
    global background, backgroundpic
    backgroundpic = Image.open("backgrounds/background.png")
    background = ImageTk.PhotoImage(backgroundpic)

    # Show image using label
    backgroundlabel = Label(root, image=background, background="black")
    backgroundlabel.image = background
    backgroundlabel.place(x=0, y=0)

    title = Label(
        root,
        font=(myFont, 70),
        text="MUSE",
        bg="black",
        foreground="white"
    )
    title.place(relx=0.1, rely=0.25)

    line = Label(
        root,
        font=(myFont, 12),
        text="_____________________________________________________",
        bg="black",
        foreground="white"
    )
    line.place(relx=0.1, rely=0.37)

    desc = Label(
        root,
        font=(myFont, 18),
        text="famous painting reconstructor with  Deap",
        bg="black",
        foreground="#CBACFF"
    )
    desc.place(relx=0.1, rely=0.42)

    desc1 = Label(
        root,
        font=(myFont, 18),
        text="and painter identifier with Keras",
        bg="black",
        foreground="#CBACFF"
    )
    desc1.place(relx=0.1, rely=0.46)

    line1 = Label(
        root,
        font=(myFont, 12),
        text="_____________________________________________________",
        bg="black",
        foreground="white"
    )
    line1.place(relx=0.1, rely=0.5)

    desc2 = Label(
        root,
        font=(myFont, 15),
        text="A project of Andrean, Maria, Raissa, and William",
        bg="black",
        foreground="white"
    )
    desc2.place(relx=0.1, rely=0.545)

    desc2 = Label(
        root,
        font=(myFont, 15),
        text="for Artificial Intelligence Course",
        bg="black",
        foreground="white"
    )
    desc2.place(relx=0.1, rely=0.58)
    
    startbutton = Button(
        root,
        font=(myFont, 20),
        command=lambda:menupage(root),
        text="   Start   ",
        background="white",
        foreground="black",
    )
    startbutton.place(relx=0.1, rely=0.65)

def menupage(root):
    cleanPage(root)
    global myFont
    myFont = font.Font(family="Helvetica")
    # Add image file
    global background, backgroundpic
    backgroundpic = Image.open("backgrounds/background1.png")
    background = ImageTk.PhotoImage(backgroundpic)

    # Show image using label
    backgroundlabel = Label(root, image=background, background="black")
    backgroundlabel.image = background
    backgroundlabel.place(x=0, y=0)

    title = Label(
        root,
        font=(myFont, 50),
        text="RECONSTRUCTOR",
        bg="black",
        foreground="white"
    )
    title.place(relx=0.26, rely=0.15)

    desc = Label(
        root,
        font=(myFont, 15),
        text="Utilizing a genetic algorithm with DEAP framework, you can",
        bg="black",
        foreground="#CBACFF"
    )
    desc.place(relx=0.26, rely=0.25)
    desc1 = Label(
        root,
        font=(myFont, 15),
        text="reconstruct a painting for every 10 generations.",
        bg="black",
        foreground="#CBACFF"
    )
    desc1.place(relx=0.26, rely=0.29)

    reconstructbutton = Button(
        root,
        font=(myFont, 12),
        command=lambda:reconstruct(root),
        text="   Reconstruct   ",
        background="white",
        foreground="black",
    )
    reconstructbutton.place(relx=0.26, rely=0.35)

    line1 = Label(
        root,
        font=(myFont, 12),
        text="_______________________________________________________________",
        bg="black",
        foreground="white"
    )
    line1.place(relx=0.26, rely=0.44)

    title = Label(
        root,
        font=(myFont, 50),
        text="IDENTIFIER",
        bg="black",
        foreground="white"
    )
    title.place(relx=0.453, rely=0.5)
    desc2 = Label(
        root,
        font=(myFont, 15),
        text="Using a prediction model constructed with Keras Deep Learning ",
        bg="black",
        foreground="#CBACFF"
    )
    desc2.place(relx=0.26, rely=0.6)
    desc3 = Label(
        root,
        font=(myFont, 15),
        text="framework, you can identify the painter behind a painting with ",
        bg="black",
        foreground="#CBACFF"
    )
    desc3.place(relx=0.275, rely=0.635)
    desc4 = Label(
        root,
        font=(myFont, 15),
        text="corresponding accuracy scores.",
        bg="black",
        foreground="#CBACFF"
    )
    desc4.place(relx=0.477, rely=0.67)
    identifybutton = Button(
        root,
        font=(myFont, 12),
        command=lambda:identify(root),
        text="   Identify Painter   ",
        background="white",
        foreground="black",
    )
    identifybutton.place(relx=0.555, rely=0.725)
    returnButton = Button(
        root,
        font=(myFont, 8),
        command=lambda: landingPage(root),
        text="Return",
        background="white",

        foreground="black"
    )
    returnButton.place(relx=0.92, rely=0.02)

def reconstruct(root):
    cleanPage(root)
    global myFont
    myFont = font.Font(family="Helvetica")
    # Add image file
    global background, backgroundpic
    backgroundpic = Image.open("backgrounds/background2.png")
    background = ImageTk.PhotoImage(backgroundpic)

    # Show image using label
    backgroundlabel = Label(root, image=background, background="black")
    backgroundlabel.image = background
    backgroundlabel.place(x=0, y=0)
    def load_photo_path():
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r") as file:
                return file.read().strip()
        return None

    def save_photo_path(path):
        with open(CONFIG_FILE, "w") as file:
            file.write(path)

    desc2 = Label(
        root,
        font=(myFont, 15),
        text= "No image path uploaded.",
        bg="black",
        foreground="white"
    )
    desc2.place(relx=0.4, rely=0.44)

    def upload_photo():
       
        file_path = filedialog.askopenfilename(
            title="Select a Photo",
            filetypes=[
                ("PNG files", "*.png"),
                ("JPG files", "*.jpg"),
                ("JPEG files", "*.jpeg"),
                ("GIF files", "*.gif")
            ]
        )
        if file_path:
            repo_path = "reconstructor/images/upload"  
            os.makedirs(repo_path, exist_ok=True)
            photo_name = os.path.basename(file_path)
            dest_path = os.path.join(repo_path, photo_name)
            shutil.copyfile(file_path, dest_path)

            photo_path = dest_path
            print(f"Selected Photo Path: {photo_path}")
            save_photo_path(photo_path)
            
            photo_path = load_photo_path()
            desc2.config(text=photo_path)

    title = Label(
        root,
        font=(myFont, 50),
        text="RECONSTRUCT",
        bg="black",
        foreground="white"
    )
    title.place(relx=0.4, rely=0.25)
    desc = Label(
        root,
        font=(myFont, 15),
        text="Upload a painting to reconstruct",
        bg="black",
        foreground="#CBACFF"
    )
    desc.place(relx=0.4, rely=0.34)
    line = Label(
        root,
        font=(myFont, 10),
        text="_______________________________________________________________",
        bg="black",
        foreground="white"
    )
    line.place(relx=0.4, rely=0.38)

    desc1 = Label(
        root,
        font=(myFont, 15),
        text="Selected path to painting image:",
        bg="black",
        foreground="white"
    )
    desc1.place(relx=0.4, rely=0.41)

    line1 = Label(
        root,
        font=(myFont, 10),
        text="_______________________________________________________________",
        bg="black",
        foreground="white"
    )
    line1.place(relx=0.4, rely=0.5)           

    uploadbutton = Button(
        root,
        font=(myFont, 12),
        command=upload_photo,
        text="   Upload Painting Image   ",
        background="white",
        foreground="black",
    )
    uploadbutton.place(relx=0.4, rely=0.55)

    startrecons = Button(
        root,
        font=(myFont, 12),
        command=lambda: reconResult(root),
        text="   Start Reconstruction   ",
        background="white",
        foreground="black",
    )
    startrecons.place(relx=0.6, rely=0.55)
    returnButton = Button(
        root,
        font=(myFont, 8),
        command=lambda: menupage(root),
        text="Return",
        background="white",

        foreground="black"
    )
    returnButton.place(relx=0.92, rely=0.02)


def get_last_picture(folder_path):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    image_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path, x)), reverse=True)

    if image_files:
        return os.path.join(folder_path, image_files[0])
    else:
        return None

def show_last_picture(picture_label, folder_path):
    last_picture_path = get_last_picture(folder_path)
    if last_picture_path:
        image = PhotoImage(file=last_picture_path)
        picture_label.config(image=image)
        picture_label.image = image
    else:
        picture_label.config(text="No pictures in the folder.")


def reconResult(root):
    global subprocess1
    folder_path = "reconstructor/images/results"
    cleanPage(root)
    global myFont
    myFont = font.Font(family="Helvetica")
    # Add image file
    global background, backgroundpic
    backgroundpic = Image.open("backgrounds/background3.png")
    background = ImageTk.PhotoImage(backgroundpic)

    # Show image using label
    backgroundlabel = Label(root, image=background, background="black")
    backgroundlabel.image = background
    backgroundlabel.place(x=0, y=0)
    space=Label(root, background="black")
    space.pack(pady=2)
    desc = Label(
        root,
        font=(myFont, 12),
        text="Reconstructed image can be refreshed every 10 generations, this may take some time.",
        bg="black",
        foreground="#CBACFF"
    )
    desc.pack()
    desc1 = Label(
        root,
        font=(myFont, 12),
        text="If the current image hasn't passed 10 generations, it may show the previous image run.",
        bg="black",
        foreground="#CBACFF"
    )
    desc1.pack()

    picture_label = Label(root, background="black")
    picture_label.pack(padx=10, pady=10)

    def on_show_button_click():
        show_last_picture(picture_label, folder_path)

    show_button = Button(
        root,
        font=(myFont, 12),
        command=on_show_button_click,
        text="Refresh Most Recent Reconstruction",
        background="white",
        foreground="black",
    )
    show_button.pack(padx=10, pady=5)

    def returnafterstoppingrecon():
        stop_processrecon()
        returnButton = Button(
            root,
            font=(myFont, 8),
            command=lambda: reconstruct(root),
            text="Return",
            background="white",
            foreground="black"
        )
        returnButton.place(relx=0.92, rely=0.02)


    stop_button= Button(
        root,
        font=(myFont, 12),
        command= returnafterstoppingrecon,
        text="Stop Reconstruction",
        background="white",
        foreground="black",
    )
    stop_button.pack(padx=10, pady=5)
    thread_script1 = threading.Thread(target=run_reconstructor_script)
    thread_script1.start()
    thread_script1.join()
    root.protocol("WM_DELETE_WINDOW", quitrecon)

def quitrecon():
    stop_processrecon()
    root.destroy()



def identify(root):
    cleanPage(root)
    global myFont
    myFont = font.Font(family="Helvetica")
    # Add image file
    global background, backgroundpic
    backgroundpic = Image.open("backgrounds/background4.png")
    background = ImageTk.PhotoImage(backgroundpic)

    # Show image using label
    backgroundlabel = Label(root, image=background, background="black")
    backgroundlabel.image = background
    backgroundlabel.place(x=0, y=0)

    def load_photo_pathident():
        if os.path.exists(CONFIG_FILE2):
            with open(CONFIG_FILE2, "r") as file:
                return file.read().strip()
        return None

    def save_photo_path(path):
        with open(CONFIG_FILE2, "w") as file:
            file.write(path)

    desc2 = Label(
        root,
        font=(myFont, 15),
        text= "No image path uploaded.",
        bg="black",
        foreground="white"
    )
    desc2.place(relx=0.1, rely=0.44)

    def upload_photoident():
        file_path1 = filedialog.askopenfilename(
            title="Select a Photo",
            filetypes=[
                ("PNG files", "*.png"),
                ("JPG files", "*.jpg"),
                ("JPEG files", "*.jpeg"),
                ("GIF files", "*.gif")
            ]
        )
        if file_path1:
            repo_path = "identifier/images/upload"  
            os.makedirs(repo_path, exist_ok=True)
            photo_name = os.path.basename(file_path1)
            dest_path = os.path.join(repo_path, photo_name)
            shutil.copyfile(file_path1, dest_path)

            photo_path = dest_path
            print(f"Selected Photo Path: {photo_path}")
            save_photo_path(photo_path)
            
            photo_path = load_photo_pathident()
            desc2.config(text=photo_path)

    title = Label(
        root,
        font=(myFont, 50),
        text="IDENTIFY",
        bg="black",
        foreground="white"
    )
    title.place(relx=0.1, rely=0.25)
    desc = Label(
        root,
        font=(myFont, 15),
        text="Upload a painting to predict its painter",
        bg="black",
        foreground="#CBACFF"
    )
    desc.place(relx=0.1, rely=0.34)
    line = Label(
        root,
        font=(myFont, 10),
        text="_______________________________________________________________",
        bg="black",
        foreground="white"
    )
    line.place(relx=0.1, rely=0.38)

    desc1 = Label(
        root,
        font=(myFont, 15),
        text="Selected path to painting image:",
        bg="black",
        foreground="white"
    )
    desc1.place(relx=0.1, rely=0.41)

    line1 = Label(
        root,
        font=(myFont, 10),
        text="_______________________________________________________________",
        bg="black",
        foreground="white"
    )
    line1.place(relx=0.1, rely=0.5)           

    uploadbutton = Button(
        root,
        font=(myFont, 12),
        command=upload_photoident,
        text="   Upload Painting Image   ",
        background="white",
        foreground="black",
    )
    uploadbutton.place(relx=0.1, rely=0.55)

    startidentify = Button(
        root,
        font=(myFont, 12),
        command=lambda: identifyresult(root),
        text="   Start Prediction   ",
        background="white",
        foreground="black",
    )
    startidentify.place(relx=0.3, rely=0.55)
    returnButton = Button(
        root,
        font=(myFont, 8),
        command=lambda: menupage(root),
        text="Return",
        background="white",

        foreground="black"
    )
    returnButton.place(relx=0.92, rely=0.02)





def identifyresult(root):
    global subprocess2
    global flag1
    global file_path1
    file_path1 = "identifier/config.txt"
    cleanPage(root)
    global myFont
    myFont = font.Font(family="Helvetica")
    global background, backgroundpic
    backgroundpic = Image.open("backgrounds/background3.png")
    background = ImageTk.PhotoImage(backgroundpic)

    backgroundlabel = Label(root, image=background, background="black")
    backgroundlabel.image = background
    backgroundlabel.place(x=0, y=0)

    picture_label = Label(root, background="black")
    picture_label.pack(padx=10, pady=10)
    
    try:
        with open(file_path1, "r") as file:
            file_content = file.read().strip()  # Strip any leading/trailing whitespace

        # Load the image
        img = Image.open(file_content)  # Adjust the size as needed
        photo = ImageTk.PhotoImage(img)

        # Display the picture
        picture_label1 = Label(root, image=photo)
        picture_label1.pack(padx=10, pady=10)
        
        labels = {0: 'Vincent_van_Gogh', 1: 'Edgar_Degas', 2: 'Pablo_Picasso', 3: 'Pierre-Auguste_Renoir', 4: 'Albrecht_Dürer', 5: 'Paul_Gauguin', 6: 'Francisco_Goya', 7: 'Rembrandt', 8: 'Alfred_Sisley', 9: 'Titian', 10: 'Marc_Chagall'}

        loaded_model = load_model('identifier/keras_model.h5')
        model = loaded_model

        train_input_shape = (224, 224, 4)
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
        
        text_label = Label(root, text="Your painting might be made by "+labels[prediction_idx].replace('_', ' '))
        text_label.pack(pady=10)
        
        text_label = Label(root, text="The prediction accuracy: "+str(prediction_probability*100)+ " %")
        text_label.pack(pady=10)

    except FileNotFoundError:
        print(f"File not found: {file_path1}")
    except Exception as e:
        print(f"An error occurred: {e}")

    def returnafterstoppingidentify():
        stop_processident()
        identify(root)


    stop_button= Button(
        root,
        font=(myFont, 12),
        command= returnafterstoppingidentify,
        text="Finish and Return",
        background="white",
        foreground="black",
    )
    stop_button.pack(padx=10, pady=5)
    thread_script2 = threading.Thread(target=run_identify_script)
    thread_script2.start()
    thread_script2.join()
    stop_processrecon()
    root.protocol("WM_DELETE_WINDOW", quitrecon)

def main():
    width = 1000
    height = 700

    global root
    root = Tk()
    root.config(bg="#2C602E")
    root.title("MUSE")
    global myFont
    myFont = font.Font(family="Helvetica")

    setW = root.winfo_screenwidth()
    setH = root.winfo_screenheight()

    padW = (setW//2)-(width//2)
    padH = (setH//2)-(height//2)

    root.geometry(f"{width}x{height}+{padW}+{padH}")
    root.resizable(False, False)

    landingPage(root)
    root.mainloop()

main()