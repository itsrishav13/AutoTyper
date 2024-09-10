import tkinter as tk
import pyautogui
import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# Creating window
root = tk.Tk()
img = tk.PhotoImage(file=BASE_DIR / "logo.png")
root.iconphoto(False, img)
root.geometry("720x750")
root.title("AutoTyper App")

# Text Entry
def get_text():
    return entry.get()  # Getting Data from the first check box

label = tk.Label(root, text="Paste Your text here :)", font=("Helvetica", 12))  # Making Label For first entry box
label.pack()

entry = tk.Entry(root, width=40, font=("Helvetica", 14))
entry.pack(pady=10)

# Loop
def get_no_of_times():
    try:
        user_input = int(loop.get())
        if user_input <= 0:
            raise ValueError("Number of times should be a positive integer")
        return user_input
    except ValueError as e:
        error_label.config(text=str(f"{e} >> Please Enter Integer Value!"))
        return None

label_loop = tk.Label(root, text="Number of times?", font=("Helvetica", 12))
label_loop.pack()

loop = tk.Entry(root, font=("Helvetica", 18))
loop.pack(pady=10)
loop.insert(0, "1")  # Making default value 1
error_label = tk.Label(root, fg="red")
error_label.pack()

# Enter Button
def check_enter():
    current_state = checkbox_enter.get()
    if current_state == 1:
        pyautogui.press("enter")

checkbox_enter = tk.IntVar()
checkbox = tk.Checkbutton(root, text="Press Enter after every line?", variable=checkbox_enter, command=checkbox_enter, font=("Helvetica", 12))
checkbox.pack(pady=10)

# Sleep
def waiting_time():
    try:
        user_input = int(wait.get())
        if user_input <= 0:
            raise ValueError("Number of times should be a positive integer")
        return user_input
    except ValueError as e:
        error_label.config(text=str(f"{e} >> Please Enter Integer Value! Recommended more than 3"))
        return None

label = tk.Label(root, text="Time to wait before Execution!", font=("Helvetica", 10))
label.pack(pady=10)
wait = tk.Entry(root, font=("Helvetica", 14))
wait.pack(pady=10)
wait.insert(0, "3")

error_label = tk.Label(root, fg="red")
error_label.pack()

# Typing Speed
def typing_speed():
    try:
        user_input = float(speed.get())
        if user_input < 0:
            raise ValueError("Typing speed must be a positive number")
        return user_input
    except ValueError as e:
        error_label.config(text=str(f"{e} >> Please Enter a positive number for typing speed"))
        return None

label_speed = tk.Label(root, text="Typing speed (seconds per character)?\n (0 is the fastest, want more slow? Try 0.3)", font=("Helvetica", 10))
label_speed.pack(pady=10)
speed = tk.Entry(root, font=("Helvetica", 14))
speed.pack(pady=10)
speed.insert(0, "0.2")  # Default typing speed is 0.2 seconds per character

error_label = tk.Label(root, fg="red")
error_label.pack()

# Final Result
def paste():
    txt = get_text()
    num_times = get_no_of_times()
    typing_delay = typing_speed()  # Get typing speed from user input
    if txt is not None and num_times is not None and typing_delay is not None:
        time.sleep(waiting_time())
        for i in range(num_times):
            pyautogui.typewrite(f"{txt}", interval=typing_delay)  # Use typing delay
            check_enter()

button = tk.Button(root, text="Submit", font=("Helvetica", 10), command=paste)
button.pack(pady=30)

root.mainloop()
