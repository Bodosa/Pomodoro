""" Pomodoro Technique """
import tkinter as tk
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 50
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 15
reps = 0
reset = None


# TIME RESET
def reset_timer():
    # cancel the timer set up previously
    window.after_cancel(reset)
    # timer text 00:00
    canvas.itemconfig(timer, text="00:00")
    title_text.config(text="Timer")
    mark.config(text="")
    global reps
    reps = 0

# TIMER MECHANISM
def start_timer():
    global reps
    reps += 1

    work_min = WORK_MIN * 60
    short_b = SHORT_BREAK_MIN * 60
    long_b = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_b)
        title_text.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_b)
        title_text.config(text="Break", fg=PINK)
    else:
        count_down(work_min)
        title_text.config(text="Work", fg=GREEN)




# COUNTDOWN MECHANISM
def count_down(count):
    # math.floor() returns the largest whole number <= x
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global reset
        reset = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        mark.config(text=marks)



window = tk.Tk()
window.title("Pomodoro")
window.config(padx=150, pady=100, bg=YELLOW)



# DISPLAY IMAGE
# canvas widget = allows to layer things one o top of the others
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# the way to read through a file and get hold of a particular image at file location
img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)


# TEXT
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)
title_text = tk.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
title_text.grid(column=1, row=0)


# BUTTONS
start_button = tk.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# MARK
mark = tk.Label(fg=GREEN, bg=YELLOW)
mark.grid(column=1, row=3)


window.mainloop()
