import os
import tkinter as tk
import pygame
import customtkinter
from customtkinter import CTkImage
from PIL import Image
import DatabaseHelper

# ---------- Paths ----------
BASE_DIR = os.path.dirname(__file__)
DRAWABLES_DIR = os.path.join(BASE_DIR, "drawables")


def levelOne(root, homePageCanvas, username, user, go_back_function):
    print(user)
    print("openlevelone")
    global stage
    stage = 1

    pygame.mixer.init()

    # Main container frame
    levelOnePage = customtkinter.CTkFrame(root, width=1080, height=720)
    levelOnePage.pack(fill="both", expand=True)

    # --- Load background ---
    bg_img = Image.open(os.path.join(DRAWABLES_DIR, "levelbackground1.png")).resize((1080, 720), Image.LANCZOS)
    bg_image = CTkImage(light_image=bg_img, dark_image=bg_img, size=(1080, 720))

    background_label = customtkinter.CTkLabel(levelOnePage, text="", image=bg_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # --- Speaker icon ---
    speaker_img = Image.open(os.path.join(DRAWABLES_DIR, "speaker.png"))
    speaker_img = speaker_img.resize((speaker_img.width // 2, speaker_img.height // 2))
    speakerIcon = CTkImage(light_image=speaker_img, dark_image=speaker_img)

    # --- Apple image (larger via CTkImage size) ---
    apple_img = Image.open(os.path.join(DRAWABLES_DIR, "apple.png"))
    # Pick the final on-screen size you want (adjust as needed)
    appleCTkImage = CTkImage(light_image=apple_img, dark_image=apple_img, size=(240, 240))

    appleImage = customtkinter.CTkLabel(
        levelOnePage,
        text="",
        fg_color="#ffffff",
        image=appleCTkImage
    )
    appleImage.place(relx=0.50, rely=0.30, anchor=customtkinter.CENTER)

    # keep a reference to prevent garbage collection
    levelOnePage.apple_image_ref = appleCTkImage

    spellTheWord = customtkinter.CTkLabel(
        levelOnePage,
        text="Spell The Word",
        text_color="#fd6909",
        fg_color="#ffffff",
        font=("Comic Sans MS", 24)
    )
    spellTheWord.place(relx=0.5, rely=0.67, anchor=tk.CENTER)

    usernameText = customtkinter.CTkLabel(
        levelOnePage, text=username,
        font=("Comic Sans MS", 20),
        text_color="#fd6909",
        fg_color="#ffffff"
    )
    usernameText.place(relx=0.83, rely=0.01)

    levelText = customtkinter.CTkLabel(
        levelOnePage, text="Level: 1",
        font=("Comic Sans MS", 20),
        text_color="#fd6909",
        fg_color="#ffffff"
    )
    levelText.place(relx=0.90, rely=0.01)

    def airplaneF():
        if stage == 2:
            airplane_img = Image.open(os.path.join(DRAWABLES_DIR, "airplane.png"))
            resized_image1 = airplane_img.resize((airplane_img.width, airplane_img.height))  # Original size
            airplane = CTkImage(light_image=resized_image1, dark_image=resized_image1, size=(200, 200))
            airplaneImage = customtkinter.CTkLabel(
                levelOnePage,
                text="",
                fg_color="#ffffff",
                image=airplane
            )
            airplaneImage.place(relx=0.50, rely=0.30, anchor=customtkinter.CENTER)
        elif stage == 3:
            arrow_img = Image.open(os.path.join(DRAWABLES_DIR, "arrow.png"))
            resized_arrow = arrow_img.resize((arrow_img.width, arrow_img.height))  # Original size
            arrow = CTkImage(light_image=resized_arrow, dark_image=resized_arrow, size=(240, 240))
            arrowImage = customtkinter.CTkLabel(
                levelOnePage,
                text="",
                fg_color="#ffffff",
                image=arrow
            )
            arrowImage.place(relx=0.50, rely=0.30, anchor=customtkinter.CENTER)

    def playAppleVoice():
        print(stage)
        if stage == 1:
            pygame.mixer.music.load(os.path.join(DRAWABLES_DIR, "applevoice.mp3"))
        elif stage == 2:
            pygame.mixer.music.load(os.path.join(DRAWABLES_DIR, "airplane.wav"))
        elif stage == 3:
            pygame.mixer.music.load(os.path.join(DRAWABLES_DIR, "arrowvoice.wav"))
        pygame.mixer.music.play(loops=0)

    levelComplete = customtkinter.CTkLabel(
        levelOnePage,
        text="Level Complete",
        text_color="#fd6909",
        fg_color="#ffffff",
        font=("Comic Sans MS", 24)
    )

    def next():
        global stage
        word = appleEntry.get().lower()
        if word == "apple":
            appleEntry.delete(0, tk.END)
            stage = 2
            levelOnePage.after(100, airplaneF)
        elif word == "airplane":
            appleEntry.delete(0, tk.END)
            stage = 3
            levelOnePage.after(100, airplaneF)
        elif word == "arrow":
            levelComplete.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
            level = 2
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

    wrongAnswer = customtkinter.CTkLabel(
        levelOnePage,
        text="Wrong Answer!",
        text_color="#ffffff",
        fg_color="#ffffff",
        font=("Comic Sans MS", 24)
    )
    wrongAnswer.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    def count_down(count):
        countDown.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
        if count > 0:
            countDown.configure(text=f"Going Back in {count}")
            root.after(800, count_down, count - 1)
        else:
            levelOnePage.destroy()
            go_back_function()

    countDown = customtkinter.CTkLabel(
        levelOnePage,
        text="",
        text_color="#fd6909",
        fg_color="#ffffff",
        font=("Comic Sans MS", 24)
    )

    # --- ENTRY BOX ---
    appleEntry = customtkinter.CTkEntry(
        levelOnePage, placeholder_text="?",
        border_color="#b14802",
        font=("Comic Sans MS", 20),
        width=200, height=40,
        justify='center',
        fg_color="#f0f0f0", text_color="#fd6909",
        bg_color = "#ffffff"

    )
    appleEntry.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

    # --- ENTER BUTTON ---
    customtkinter.CTkButton(
        levelOnePage, text="Enter",
        font=("Comic Sans MS", 20),
        text_color="white",
        corner_radius=10,
        hover_color="#b14802",
        fg_color="#fd6909",
        bg_color="#ffffff",
        width=200, height=30,
        command=next
    ).place(relx=0.5, rely=0.83, anchor=tk.CENTER)

    # --- PLAY VOICE BUTTON ---
    customtkinter.CTkButton(
        levelOnePage, text="Play",
        font=("Comic Sans MS", 20),
        text_color="white",
        image=speakerIcon,
        corner_radius=10,
        hover_color="#b14802",
        fg_color="#fd6909",
        width=30, height=15,
        bg_color="#ffffff",
        command=playAppleVoice
    ).place(relx=0.445, rely=0.50)

    # --- BACK BUTTON ---
    def backButton():
        levelOnePage.destroy()
        print("Back Button From Level 1")
        go_back_function()

    customtkinter.CTkButton(
        levelOnePage, text="Back",
        font=("Comic Sans MS", 20),
        text_color="white",
        corner_radius=10,
        hover_color="#b14802",
        fg_color="#fd6909", width=15,
        height=15, command=backButton,
        bg_color="#ffffff"

    ).place(relx=0.03, rely=0.04)