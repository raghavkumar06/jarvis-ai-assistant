import tkinter as tk
import threading
from jarvis_core import main_process

# ---------------- GUI FUNCTIONS ----------------

def start_jarvis():
    status_label.config(text="JARVIS is Listening...")
    t = threading.Thread(target=main_process, daemon=True)
    t.start()

# ---------------- MAIN WINDOW ------------------

window = tk.Tk()
window.title("JARVIS AI Assistant")
window.geometry("500x400")
window.configure(bg="black")

# ---------------- TITLE ------------------

title = tk.Label(
    window,
    text="JARVIS AI",
    fg="cyan",
    bg="black",
    font=("Arial", 24, "bold")
)
title.pack(pady=30)

# ---------------- BUTTON ------------------

start_btn = tk.Button(
    window,
    text="Start JARVIS",
    command=start_jarvis,
    font=("Arial", 14),
    bg="cyan",
    width=15
)
start_btn.pack(pady=20)

# ---------------- STATUS ------------------

status_label = tk.Label(
    window,
    text="Click Start to run JARVIS",
    fg="white",
    bg="black",
    font=("Arial", 12)
)
status_label.pack(pady=20)

# ---------------- RUN GUI ------------------

window.mainloop()
