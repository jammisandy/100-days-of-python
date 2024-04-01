from tkinter import *
import math
YELLOW = "#f7f5dd"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file="100-days-of-python/Day-29/logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.pack()

window.mainloop()