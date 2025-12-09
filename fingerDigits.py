import tkinter as tk
from tensorflow.keras.models import load_model
from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt


Sequential = load_model(r"C:\Users\kaige\python projects\Deep Learning\Sequential.h5")
prediction = 0
number = 0
blankImage = 0


screen = tk.Tk()
screen.title("DL Digits")
screen.geometry("500x500")
canvas = tk.Canvas(screen, bg = "white", height = 250, width = 250)
canvas.place(x = 120, y = 100)
label2 = tk.Label(screen, text = "", font = ("arial", 10), bg = "green", fg = "white", bd = 2)
label2.place(x = 360, y = 480)


def mouseDrawing(event):
    canvas.create_oval(event.x, event.y, event.x + 5, event.y + 5, fill = "green", outline = "#1c6537")

#img = canvas.postscript(file="temp_canvas.ps")  # Save canvas content as .ps (PostScript), to make it not based on vectors.
#blankImage = Image.open("temp_canvas.ps")
blankImage = Image.new("L", (250, 250), color = "white")
number = ImageDraw.Draw(blankImage)

def Clear():
    global number, blankImage
    canvas.delete("all")
    blankImage = Image.new("L", (250, 250), color = "white")
    number = ImageDraw.Draw(blankImage)
    label2.config(text = "")



def Predict():
    global prediction
    proccessedImage = blankImage.resize((28, 28))
    print(proccessedImage)
    #plt.imshow(proccessedImage)
    proccessedImage = np.array(proccessedImage)
    plt.imshow(proccessedImage)
    plt.show()
    proccessedImage = proccessedImage / 255.0
    proccessedImage = np.expand_dims(proccessedImage, axis = 0)
    #plt.imshow(proccessedImage)
    #print(proccessedImage)
    prediction = Sequential.predict(proccessedImage)
    print(prediction)
    prediction = np.argmax(prediction)
    label2.config(text = prediction)
    #print(prediction)




    # print(proccessedImage)


button1 = tk.Button(screen, text = "Predict", bg = "green", fg = "white", borderwidth = 10, activebackground = "red", activeforeground = "yellow", highlightbackground = "purple", highlightthickness = 5, command = Predict)
button1.place(x = 200, y = 400)

button2 = tk.Button(screen, text="Clear",
                    bg="green",
                    fg="white",
                    activebackground="red",
                    activeforeground="black",
                    width=10,
                    command= Clear,
                    cursor="hand2")
button2.place(x=330, y=430)

label = tk.Label(screen, text = "Digit Classifer", font = ("arial", 20), bg = "green", fg = "white", bd = 2)
label.place(x = 160, y = 0)






canvas.bind("<B1-Motion>", mouseDrawing)








screen.mainloop()