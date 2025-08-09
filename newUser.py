import tkinter as tk
import customtkinter
from DatabaseHelper import insertAccount

def newUserAccount(root, image1, canvas1):
    username = ""
    password = ""

    def insertAccountToDb():
        username = usernameEntry.get()
        password = passwordEntry.get()
        insertAccount(username, password, displayAccountValidity, successFullInsert)

    def back():
        canvas1.pack()
        newUser_Canvas.pack_forget()

    def displayAccountValidity(count):
        wrongAnswer.configure(text="Acount already exist!")
        wrongAnswer.configure(text_color="#ff0000")
        wrongAnswer.place(relx=0.5, rely=0.37, anchor=tk.CENTER)
        if count > 0:
            root.after(200, displayAccountValidity, count - 1)
        else:
            wrongAnswer.configure(text_color="#f0f0f0")
            wrongAnswer.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    def successFullInsert(count):
        success.configure(text="Account Create Success!")
        success.configure(text_color="#ff0000")
        success.place(relx=0.5, rely=0.37, anchor=tk.CENTER)
        if count > 0:
            root.after(200, successFullInsert, count - 1)
        else:
            success.configure(text_color="#f0f0f0")
            success.place(relx=0.5, rely=0.9, anchor=tk.CENTER)




    newUser_Canvas = customtkinter.CTkCanvas(root, width=1080, height=720)
    newUser_Canvas.create_image(0, 0, anchor=tk.NW, image=image1)
    newUser_Canvas.pack()

    success = customtkinter.CTkLabel(newUser_Canvas,
                                         text="Wrong username or password!",
                                         text_color="#f0f0f0",
                                         fg_color="#f0f0f0",
                                         font=("Comic Sans MS", 13))

    wrongAnswer = customtkinter.CTkLabel(newUser_Canvas,
                                         text="Wrong username or password!",
                                         text_color="#f0f0f0",
                                       fg_color="#f0f0f0",
                                       font=("Comic Sans MS", 13))

    usernameEntry = customtkinter.CTkEntry(newUser_Canvas, placeholder_text="Username",
                                           border_color="#b14802",
                                           width=200, height=40,
                                           fg_color="#f0f0f0", text_color="#fd6909")
    usernameEntry.place(relx=0.5, rely=0.43, anchor=tk.CENTER)

    passwordEntry = customtkinter.CTkEntry(newUser_Canvas, placeholder_text="Password",
                                           border_color="#b14802",
                                           width=200, height=40,
                                           fg_color="#f0f0f0", text_color="#fd6909")
    passwordEntry.place(relx=0.5, rely=0.51, anchor=tk.CENTER)

    createUser_button = customtkinter.CTkButton(newUser_Canvas, text="Create User",
                                           font=("Comic Sans MS", 20),
                                           text_color="white",
                                           corner_radius=40,
                                           hover_color="#b14802",
                                           fg_color="#fd6909",
                                           width=200, height=15,
                                           command=insertAccountToDb).place(relx=0.5, rely=0.59, anchor=tk.CENTER)

    back_Button = customtkinter.CTkButton(newUser_Canvas, text="Back",
                                     font=("Comic Sans MS", 20),
                                     text_color="#fd6909",
                                     corner_radius=40,
                                     hover_color="#fef8e5",
                                     fg_color="#fef8e5",
                                     width=15, height=15,
                                     command=back).place(relx=0.068, rely=0.095)