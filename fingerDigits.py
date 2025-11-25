import tkinter as tk

screen = tk.Tk()
screen.title("DL Digits")
screen.geometry("500x500")

button1 = tk.Button(screen, text = "I'm a button", bg = "green", fg = "white", borderwidth = 10, activebackground = "red", activeforeground = "yellow", highlightbackground = "purple", highlightthickness = 5)
button1.place(x = 200, y = 400)

label = tk.Label(screen, text = "Digit Classifer", font = ("arial", 20), bg = "green", fg = "white", bd = 2)
label.place(x = 0, y = 0)

canvas = tk.Canvas(screen, bg = "white", height = 250, width = 250)
canvas.place(x = 120, y = 100)

def mouseDrawing(event):
    canvas.create_oval(event.x, event.y, event.x + 2, event.y + 5, fill = "green", outline = "#1c6537")

canvas.bind("<B1-Motion>", mouseDrawing)








screen.mainloop()