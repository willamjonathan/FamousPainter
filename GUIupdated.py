from tkinter import *
from tkinter import ttk, filedialog, messagebox
import tkinter as tk
import tkinter.font as font
from PIL import Image, ImageTk


def cleanPage(root):
    """
    Method to clean the window
    """
    for widget in root.winfo_children():  # To know the widgets used in that page
        widget.destroy()  # To delete all the widgets with iteration

def landingPage(root):
    cleanPage(root)
    global myFont
    myFont = font.Font(family="Helvetica")
    # Add image file
    global background, backgroundpic
    backgroundpic = Image.open("background.png")
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
    backgroundpic = Image.open("background1.png")
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
        command=lambda:menupage(root),
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
        text="IDENTIFY",
        bg="black",
        foreground="white"
    )
    title.place(relx=0.49, rely=0.5)
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
        command=lambda:menupage(root),
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

def main():
    width = 1000
    height = 700

    # Create tkinter root
    global root
    root = Tk()
    root.config(bg="#2C602E")
    root.title("MUSE")
    global myFont
    myFont = font.Font(family="Helvetica")

    # Assign value of device screen size
    setW = root.winfo_screenwidth()
    setH = root.winfo_screenheight()

    # Set the padding so it will position window center
    padW = (setW//2)-(width//2)
    padH = (setH//2)-(height//2)

    # Set the window size and position
    root.geometry(f"{width}x{height}+{padW}+{padH}")
    root.resizable(False, False)

    landingPage(root)
    root.mainloop()

main()