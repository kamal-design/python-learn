import tkinter as tk
from time import strftime

# step1: create the main window
root = tk.Tk()
root.title("Simple Clock")
root.geometry("300x220")
root.configure(bg="white")  # explicit bg so text isn't invisible in macOS dark mode

# step2: add a label to display the current time
time_label = tk.Label(root, font=("Arial", 32), bg="white", fg="black")
time_label.pack(pady=10)

# step3: clock timer - updates the label and reschedules itself
def update_time():
    time_label.config(text=strftime("%H:%M:%S"))
    root.after(1000, update_time)  # run again after 1000ms (1 second)

update_time()

# step4: stopwatch fields
elapsed_seconds = 0
running = False
stopwatch_job = None

stopwatch_label = tk.Label(root, text="00:00:00", font=("Arial", 24), bg="white", fg="black")
stopwatch_label.pack(pady=5)

def format_elapsed(total_seconds):
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def tick():
    global elapsed_seconds, stopwatch_job
    elapsed_seconds += 1
    stopwatch_label.config(text=format_elapsed(elapsed_seconds))
    stopwatch_job = root.after(1000, tick)

def start_stopwatch():
    global running
    if not running:
        running = True
        tick()

def stop_stopwatch():
    global running, stopwatch_job
    running = False
    if stopwatch_job is not None:
        root.after_cancel(stopwatch_job)
        stopwatch_job = None

def reset_stopwatch():
    global elapsed_seconds
    stop_stopwatch()
    elapsed_seconds = 0
    stopwatch_label.config(text=format_elapsed(elapsed_seconds))

# step5: stopwatch buttons
button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=10)

button_style = dict(bg="#e6e6e6", fg="black", activebackground="#cfcfcf",
                    highlightbackground="#e6e6e6", highlightthickness=0,
                    relief="solid", borderwidth=1)

start_button = tk.Button(button_frame, text="👏 Start", width=8, command=start_stopwatch, **button_style)
start_button.grid(row=0, column=0, padx=5)

stop_button = tk.Button(button_frame, text="✋ Stop", width=8, command=stop_stopwatch, **button_style)
stop_button.grid(row=0, column=1, padx=5)

reset_button = tk.Button(button_frame, text="❌ Reset", width=8, command=reset_stopwatch, **button_style)
reset_button.grid(row=0, column=2, padx=5)

# step6: bring window to front (macOS often opens it behind other windows)
root.lift()
root.attributes("-topmost", True)
root.after(500, lambda: root.attributes("-topmost", False))
root.focus_force()

# step7: start the GUI loop
root.mainloop()
