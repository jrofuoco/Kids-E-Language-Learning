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
import level_ten
import level_eleven
import level_twelve
import level_thirteen
import level_fourteen
import level_fifteen
import level_sixteen
import level_seventeen
import level_eighteen
import level_nineteen
import level_twenty
import level_twentyone
import level_twentytwo
import level_twentythree
import level_twentyfour
import level_twentyfive
import level_twentysix
import DatabaseHelper


locked = "#2b2d30"
unlocked = "#fd6909"

def thirdPageWindow(root, firstPageImage, canvas1, username, updateSecondPageWindow):
    global level
    level = DatabaseHelper.getLevel(username)
    print(level)
    convertLevel = str(level)

    def updatethirdPageWindow():
        global level
        level = DatabaseHelper.getLevel(username)
        print(level)
        convertLevel = str(level)
        levelText.configure(text="Level: " + level)

        if convertLevel == "20":
            tLevel.configure(state="normal", command=openLevelTwenty)
            tLevel.configure(fg_color="#fd6909")

        if convertLevel == "21":
            uLevel.configure(state="normal", command=openLevelTwentyOne)
            uLevel.configure(fg_color="#fd6909")

        if convertLevel == "22":
            vLevel.configure(state="normal", command=openLevelTwentyTwo)
            vLevel.configure(fg_color="#fd6909")

        if convertLevel == "23":
            wLevel.configure(state="normal", command=openLevelTwentyThree)
            wLevel.configure(fg_color="#fd6909")

        if convertLevel == "24":
            xLevel.configure(state="normal", command=openLevelTwentyFour)
            xLevel.configure(fg_color="#fd6909")

        if convertLevel == "25":
            yLevel.configure(state="normal", command=openLevelTwentyFive)
            yLevel.configure(fg_color="#fd6909")

        if convertLevel == "26":
            zLevel.configure(state="normal", command=openLevelTwentySix)
            zLevel.configure(fg_color="#fd6909")

        thirdPageCanvas.pack()

    def openLevelNineteen():
        level_nineteen.levelNineteen(root, thirdPageCanvas, username, level, updatethirdPageWindow)
        thirdPageCanvas.pack_forget()

    def openLevelTwenty():
        level_twenty.levelTwenty(root, thirdPageCanvas, username, level, updatethirdPageWindow)
        thirdPageCanvas.pack_forget()

    def openLevelTwentyOne():
        level_twentyone.levelTwentyOne(root, thirdPageCanvas, username, level, updatethirdPageWindow)
        thirdPageCanvas.pack_forget()

    def openLevelTwentyTwo():
        level_twentytwo.levelTwentyTwo(root, thirdPageCanvas, username, level, updatethirdPageWindow)
        thirdPageCanvas.pack_forget()

    def openLevelTwentyThree():
        level_twentythree.levelTwentyThree(root, thirdPageCanvas, username, level, updatethirdPageWindow)
        thirdPageCanvas.pack_forget()

    def openLevelTwentyFour():
        level_twentyfour.levelTwentyFour(root, thirdPageCanvas, username, level, updatethirdPageWindow)
        thirdPageCanvas.pack_forget()

    def openLevelTwentyFive():
        thirdPageCanvas.pack_forget()
        level_twentyfive.levelTwentyFive(root, thirdPageCanvas, username, level, updatethirdPageWindow)

    def openLevelTwentySix():
        level_twentysix.levelTwentySix(root, thirdPageCanvas, username, level, updatethirdPageWindow)
        thirdPageCanvas.pack_forget()

    def opewLevelEighteen():
        level_eighteen.levelEighteen(root, thirdPageCanvas, username, level, updatethirdPageWindow)
        thirdPageCanvas.pack_forget()

    def logOutCommand():
        updateSecondPageWindow()
        thirdPageCanvas.destroy()

    thirdPageCanvas = tk.Canvas(root, width=1080, height=720)
    thirdPageCanvas.create_image(0, 0, anchor=tk.NW, image=firstPageImage)
    thirdPageCanvas.pack()

    levelText = customtkinter.CTkLabel(thirdPageCanvas, text="Level: " + level,
                                       font=("Comic Sans MS", 20),
                                       text_color="#fd6909")
    levelText.place(relx=0.90, rely=0.01)

    #----------------------------------USER---------------------------
    usernameText = customtkinter.CTkLabel(thirdPageCanvas, text=username,
                                       font=("Comic Sans MS", 20),
                                       text_color="#fd6909")
    usernameText.place(relx=0.83, rely=0.01)

    logout_Button = customtkinter.CTkButton(thirdPageCanvas, text="Back",
                                          font=("Comic Sans MS", 20),
                                          text_color="white",
                                          corner_radius=40,
                                          hover_color="#b14802",
                                          fg_color="#fd6909",
                                            bg_color="#1395e8",
                                          width=15, height=15,
                                          command=logOutCommand).place(relx=0.01, rely=0.01)


    # ----------------------OPEN LEVELS-------------------------

    # ----------------------------------------------------------

   #METHODS TO UNLOCKED THE OTHER LEVELS
    def issLevelComplete():
        tLevel.configure(fg_color=unlocked, state="normal")
        levelText.configure(text="Level 2")

    #-------------------------------LEVEL 1---------------------------------
    sLevel = customtkinter.CTkButton(thirdPageCanvas, text="Ss",
                                          font=("Comic Sans MS", 20),
                                          text_color="white",
                                          corner_radius=10,
                                          hover_color="#b14802",
                                          fg_color="#fd6909",
                                     bg_color="#1395e8",
                                          width=50, height=40, command=openLevelNineteen).place(relx=0.03, rely=0.24)

    #-----------------------------------------------------------------------

    tLevel = customtkinter.CTkButton(thirdPageCanvas, text="Tt",
                                     font=("Comic Sans MS", 20),
                                     text_color="white",
                                     corner_radius=10,
                                     hover_color="#b14802",
                                     fg_color="#2b2d30",
                                     bg_color="#41c457",
                                     width=50, height=40)
    tLevel.place(relx=0.180, rely=0.3)
    tLevel.configure(state="DISABLED")

    uLevel = customtkinter.CTkButton(thirdPageCanvas, text="Uu",
                                     font=("Comic Sans MS", 20),
                                     text_color="white",
                                     corner_radius=10,
                                     hover_color="#b14802",
                                     fg_color="#2b2d30",
                                     bg_color="#1395e8",
                                     width=50, height=40)
    uLevel.place(relx=0.28, rely=0.17)
    uLevel.configure(state="DISABLED")

    vLevel = customtkinter.CTkButton(thirdPageCanvas, text="Vv",
                                     font=("Comic Sans MS", 20),
                                     text_color="white",
                                     corner_radius=10,
                                     hover_color="#b14802",
                                     fg_color="#2b2d30",
                                     bg_color="#41c457",
                                     width=50, height=40)
    vLevel.place(relx=0.38, rely=0.32)
    vLevel.configure(state="DISABLED")

    wLevel = customtkinter.CTkButton(thirdPageCanvas, text="Ww",
                                     font=("Comic Sans MS", 20),
                                     text_color="white",
                                     corner_radius=10,
                                     hover_color="#b14802",
                                     fg_color="#2b2d30",
                                     bg_color="#1395e8",
                                     width=50, height=40)
    wLevel.place(relx=0.53, rely=0.27)
    wLevel.configure(state="DISABLED")

    xLevel = customtkinter.CTkButton(thirdPageCanvas, text="Xx",
                                     font=("Comic Sans MS", 20),
                                     text_color="white",
                                     corner_radius=10,
                                     hover_color="#b14802",
                                     fg_color="#2b2d30",
                                     bg_color="#41c457",
                                     width=50, height=40)
    xLevel.place(relx=0.55, rely=0.48)
    xLevel.configure(state="DISABLED")

    yLevel = customtkinter.CTkButton(thirdPageCanvas, text="Yy",
                                     font=("Comic Sans MS", 20),
                                     text_color="white",
                                     corner_radius=10,
                                     hover_color="#b14802",
                                     fg_color="#2b2d30",
                                     bg_color="#1395e8",
                                     width=50, height=40)
    yLevel.place(relx=0.73, rely=0.55)
    yLevel.configure(state="DISABLED")

    zLevel = customtkinter.CTkButton(thirdPageCanvas, text="Zz",
                                     font=("Comic Sans MS", 20),
                                     text_color="white",
                                     corner_radius=10,
                                     hover_color="#b14802",
                                     fg_color="#2b2d30",
                                     bg_color="#a43d1e",
                                     width=50, height=40)
    zLevel.place(relx=0.822, rely=0.805)
    zLevel.configure(state="DISABLED")

    lastConvert = int(convertLevel)
    if lastConvert >= 20:
        tLevel.configure(state="normal", command=openLevelTwenty)
        tLevel.configure(fg_color="#fd6909")
    if lastConvert >= 21:
        uLevel.configure(state="normal", command=openLevelTwentyOne)
        uLevel.configure(fg_color="#fd6909")
    if lastConvert >= 22:
        vLevel.configure(state="normal", command=openLevelTwentyTwo)
        vLevel.configure(fg_color="#fd6909")
    if lastConvert >= 23:
        wLevel.configure(state="normal", command=openLevelTwentyThree)
        wLevel.configure(fg_color="#fd6909")
    if lastConvert >= 24:
        xLevel.configure(state="normal", command=openLevelTwentyFour)
        xLevel.configure(fg_color="#fd6909")
    if lastConvert >= 25:
        yLevel.configure(state="normal", command=openLevelTwentyFive)
        yLevel.configure(fg_color="#fd6909")
    if lastConvert >= 26:
        zLevel.configure(state="normal", command=openLevelTwentySix)
        zLevel.configure(fg_color="#fd6909")

