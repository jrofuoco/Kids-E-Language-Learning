from PIL import Image, ImageTk

secondPageImagePath = "C:\\Users\\Fuoco\\PycharmProjects\\pythonProject\\.venv\\drawables\\secondpagebackground.png"
secondPageImage = Image.open(secondPageImagePath)
secondPageImage = secondPageImage.resize((1080, 720), Image.FIXED)
secondPageImage = ImageTk.PhotoImage(secondPageImage)