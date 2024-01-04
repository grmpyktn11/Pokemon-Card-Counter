import cv2
from PIL import Image  as pilImage
from pytesseract import pytesseract
import re

def cleanUpText(ocr_text):
    # Remove non-alphanumeric characters and extra whitespaces
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', ocr_text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    return cleaned_text

on = True
#MANAGING DECK
switchCards = {'Switch':4,  'Ultra Ball': 4, 'Nest Ball': 2}


def tesseract():
    path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    Imagepath='test1.jpg'
    pytesseract.tesseract_cmd = path 
    textfromimage = pytesseract.image_to_string(pilImage.open(Imagepath))
    return(textfromimage)

def captureImage() -> str:
    #MAIN FUNCTIONALITY
    url = 'http://192.168.1.163:8080/video'
    camera = cv2.VideoCapture(url)

    while True:
        _,image = camera.read()
        cv2.imshow('image',image)

        if cv2.waitKey(1):
            cv2.imwrite('test1.jpg',image)
            break
    camera.release()
    cv2.destroyAllWindows()
    pop = tesseract()
    return pop


def turn():
    card = 'ERROR'
    q= captureImage()
    print(q)
    for i in switchCards:
        if(i in q) and switchCards[i] > 0:
            switchCards[i] -= 1
            card = i
            return ("you have " + str(switchCards[i]) + " " + card + " cards left.")
    return "Error"



# Import the required libraries
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Create an instance of tkinter frame
win= Tk()

# Set the size of the tkinter window
win.geometry("1000x500")

# # Define a function to show the popup message
# def show_msg():
#    messagebox.showinfo("Switch cards",turn())

def setMsg():
    var.set(turn())

var = StringVar()

var.set("Pokemon deck counter! ")
# Add an optional Label widget
msg = Label(win, textvariable=var, font= ('Aerial 17 bold italic')).pack(pady= 30)

# Create a Button to display the message
ttk.Button(win, text= "Click Here", command=setMsg).pack(pady= 20)
win.mainloop()
