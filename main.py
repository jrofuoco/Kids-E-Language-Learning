# main.py
import os
import tkinter as tk
import customtkinter
from PIL import Image, ImageTk

from logInWindow import loginWindow
from startWindow import startWindow
from homeWindow import homePageWindow
from newUser import newUserAccount

# ---------- Helper function to load and resize images ----------
def load_image(filename, size):
    """
    Load an image from the drawables folder and resize it.
    :param filename: Image file name (e.g., 'startpage.png')
    :param size: Tuple (width, height)
    :return: ImageTk.PhotoImage
    """
    image_path = os.path.join(DRAWABLES_DIR, filename)
    img = Image.open(image_path)
    img = img.resize(size, Image.LANCZOS)  # LANCZOS = high-quality resize
    return ImageTk.PhotoImage(img)

# ---------- Base paths ----------
BASE_DIR = os.path.dirname(__file__)               # Project folder
DRAWABLES_DIR = os.path.join(BASE_DIR, "drawables")  # drawables folder

# ---------- Tkinter window setup ----------
root = customtkinter.CTk()
root.title("Kids: E-Language Learning System")
root.geometry("860x580")
root.resizable(False, False)

# ---------- Load images ----------
image = load_image("startpage.png", (1080, 720))
image1 = load_image("loginpage.png", (1080, 720))
firstPageImage = load_image("firstpage1.png", (1080, 720))
newUserImage = load_image("newuser.png", (1080, 720))

# ---------- Function to open login window ----------
def openLoginWindow(root, image1):
    loginWindow(root, image1, firstPageImage, homePageWindow, newUserAccount, newUserImage)

# ---------- Start the application ----------
startWindow(root, image, openLoginWindow, image1)

root.mainloop()
