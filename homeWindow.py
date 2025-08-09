import os
import tkinter as tk
import customtkinter
from PIL import Image, ImageTk
import level_one
import level_two
import level_three
import level_four
import level_five
import level_six
import level_seven
import level_eight
import level_nine
import second_page
import time
import DatabaseHelper

# ---------- Paths ----------
BASE_DIR = os.path.dirname(__file__)
DRAWABLES_DIR = os.path.join(BASE_DIR, "drawables")

locked = "#2b2d30"
unlocked = "#fd6909"


def homePageWindow(root, firstPageImage, canvas1, username, password, usernameEntry, passwordEntry):
    global level
    level = DatabaseHelper.getLevel(username)
    print(level)
    convertLevel = str(level)

    def updateHomeWindow():
        global level
        level = DatabaseHelper.getLevel(username)
        print(level)
        convertLevel = str(level)
        levelText.configure(text="Level: " + str(level))

        if convertLevel == "2":
            bLevel.configure(state="normal", command=openLevelTwo, fg_color="#fd6909")

        if convertLevel == "3":
            cLevel.configure(state="normal", command=openLevelThree, fg_color="#fd6909")

        if convertLevel == "4":
            dLevel.configure(state="normal", command=openLevelFour, fg_color="#fd6909")

        if convertLevel == "5":
            eLevel.configure(state="normal", command=openLevelFive, fg_color="#fd6909")

        if convertLevel == "6":
            fLevel.configure(state="normal", command=openLevelSix, fg_color="#fd6909")

        if convertLevel == "7":
            gLevel.configure(state="normal", command=openLevelSeven, fg_color="#fd6909")

        if convertLevel == "8":
            hLevel.configure(state="normal", command=openLevelEight, fg_color="#fd6909")

        if convertLevel == "9":
            iLevel.configure(state="normal", command=openLevelNine, fg_color="#fd6909")
            nextPageButton.configure(state="normal", command=logOutCommand, fg_color="#fd6909")

        if convertLevel == "10":
            nextPageButton.configure(state="normal", command=openSecondPage, fg_color="#fd6909")

        homePageCanvas.pack()

    def openLevelOne():
        level_one.levelOne(root, homePageCanvas, username, level, updateHomeWindow)
        homePageCanvas.pack_forget()

    def openLevelTwo():
        level_two.levelTwo(root, homePageCanvas, username, level, updateHomeWindow)
        homePageCanvas.pack_forget()

    def openLevelThree():
        level_three.levelThree(root, homePageCanvas, username, level, updateHomeWindow)
        homePageCanvas.pack_forget()

    def openLevelFour():
        level_four.levelFour(root, homePageCanvas, username, level, updateHomeWindow)
        homePageCanvas.pack_forget()

    def openLevelFive():
        level_five.levelFive(root, homePageCanvas, username, level, updateHomeWindow)
        homePageCanvas.pack_forget()

    def openLevelSix():
        level_six.levelSix(root, homePageCanvas, username, level, updateHomeWindow)
        homePageCanvas.pack_forget()

    def openLevelSeven():
        level_seven.levelSeven(root, homePageCanvas, username, level, updateHomeWindow)
        homePageCanvas.pack_forget()

    def openLevelEight():
        level_eight.levelEight(root, homePageCanvas, username, level, updateHomeWindow)
        homePageCanvas.pack_forget()

    def openLevelNine():
        level_nine.levelNine(root, homePageCanvas, username, level, updateHomeWindow)
        homePageCanvas.pack_forget()

    def logOutCommand():
        global username
        global password
        username = ""
        password = ""
        usernameEntry.delete(0, customtkinter.END)
        passwordEntry.delete(0, customtkinter.END)
        homePageCanvas.destroy()
        canvas1.pack()

    def wordFlash(count):
        if not homePageCanvas.winfo_exists():
            return
        wordArray = ["Discover", "Learn", "Grow", "Explore", "Imagine"]
        if count < len(wordArray):
            motivateWord.configure(text=wordArray[count])
            root.after(1000, wordFlash, count + 1)
        else:
            root.after(1000, wordFlash, 0)

    # --- Load images safely ---
    secondPageImagePath = os.path.join(DRAWABLES_DIR, "secondpagebackground1.png")
    secondPageImage = Image.open(secondPageImagePath).resize((1080, 720), Image.LANCZOS)
    secondPageImage = ImageTk.PhotoImage(secondPageImage)

    def openSecondPage():
        second_page.secondPageWindow(root, secondPageImage, canvas1, username, updateHomeWindow)
        homePageCanvas.pack_forget()

    homePageCanvas = tk.Canvas(root, width=1080, height=720)
    homePageCanvas.create_image(0, 0, anchor=tk.NW, image=firstPageImage)
    homePageCanvas.pack()

    motivateWord = customtkinter.CTkLabel(homePageCanvas, text="Level: " + str(level),
                                          font=("Comic Sans MS", 20),
                                          bg_color="#41c457",
                                          text_color="#ffffff")
    motivateWord.place(relx=0.170, rely=0.68)

    levelText = customtkinter.CTkLabel(homePageCanvas, text="Level: " + str(level),
                                       font=("Comic Sans MS", 20),
                                       text_color="#fd6909")
    levelText.place(relx=0.90, rely=0.01)

    wordFlash(0)

    usernameText = customtkinter.CTkLabel(homePageCanvas, text=username,
                                          font=("Comic Sans MS", 20),
                                          text_color="#fd6909")
    usernameText.place(relx=0.83, rely=0.01)

    logout_Button = customtkinter.CTkButton(homePageCanvas, text="Log-out",
                                            font=("Comic Sans MS", 20),
                                            text_color="white",
                                            hover_color="#b14802",
                                            fg_color="#fd6909",
                                            corner_radius=40,
                                            bg_color="#1395e8",
                                            width=15, height=15,
                                            command=logOutCommand)
    logout_Button.place(relx=0.01, rely=0.01)

    nextPageIconPath = os.path.join(DRAWABLES_DIR, "nextpagearrow.png")
    nextPageIcon = customtkinter.CTkImage(Image.open(nextPageIconPath))
    nextPageButton = customtkinter.CTkButton(homePageCanvas, text="",
                                             font=("Comic Sans MS", 30),
                                             image=nextPageIcon,
                                             bg_color="#41c457",
                                             text_color="white",
                                             corner_radius=10,
                                             hover_color="#b14802",
                                             fg_color="#2b2d30",
                                             state="DISABLED",
                                             width=20, height=30)
    nextPageButton.place(relx=0.94, rely=0.450)

    # --- Level buttons ---
    aLevel = customtkinter.CTkButton(homePageCanvas, text="Aa",
                                     font=("Comic Sans MS", 20),
                                     text_color="white",
                                     corner_radius=10,
                                     hover_color="#b14802",
                                     bg_color="#1395e8",
                                     fg_color="#fd6909",
                                     width=50, height=40, command=openLevelOne)
    aLevel.place(relx=0.03, rely=0.34)

    bLevel = customtkinter.CTkButton(homePageCanvas, text="Bb",
                                     font=("Comic Sans MS", 20),
                                     text_color="white",
                                     corner_radius=10,
                                     hover_color="#b14802",
                                     fg_color=locked,
                                     bg_color="#41c457",
                                     width=50, height=40, state="DISABLED")
    bLevel.place(relx=0.150, rely=0.43)

    cLevel = customtkinter.CTkButton(homePageCanvas, text="Cc",
                                     font=("Comic Sans MS", 20),
                                     text_color="white",
                                     corner_radius=10,
                                     hover_color="#b14802",
                                     bg_color="#1395e8",
                                     fg_color=locked,
                                     width=50, height=40, state="DISABLED")
    cLevel.place(relx=0.3, rely=0.38)

    dLevel = customtkinter.CTkButton(homePageCanvas, text="Dd",
                                     font=("Comic Sans MS", 20),
                                     text_color="white",
                                     corner_radius=10,
                                     hover_color="#b14802",
                                     fg_color=locked,
                                     bg_color="#41c457",
                                     width=50, height=40, state="DISABLED")
    dLevel.place(relx=0.350, rely=0.59)

    eLevel = customtkinter.CTkButton(homePageCanvas, text="Ee",
                                     font=("Comic Sans MS", 20),
                                     text_color="white",
                                     corner_radius=10,
                                     hover_color="#b14802",
                                     fg_color=locked,
                                     bg_color="#1395e8",
                                     width=50, height=40, state="DISABLED")
    eLevel.place(relx=0.5, rely=0.49)

    fLevel = customtkinter.CTkButton(homePageCanvas, text="Ff",
                                     font=("Comic Sans MS", 20),
                                     text_color="white",
                                     corner_radius=10,
                                     hover_color="#b14802",
                                     fg_color=locked,
                                     bg_color="#41c457",
                                     width=50, height=40, state="DISABLED")
    fLevel.place(relx=0.570, rely=0.75)

    gLevel = customtkinter.CTkButton(homePageCanvas, text="Gg",
                                     font=("Comic Sans MS", 20),
                                     text_color="white",
                                     corner_radius=10,
                                     hover_color="#b14802",
                                     fg_color=locked,
                                     bg_color="#1395e8",
                                     width=50, height=40, state="DISABLED")
    gLevel.place(relx=0.7, rely=0.69)

    hLevel = customtkinter.CTkButton(homePageCanvas, text="Hh",
                                     font=("Comic Sans MS", 20),
                                     text_color="white",
                                     corner_radius=10,
                                     hover_color="#b14802",
                                     fg_color=locked,
                                     bg_color="#41c457",
                                     width=50, height=40, state="DISABLED")
    hLevel.place(relx=0.845, rely=0.65)

    iLevel = customtkinter.CTkButton(homePageCanvas, text="Ii",
                                     font=("Comic Sans MS", 20),
                                     text_color="white",
                                     corner_radius=10,
                                     hover_color="#b14802",
                                     bg_color="#1395e8",
                                     fg_color=locked,
                                     width=50, height=40, state="DISABLED")
    iLevel.place(relx=0.790, rely=0.40)

    lastConvert = int(convertLevel)
    if lastConvert >= 2:
        bLevel.configure(state="normal", command=openLevelTwo, fg_color="#fd6909")
    if lastConvert >= 3:
        cLevel.configure(state="normal", command=openLevelThree, fg_color="#fd6909")
    if lastConvert >= 4:
        dLevel.configure(state="normal", command=openLevelFour, fg_color="#fd6909")
    if lastConvert >= 5:
        eLevel.configure(state="normal", command=openLevelFive, fg_color="#fd6909")
    if lastConvert >= 6:
        fLevel.configure(state="normal", command=openLevelSix, fg_color="#fd6909")
    if lastConvert >= 7:
        gLevel.configure(state="normal", command=openLevelSeven, fg_color="#fd6909")
    if lastConvert >= 8:
        hLevel.configure(state="normal", command=openLevelEight, fg_color="#fd6909")
    if lastConvert >= 9:
        iLevel.configure(state="normal", command=openLevelNine, fg_color="#fd6909")
    if lastConvert >= 10:
        nextPageButton.configure(state="normal", command=openSecondPage, fg_color="#fd6909")
