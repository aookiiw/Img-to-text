import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import pytesseract

# Function to handle button click event
def upload_image():
    # Open file dialog to select an image file
    filepath = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")])

    # Check if a file was selected
    if filepath:
        # Load the image
        image = Image.open(filepath)

        # Display the image on the GUI
        image.thumbnail((400, 400))  # Resize image to fit within the GUI
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo

        # Perform OCR on the image
        text = pytesseract.image_to_string(image)

        # Log the extracted text
        log_text(text)


# Function to log the extracted text
def log_text(text):
    text_log.insert(tk.END, text + '\n')


# Create the main window
window = tk.Tk()
window.title("Image Text Extractor")

# Create the GUI components
upload_button = tk.Button(window, text="Upload Image", command=upload_image)
upload_button.pack(pady=10)

image_label = tk.Label(window)
image_label.pack()

text_log = tk.Text(window, height=10, width=50)
text_log.pack(padx=10, pady=10)

# Start the GUI event loop
window.mainloop()
