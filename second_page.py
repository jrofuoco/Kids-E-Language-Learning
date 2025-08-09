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
import third_page
import DatabaseHelper


locked = "#2b2d30"
unlocked = "#fd6909"



def secondPageWindow(root, firstPageImage, canvas1, username, updateHomeWindow):
    global level
    level = DatabaseHelper.getLevel(username)
    print(level)
    convertLevel = str(level)

    def updateSecondPageWindow():
        global level
        level = DatabaseHelper.getLevel(username)
        print(level)
        convertLevel = str(level)
        levelText.configure(text="Level: " + level)

        if convertLevel == "11":
            kLevel.configure(state="normal", command=openLevelEleven)
            kLevel.configure(fg_color="#fd6909")

        if convertLevel == "12":
            lLevel.configure(state="normal", command=openLevelTwelve)
            lLevel.configure(fg_color="#fd6909")

        if convertLevel == "13":
            mLevel.configure(state="normal", command=openLevelThirteen)
            mLevel.configure(fg_color="#fd6909")

        if convertLevel == "14":
            nLevel.configure(state="normal", command=openLevelFourteen)
            nLevel.configure(fg_color="#fd6909")

        if convertLevel == "15":
            oLevel.configure(state="normal", command=openLevelFifteen)
            oLevel.configure(fg_color="#fd6909")

        if convertLevel == "16":
            pLevel.configure(state="normal", command=openLevelSixteen)
            pLevel.configure(fg_color="#fd6909")

        if convertLevel == "17":
            qLevel.configure(state="normal", command=openLevelSeventeen)
            qLevel.configure(fg_color="#fd6909")

        if convertLevel == "18":
            rLevel.configure(state="normal", command=openLevelEighteen)
            rLevel.configure(fg_color="#fd6909")
        if convertLevel == "19":
            nextPageButton.configure(state="normal", command=openThirdPage, fg_color="#fd6909")

        secondPageCanvas.pack()

    def openLevelTen():
        level_ten.levelTen(root, secondPageCanvas, username, level, updateSecondPageWindow)
        secondPageCanvas.pack_forget()

    def openLevelEleven():
        level_eleven.levelEleven(root, secondPageCanvas, username, level, updateSecondPageWindow)
        secondPageCanvas.pack_forget()

    def openLevelTwelve():
        level_twelve.levelTwelve(root, secondPageCanvas, username, level, updateSecondPageWindow)
        secondPageCanvas.pack_forget()

    def openLevelThirteen():
        level_thirteen.levelThirteen(root, secondPageCanvas, username, level, updateSecondPageWindow)
        secondPageCanvas.pack_forget()

    def openLevelFourteen():
        level_fourteen.levelFourteen(root, secondPageCanvas, username, level, updateSecondPageWindow)
        secondPageCanvas.pack_forget()

    def openLevelFifteen():
        level_fifteen.levelFifteen(root, secondPageCanvas, username, level, updateSecondPageWindow)
        secondPageCanvas.pack_forget()

    def openLevelSixteen():
        level_sixteen.levelSixteen(root, secondPageCanvas, username, level, updateSecondPageWindow)
        secondPageCanvas.pack_forget()

    def openLevelSeventeen():
        level_seventeen.levelSeventeen(root, secondPageCanvas, username, level, updateSecondPageWindow)
        secondPageCanvas.pack_forget()

    def openLevelEighteen():
        level_eighteen.levelEighteen(root, secondPageCanvas, username, level, updateSecondPageWindow)
        secondPageCanvas.pack_forget()

    def logOutCommand():
        updateHomeWindow()
        secondPageCanvas.destroy()

    def openThirdPage():
        third_page.thirdPageWindow(root, background, canvas1, username, updateSecondPageWindow)
        secondPageCanvas.pack_forget()

    bacgkrdounaImagePath = "C:\\Users\\Fuoco\\PycharmProjects\\pythonProject\\.venv\\drawables\\backgroundthirdpage1.png"
    background = Image.open(bacgkrdounaImagePath)
    background = background.resize((1080, 720), Image.FIXED)
    background = ImageTk.PhotoImage(background)

    secondPageCanvas = tk.Canvas(root, width=1080, height=720)
    secondPageCanvas.create_image(0, 0, anchor=tk.NW, image=firstPageImage)
    secondPageCanvas.pack()

    levelText = customtkinter.CTkLabel(secondPageCanvas, text="Level: " + level,
                                       font=("Comic Sans MS", 20),
                                       text_color="#fd6909")
    levelText.place(relx=0.90, rely=0.01)

    #----------------------------------USER---------------------------
    usernameText = customtkinter.CTkLabel(secondPageCanvas, text=username,
                                       font=("Comic Sans MS", 20),
                                       text_color="#fd6909")
    usernameText.place(relx=0.83, rely=0.01)

    logout_Button = customtkinter.CTkButton(secondPageCanvas, text="Back",
                                          font=("Comic Sans MS", 20),
                                          text_color="white",
                                          corner_radius=40,
                                          hover_color="#b14802",
                                          fg_color="#fd6909",
                                            bg_color="#1395e8",
                                            width=15, height=15,

                                          command=logOutCommand).place(relx=0.01, rely=0.01)

    nextPageIcon = customtkinter.CTkImage(Image.open("C:\\Users\\Fuoco\\PycharmProjects\\pythonProject\\.venv\\drawables\\nextpagearrow.png"))
    nextPageButton = customtkinter.CTkButton(secondPageCanvas, text="",
                                          font=("Comic Sans MS", 30),
                                             image=nextPageIcon,
                                          text_color="white",
                                          corner_radius=10,
                                          hover_color="#b14802",
                                             bg_color="#1395e8",
                                             fg_color="#2b2d30",
                                          state="DISABLED",
                                          width=20, height=30,
                                          )
    nextPageButton.place(relx=0.94, rely=0.39)


    # ----------------------OPEN LEVELS-------------------------

    # ----------------------------------------------------------

   #METHODS TO UNLOCKED THE OTHER LEVELS
    def isjLevelComplete():
        kLevel.configure(fg_color=unlocked, state="normal")
        levelText.configure(text="Level 2")

    #-------------------------------LEVEL 1---------------------------------
    jLevel = customtkinter.CTkButton(secondPageCanvas, text="Jj",
                                          font=("Comic Sans MS", 20),
                                          text_color="white",
                                          corner_radius=10,
                                          hover_color="#b14802",
                                          fg_color="#fd6909",
                                     bg_color="#1395e8",
                                     width=50, height=40, command=openLevelTen).place(relx=0.03, rely=0.27)

    #-----------------------------------------------------------------------

    kLevel = customtkinter.CTkButton(secondPageCanvas, text="Kk",
                                     font=("Comic Sans MS", 20),
                                     text_color="white",
                                     corner_radius=10,
                                     hover_color="#b14802",
                                     fg_color="#2b2d30",
                                     bg_color="#41c457",
                                     width=50, height=40)
    kLevel.place(relx=0.05, rely=0.45)
    kLevel.configure(state="DISABLED")

    lLevel = customtkinter.CTkButton(secondPageCanvas, text="Ll",
                                     font=("Comic Sans MS", 20),
                                     text_color="white",
                                     corner_radius=10,
                                     hover_color="#b14802",
                                     fg_color="#2b2d30",
                                     bg_color="#1395e8",
                                     width=50, height=40)
    lLevel.place(relx=0.180, rely=0.5)
    lLevel.configure(state="DISABLED")

    mLevel = customtkinter.CTkButton(secondPageCanvas, text="Mm",
                                     font=("Comic Sans MS", 20),
                                     text_color="white",
                                     corner_radius=10,
                                     hover_color="#b14802",
                                     fg_color="#2b2d30",
                                     bg_color="#41c457",
                                     width=50, height=40)
    mLevel.place(relx=0.11, rely=0.69)
    mLevel.configure(state="DISABLED")

    nLevel = customtkinter.CTkButton(secondPageCanvas, text="Nn",
                                     font=("Comic Sans MS", 20),
                                     text_color="white",
                                     corner_radius=10,
                                     hover_color="#b14802",
                                     fg_color="#2b2d30",
                                     bg_color="#1395e8",
                                     width=50, height=40)
    nLevel.place(relx=0.3, rely=0.64)
    nLevel.configure(state="DISABLED")

    oLevel = customtkinter.CTkButton(secondPageCanvas, text="Oo",
                                     font=("Comic Sans MS", 20),
                                     text_color="white",
                                     corner_radius=10,
                                     hover_color="#b14802",
                                     fg_color="#2b2d30",
                                     bg_color="#41c457",
                                     width=50, height=40)
    oLevel.place(relx=0.48, rely=0.63)
    oLevel.configure(state="DISABLED")

    pLevel = customtkinter.CTkButton(secondPageCanvas, text="Pp",
                                     font=("Comic Sans MS", 20),
                                     text_color="white",
                                     corner_radius=10,
                                     hover_color="#b14802",
                                     fg_color="#2b2d30",
                                     bg_color="#1395e8",
                                     width=50, height=40)
    pLevel.place(relx=0.620, rely=0.41)
    pLevel.configure(state="DISABLED")

    qLevel = customtkinter.CTkButton(secondPageCanvas, text="Qq",
                                     font=("Comic Sans MS", 20),
                                     text_color="white",
                                     corner_radius=10,
                                     hover_color="#b14802",
                                     fg_color="#2b2d30",
                                     bg_color="#41c457",
                                     width=50, height=40)
    qLevel.place(relx=0.750, rely=0.47)
    qLevel.configure(state="DISABLED")

    rLevel = customtkinter.CTkButton(secondPageCanvas, text="Rr",
                                     font=("Comic Sans MS", 20),
                                     text_color="white",
                                     corner_radius=10,
                                     hover_color="#b14802",
                                     fg_color="#2b2d30",
                                     bg_color="#1395e8",
                                     width=50, height=40)
    rLevel.place(relx=0.840, rely=0.3)
    rLevel.configure(state="DISABLED")

    lastConvert = int(convertLevel)
    if lastConvert >= 11:
        kLevel.configure(state="normal", command=openLevelEleven)
        kLevel.configure(fg_color="#fd6909")
    if lastConvert >= 12:
        lLevel.configure(state="normal", command=openLevelTwelve)
        lLevel.configure(fg_color="#fd6909")
    if lastConvert >= 13:
        mLevel.configure(state="normal", command=openLevelThirteen)
        mLevel.configure(fg_color="#fd6909")
    if lastConvert >= 14:
        nLevel.configure(state="normal", command=openLevelFourteen)
        nLevel.configure(fg_color="#fd6909")
    if lastConvert >= 15:
        oLevel.configure(state="normal", command=openLevelFifteen)
        oLevel.configure(fg_color="#fd6909")
    if lastConvert >= 16:
        pLevel.configure(state="normal", command=openLevelSixteen)
        pLevel.configure(fg_color="#fd6909")
    if lastConvert >= 17:
        qLevel.configure(state="normal", command=openLevelSeventeen)
        qLevel.configure(fg_color="#fd6909")
    if lastConvert >= 18:
        rLevel.configure(state="normal", command=openLevelEighteen)
        rLevel.configure(fg_color="#fd6909")
    if lastConvert >= 19:
        nextPageButton.configure(state="normal", command=openThirdPage, fg_color="#fd6909")
