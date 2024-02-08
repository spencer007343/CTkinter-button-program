import customtkinter
import sys

#it is generally considered bad practice to import asterisks as they load serverl names into the global namespace. This can potentially cause name collisions however, this is necessary in order to use the constant 'INSERT'
from tkinter import *

customtkinter.set_appearance_mode("System")
customtkinter.set_appearance_mode("blue")

#This is where the frame for our window is defined
app = customtkinter.CTk()
app.geometry("800x420")
app.title("Hex color value display")



#This is where our buttons are defined
def red_button():
    sys.stdout.write("This button's color is hex value: #ea1c0c" + '\n')

def blue_button():
    sys.stdout.write("This button's color is hex value:  #0c48ea" + '\n')

def yellow_button():
    sys.stdout.write("This button's color is hex value:  #e2ef17" + '\n')

#create text box to display hex values
textbox_font = customtkinter.CTkFont(family="Times New Roman", size=14)

textbox = customtkinter.CTkTextbox(app, font=textbox_font, width = 400, height = 200)
textbox.configure(text_color="black", fg_color="white")
textbox.grid(row = 3, column = 4)

#This is function redirects text from sys.stdout.write to the tkinter textbox
def textredirect(inputStr):
    textbox.insert(INSERT, inputStr)

sys.stdout.write = textredirect

#define our buttons
buttonr = customtkinter.CTkButton(app, fg_color="#ea1c0c", text="Red", command=red_button)
buttonr.grid(row = 3, column = 0, ipady = 10, pady = 10, padx = 5)

buttonb = customtkinter.CTkButton(app, fg_color="#0c48ea", text="Blue", command=blue_button)
buttonb.grid(row = 3, column = 1, ipady = 10, pady = 10, padx = 5)

buttony = customtkinter.CTkButton(app, fg_color="#e2ef17", text="Yellow", command=yellow_button)
buttony.grid(row = 3, column = 2, ipady = 10, pady = 10, padx = 5)

app.mainloop()



