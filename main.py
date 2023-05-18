import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import pytesseract

def upload_image():
  
    filepath = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")])


    if filepath:

        image = Image.open(filepath)


        image.thumbnail((400, 400))  
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo

        text = pytesseract.image_to_string(image)


        log_text(text)


def log_text(text):
    text_log.insert(tk.END, text + '\n')


window = tk.Tk()
window.title("Image Text Extractor")

upload_button = tk.Button(window, text="Upload Image", command=upload_image)
upload_button.pack(pady=10)

image_label = tk.Label(window)
image_label.pack()

text_log = tk.Text(window, height=10, width=50)
text_log.pack(padx=10, pady=10)

window.mainloop()
