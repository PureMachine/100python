import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARKS = []
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    global REPS, CHECK_MARKS
    REPS = 0
    window.after_cancel(timer)
    timer_label.config(text="Timer", bg=PINK, fg=GREEN)
    CHECK_MARKS = []

# ---------------------------- TIMER MECHANISM ------------------------------- #

REPS = 0
def start():
    global REPS
    REPS += 1

    work_timer_count = WORK_MIN - 22
    short_timer_count = SHORT_BREAK_MIN - 4
    long_timer_count = LONG_BREAK_MIN * 60

    if REPS == 7:
        countdown(long_timer_count)
        timer_label.config(text="Long Break", bg=PINK, fg=GREEN)
        canvas.config(bg=PINK)
        window.config(bg=PINK)
    elif REPS % 2 == 0:
        countdown(work_timer_count)
        timer_label.config(text="Work Time", bg=RED, fg=GREEN)
        canvas.config(bg=RED)
        window.config(bg=RED)
    elif REPS % 2 != 0:
        countdown(short_timer_count)
        timer_label.config(text="Short Break", bg=GREEN, fg=RED)
        canvas.config(bg=GREEN)
        window.config(bg=GREEN)
    else:
        pass


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
import time


def countdown(count):

    global CHECK_MARKS, timer

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    if len(str(count_sec)) < 2:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start()
        if REPS % 2 != 0:
            CHECK_MARKS.append("✔")
            display = " ".join(CHECK_MARKS)
            check_mark.config(text=f"{display}")

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.config(width=500, height=500, padx=120, pady=60, bg=YELLOW)
window.title("Pomodoro")

timer_label = tkinter.Label(text="Timer", font=("Times New Roman", 40, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tkinter.Button(text="Start", command=start)
start_button.grid(column=0, row=2)
reset_button = tkinter.Button(text="Reset", command=reset)
reset_button.grid(column=2, row=2)

check_mark = tkinter.Label()
check_mark.grid(column=1, row=3)


window.mainloop()
