# logInWindow.py
import os
import tkinter as tk
import customtkinter
from PIL import Image
import DatabaseHelper
import hashlib


# ---------- Paths ----------
BASE_DIR = os.path.dirname(__file__)
DRAWABLES_DIR = os.path.join(BASE_DIR, "drawables")

def load_icon(filename, size=None):
    """Load an icon from the drawables folder."""
    path = os.path.join(DRAWABLES_DIR, filename)
    img = Image.open(path)
    if size:
        img = img.resize(size, Image.LANCZOS)
    return customtkinter.CTkImage(img)

def loginWindow(root, image1, firstPageImage, homePageWindow, newUserAccount, newUserImage):
    global username
    username = ""
    password = ""

    def openHomePageWindow():
        canvas1.pack_forget()
        homePageWindow(root, firstPageImage, canvas1, username, password, usernameEntry, passwordEntry)

    def openNewUser():
        canvas1.pack_forget()
        newUserAccount(root, newUserImage, canvas1)

    def logIn():
        global username
        username = usernameEntry.get()
        password = passwordEntry.get()

        login_result = DatabaseHelper.getUsernameAndPassword(username, password)
        print(DatabaseHelper.loginValidation)

        if username == "" or password == "":
            wrongAnswer.configure(text="Invalid Input")
            displayWrongAnswer(3)
        elif login_result:
            openHomePageWindow()
        else:
            wrongAnswer.configure(text="Wrong Username or Password")
            displayWrongAnswer(3)

    canvas1 = tk.Canvas(root, width=1080, height=720)
    canvas1.create_image(0, 0, anchor=tk.NW, image=image1)
    canvas1.pack()

    def displayWrongAnswer(count):
        wrongAnswer.configure(text_color="#ff0000")
        if count > 0:
            root.after(200, displayWrongAnswer, count - 1)
        else:
            wrongAnswer.configure(text_color="#f0f0f0")

    wrongAnswer = customtkinter.CTkLabel(
        canvas1,
        text="Invalid Input",
        text_color="#f0f0f0",
        fg_color="#f0f0f0",
        font=("Comic Sans MS", 13)
    )
    wrongAnswer.place(relx=0.5, rely=0.37, anchor=tk.CENTER)

    usernameEntry = customtkinter.CTkEntry(
        canvas1, placeholder_text="Username",
        border_color="#b14802",
        width=200, height=40,
        justify='center',
        fg_color="#f0f0f0", text_color="#fd6909"
    )
    usernameEntry.place(relx=0.5, rely=0.43, anchor=tk.CENTER)

    passwordEntry = customtkinter.CTkEntry(
        canvas1, placeholder_text="Password",
        border_color="#b14802",
        width=200, height=40,
        justify='center',
        fg_color="#f0f0f0", show="*", text_color="#fd6909"
    )
    passwordEntry.place(relx=0.5, rely=0.51, anchor=tk.CENTER)

    # Icons
    userIcon = load_icon("usernameicon.png")
    customtkinter.CTkButton(
        canvas1, text="",
        image=userIcon,
        font=("Comic Sans MS", 15),
        text_color="white",
        hover_color="#f0f0f0",
        fg_color="#f0f0f0",
        state="DISABLED",
        width=3, height=5
    ).place(relx=0.408, rely=0.43, anchor=tk.CENTER)

    passwordIcon = load_icon("passwordicon.png")
    customtkinter.CTkButton(
        canvas1, text="",
        image=passwordIcon,
        font=("Comic Sans MS", 15),
        text_color="white",
        hover_color="#f0f0f0",
        fg_color="#f0f0f0",
        state="DISABLED",
        width=3, height=5
    ).place(relx=0.410, rely=0.51, anchor=tk.CENTER)

    # Buttons
    customtkinter.CTkButton(
        canvas1, text="Login",
        font=("Comic Sans MS", 20),
        text_color="white",
        corner_radius=40,
        hover_color="#b14802",
        fg_color="#fd6909",
        width=200, height=15,
        command=logIn
    ).place(relx=0.5, rely=0.59, anchor=tk.CENTER)

    customtkinter.CTkButton(
        canvas1, text="New User",
        font=("Comic Sans MS", 15),
        text_color="white",
        corner_radius=50,
        hover_color="#b14802",
        fg_color="#fd6909",
        width=200, height=10,
        command=openNewUser
    ).place(relx=0.5, rely=0.655, anchor=tk.CENTER)
