#interface for the project 
import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np 

from database import FaceDatabase


root = tk.Tk()
root.title("File Upload Interface")
root.geometry("400x200")
root.configure(bg="#f7f7fa")
frame = tk.Frame(root, bg="#f7f7fa")
frame.place(relx=0.5, rely=0.5, anchor='center')

label = tk.Label(frame, text="Upload an Image File", font=("Helvetica", 20, "bold"),
                  bg="#f7f7fa", fg="#333")
label.pack(pady=(0,22))

button = tk.Button(
    frame, 
    text="Upload Image", 
    command=FaceDatabase.load,
    font=("Helvetica", 13, "bold"),
    bg="#4f8cff", 
    fg="white",
    activebackground="#3460a9",
    activeforeground="white",
    relief="flat",
    bd=0,
    padx=36, 
    pady=12, 
    highlightthickness=0
)
button.pack()


root.mainloop()

