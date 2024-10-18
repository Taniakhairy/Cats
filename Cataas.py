from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def loade_image():
    try:
        response = request.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        return ImageTk.PhotoImage(ing)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


window = TK()
window.title("Cats!")
window.geometry("600x480")

label = Label()
label.pack()

url = "https://cataas.com/cat"
img = load_image(url)

if img:
    label.config(image=img)
    label.image = img

    window.mainloop()
