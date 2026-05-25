import tkinter as tk
from PIL import Image, ImageTk
import random
import string

root = tk.Tk()
root.title("Password Cracker")
root.geometry("600x400")

canvas = tk.Canvas(root, highlightthickness=0)
canvas.pack(fill="both", expand=True)

img = Image.open("./password front.png")

bg_img = None
bg_id = canvas.create_image(0, 0, anchor="nw")

def resize(event):
    root.after(50, lambda: update_bg(event))

def update_bg(event):
    global bg_img

    resized = img.resize((event.width, event.height))
    bg_img = ImageTk.PhotoImage(resized)

    canvas.itemconfig(bg_id, image=bg_img)

root.bind("<Configure>", resize)

text_id = canvas.create_text(
    300, 50,
    text="",
    fill="#00FF00",
    font=("Courier New", 25, "bold")
)

text = "Welcome to hacker cracker!"
i = 0
display = ""

def typing():
    global i, display

    if i < len(text):
        display += text[i]
        i += 1
        canvas.itemconfig(text_id, text=display)
        root.after(60, typing)

typing()


ui_frame = tk.Frame(root, bg="black")
canvas.create_window(300, 220, window=ui_frame)

entry1 = tk.Entry(
    ui_frame,
    bg="black",
    fg="#00FF00",
    insertbackground="#00FF00",
    font=("Consolas", 12),
    width=25
)
entry1.pack(pady=5)
entry1.insert(0, "Enter the number")

entry2 = tk.Entry(
    ui_frame,
    bg="black",
    fg="#00FF00",
    insertbackground="#00FF00",
    font=("Consolas", 12),
    width=25
)
entry2.pack(pady=5)
entry2.insert(0, "Your password is here")

def clear_text(event):
    event.widget.delete(0, tk.END)

entry1.bind("<FocusIn>", clear_text)
entry2.bind("<FocusIn>", clear_text)


characters = string.ascii_letters + string.digits + string.punctuation

def generate():
    value = entry1.get()

    if not value.isdigit():
        entry2.delete(0, tk.END)
        entry2.insert(0, "Enter valid number")
        return

    length = int(value)

    password = ""
    for _ in range(length):
        password += random.choice(characters)

    entry2.delete(0, tk.END)
    entry2.insert(0, password)


button = tk.Button(
    ui_frame,
    text="Press to generate",
    command=generate,
    bg="black",
    fg="#00FF00",
    activebackground="black",
    activeforeground="#00FF00"
)
button.pack(pady=10)

# hover effect
button.bind("<Enter>", lambda e: button.config(bg="green"))
button.bind("<Leave>", lambda e: button.config(bg="black"))
root.attributes("-alpha", 0.9)

root.mainloop()