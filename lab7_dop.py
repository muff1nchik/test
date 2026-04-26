import tkinter as tk
import requests
from PIL import Image, ImageTk
from io import BytesIO #убираем ошибки при передаче в image.pillow

API = "https://nekos.best/api/v2/neko"

def get_image_url():
    response = requests.get(API)

    if response.status_code == 200:
        data = response.json()
        return data["results"][0]["url"]
    else:
        print(f"Ошибка {response.status_code}")

def get_image(image_url):
    response = requests.get(image_url)

    if response.status_code == 200:
        image_data = BytesIO(response.content)
        image = Image.open(image_data)
        image.thumbnail((400, 400)) # как resize только не меняет пропорции
        return ImageTk.PhotoImage(image)
    else:
        print("Ошибка загрузки картинки")


def change():
    image_url = get_image_url()

    if image_url is None:
        return 
    
    new_image = get_image(image_url)

    if new_image is None:
        return
    
    image_label.config(image=new_image)
    image_label.image = new_image

window = tk.Tk()
window.title("Картинки")
window.geometry("500x520")

image_label = tk.Label(window)
image_label.pack(pady=20)

button = tk.Button(
    window,
    text="След",
    command=change
)
button.pack(pady=10)

change()

window.mainloop()