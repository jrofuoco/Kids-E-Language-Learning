import tkinter as tk
import warnings
import pygame

import customtkinter
from PIL import Image, ImageTk
import DatabaseHelper

def levelSeventeen(root, homePageCanvas, username, user, go_back_function):
    print(user)
    print("openlevelone")
    global stage
    stage = 1

    pygame.mixer.init()

    image_path = "C:\\Users\\Fuoco\\PycharmProjects\\pythonProject\\.venv\\drawables\\levelbackground1.png"
    background = Image.open(image_path)
    background = background.resize((1080, 720), Image.FIXED)
    background = ImageTk.PhotoImage(background)

    levelSeventeenpage = tk.Canvas(root, width=1080, height=720)
    levelSeventeenpage.create_image(0, 0, anchor=tk.NW, image=background)
    levelSeventeenpage.image = background
    levelSeventeenpage.after(100, levelSeventeenpage.pack)

    speakerIcon = Image.open("C:\\Users\\Fuoco\\PycharmProjects\\pythonProject\\.venv\\drawables\\speaker.png")
    speakerIcon = speakerIcon.resize((speakerIcon.width // 2, speakerIcon.height // 2))
    speakerIcon = ImageTk.PhotoImage(speakerIcon)
    global image
    image = Image.open("C:\\Users\\Fuoco\\PycharmProjects\\pythonProject\\.venv\\drawables\\queen.png")
    resized_image1 = image.resize((image.width // 8, image.height // 8))
    imagetk = ImageTk.PhotoImage(resized_image1)

    banana = customtkinter.CTkLabel(levelSeventeenpage,
                                        text="",
                                        fg_color="#ffffff",
                                        image=imagetk).place(relx=0.50, rely=0.30, anchor=customtkinter.CENTER)

    spellTheWord = customtkinter.CTkLabel(levelSeventeenpage,
                                          text="Spell The Word",
                                          text_color="#fd6909",
                                          fg_color="#ffffff",
                                          font=("Comic Sans MS", 24)).place(relx=0.5, rely=0.67 , anchor=tk.CENTER)

    usernameText = customtkinter.CTkLabel(levelSeventeenpage, text=username,
                                          font=("Comic Sans MS", 20),
                                          text_color="#fd6909")
    usernameText.place(relx=0.83, rely=0.01)

    levelText = customtkinter.CTkLabel(levelSeventeenpage, text="Level: 17",
                                       font=("Comic Sans MS", 20),
                                       text_color="#fd6909")
    levelText.place(relx=0.90, rely=0.01)

    def twoNext():
        nextImage = "questionmark.png"
        image = Image.open("C:\\Users\\Fuoco\\PycharmProjects\\pythonProject\\.venv\\drawables\\" + nextImage)
        resized_image1 = image.resize((image.width // 6, image.height // 6))
        airplane = ImageTk.PhotoImage(resized_image1)
        if stage == 2:
            airplaneImage = customtkinter.CTkLabel(levelSeventeenpage,
                                                   text="",
                                                   fg_color="#ffffff",
                                                   image=airplane).place(relx=0.50, rely=0.30,
                                                                         anchor=customtkinter.CENTER)
        elif stage == 3:
            nextImage = "quite.png"
            image = Image.open("C:\\Users\\Fuoco\\PycharmProjects\\pythonProject\\.venv\\drawables\\" + nextImage)
            resized_image = image.resize((image.width // 6, image.height // 6))
            arrow = ImageTk.PhotoImage(resized_image)

            arrow = customtkinter.CTkLabel(levelSeventeenpage,
                                           text="",
                                           fg_color="#ffffff",
                                           image=arrow).place(relx=0.50, rely=0.30, anchor=customtkinter.CENTER)

    def playAppleVoice():
        print(stage)
        if stage == 1:
            pygame.mixer.music.load("C:\\Users\\Fuoco\\PycharmProjects\\pythonProject\\.venv\\drawables\\queenvoice.wav")
            pygame.mixer.music.play(loops=0)
        elif stage == 2:
            pygame.mixer.music.load("C:\\Users\\Fuoco\\PycharmProjects\\pythonProject\\.venv\\drawables\\questionmarkvoice.wav")
            pygame.mixer.music.play(loops=0)
        elif stage == 3:
            pygame.mixer.music.load("C:\\Users\\Fuoco\\PycharmProjects\\pythonProject\\.venv\\drawables\\quitevoice.wav")
            pygame.mixer.music.play(loops=0)

    levelComplete = customtkinter.CTkLabel(levelSeventeenpage,
                                           text="Level Complete",
                                           text_color="#fd6909",
                                           fg_color="#ffffff",
                                           font=("Comic Sans MS", 24))

    def next():
        global stage
        answer = answerEntry.get()
        answer = answer.lower()
        if answer == "queen":
            answerEntry.delete(0, tk.END)
            stage = 2
            levelSeventeenpage.after(100, twoNext)
        elif answer == "question mark":
            answerEntry.delete(0, tk.END)
            stage = 3
            levelSeventeenpage.after(100, twoNext)
        elif answer == "quiet":
            levelComplete.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
            level = 18
            users = int(user)
            if level > users:
                DatabaseHelper.updateLevel(username, level)
            count_down(3)
        else:
            displayWrongAnswer(3)

    def displayWrongAnswer(count):
        wrongAnswer.configure(text_color="#ff0000")
        if count > 0:
            root.after(200, displayWrongAnswer, count - 1)
        else:
            wrongAnswer.configure(text_color="#ffffff")

    wrongAnswer = customtkinter.CTkLabel(levelSeventeenpage,
                                         text="Wrong Answer!",
                                         text_color="#ffffff",
                                       fg_color="#ffffff",
                                       font=("Comic Sans MS", 24))
    wrongAnswer.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    def count_down(count):
        countDown.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
        if count > 0:
            stringCount = str(count)
            countDown.configure(text="Going Back in " + stringCount)
            root.after(800, count_down, count - 1)
        else:
            levelSeventeenpage.destroy()
            go_back_function()

    countDown = customtkinter.CTkLabel(levelSeventeenpage,
                                       text="asd",
                                       text_color="#fd6909",
                                       fg_color="#ffffff",
                                       font=("Comic Sans MS", 24))
    #--------------------------------ENTRYBOXES------------------------------------
    answerEntry = customtkinter.CTkEntry(levelSeventeenpage, placeholder_text="?",
                                           border_color="#b14802",
                                            font=("Comic Sans MS", 20),
                                           width=200, height=40,
                                           justify='center',
                                           fg_color="#f0f0f0", text_color="#fd6909")
    answerEntry.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

    # --------------------------------ENTER BUTTONS---------------------------------
    enterButton = customtkinter.CTkButton(levelSeventeenpage, text="Enter",
                                         font=("Comic Sans MS", 20),
                                         text_color="white",
                                         corner_radius=10,
                                         hover_color="#b14802",
                                         fg_color="#fd6909",
                                         width=200, height=30,
                                         command=next).place(relx=0.5, rely=0.83, anchor=tk.CENTER)

    #--------------------------------PLAY VOICES-----------------------------------
    playAppleVoiceButton = customtkinter.CTkButton(levelSeventeenpage, text="Play",
                                         font=("Comic Sans MS", 20),
                                         text_color="white",
                                         image=speakerIcon,
                                         corner_radius=10,
                                         hover_color="#b14802",
                                         fg_color="#fd6909",
                                         width=30, height=15,
                                         command=playAppleVoice).place(relx=0.445, rely=0.50)
    #-----------------------------------------------------------------------------------------
    def backButton():
        levelSeventeenpage.destroy()
        print("Back Button From Level 1")
        go_back_function()
    backButton = customtkinter.CTkButton(levelSeventeenpage, text="Back",
                                         font=("Comic Sans MS", 20),
                                         text_color="white",
                                         corner_radius=10,
                                         hover_color="#b14802",
                                         fg_color="#fd6909", width=15,
                                         height=15, command=backButton).place(relx=0.03, rely=0.04)