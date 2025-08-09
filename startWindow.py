import tkinter as tk
import customtkinter
from PIL import Image, ImageTk
from logInWindow import loginWindow

def startWindow(root, image, openLoginWindow, image1):
    def open():
        canvas.destroy()
        openLoginWindow(root, image1)  # Call the openLoginWindow function with the appropriate parameters

    canvas = tk.Canvas(root, width=1080, height=720)
    canvas.create_image(0, 0, anchor=tk.NW, image=image)
    canvas.pack()

    start_button = customtkinter.CTkButton(canvas, text="Start",
                                           font=("Comic Sans MS", 24),
                                           text_color="white",
                                           corner_radius=40,
                                           hover_color="#b14802",
                                           fg_color="#fd6909",
                                           width=200, height=50, command=open)
    start_button.place(relx=0.5, rely=0.73, anchor=tk.CENTER)

