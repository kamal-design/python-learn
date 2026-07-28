import tkinter as tk # import the tkinter module

# step1: create the main window
root = tk.Tk()
root.title("My first GUI")
root.geometry("300x200") # set width x height
root.configure(bg="black") # explicit bg so text isn't invisible in macOS dark mode

# step2: add a label
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14), bg="black", fg="white")
label.pack(pady=20) #add vertical padding

# step3: add a button usage
def on_click():
    label.config(text="You clicked the button!")

button = tk.Button(root, text="Click Me", command=on_click)
button.pack()

# step4: bring window to front (macOS often opens it behind other windows)
root.lift()
root.attributes("-topmost", True)
root.after(500, lambda: root.attributes("-topmost", False))
root.focus_force()

# step5: start the GUI loop
root.mainloop()


# pkill -f tkinter_app.py