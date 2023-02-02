import math
import tkinter as tk
from PIL import Image, ImageTk
import pyspeedtest
from tkinter import messagebox



root = tk.Tk()
root.geometry("300x450")
root.resizable(0,0)
root.title("Internet Download speed")
root.iconbitmap("robot icon.ico")

# Creating Function
st = pyspeedtest.SpeedTest("www.google.com")
def SpeedTest():
    speed = str(math.floor(st.download()/1000)) + "Kb/s"
    messagebox.showinfo("The speed is ", speed)




# Logo
logo = Image.open("b robot.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.pack()

new_label = tk.Label(root, text = "Test Download Speed", font=("Areal",18, "bold"), fg="green")
new_label.pack(padx=20, pady=20)

# Creating Buttons
button1 = tk.Button(root, text="Check",command=SpeedTest, font=("Areal",20))
button1.pack(padx=20, pady=10)
button2 = tk.Button(root, text="Exit", command=root.destroy,font=("Areal", 20))
button2.pack(padx=10, pady=10)

# Creating Label
new_label2 = tk.Label(root, text="Thanks!!", font=("Areal", 25, "bold"), bg="black", fg="white")
new_label2.pack(padx=10, pady=10, fill="both", expand=True)


root.mainloop()
