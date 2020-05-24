import RPi.GPIO as GPIO
import time
from tkinter import *
import tkinter.font
from gpiozero import LED

code = {' ': ' ', 
        "'": '.----.', 
        '(': '-.--.-', 
        ')': '-.--.-', 
        ',': '--..--', 
        '-': '-....-', 
        '.': '.-.-.-', 
        '/': '-..-.', 
        '0': '-----', 
        '1': '.----', 
        '2': '..---', 
        '3': '...--', 
        '4': '....-', 
        '5': '.....', 
        '6': '-....', 
        '7': '--...', 
        '8': '---..', 
        '9': '----.', 
        ':': '---...', 
        ';': '-.-.-.', 
        '?': '..--..', 
        'A': '.-', 
        'B': '-...', 
        'C': '-.-.', 
        'D': '-..', 
        'E': '.', 
        'F': '..-.', 
        'G': '--.', 
        'H': '....', 
        'I': '..', 
        'J': '.---', 
        'K': '-.-', 
        'L': '.-..', 
        'M': '--', 
        'N': '-.', 
        'O': '---', 
        'P': '.--.', 
        'Q': '--.-', 
        'R': '.-.', 
        'S': '...', 
        'T': '-', 
        'U': '..-', 
        'V': '...-', 
        'W': '.--', 
        'X': '-..-', 
        'Y': '-.--', 
        'Z': '--..', 
        '_': '..--.-'}

GPIO.setmode(GPIO.BCM)
led = 24
GPIO.setup(led,GPIO.OUT)

win = Tk()
win.title("Convert Morse code")
myFont = tkinter.font.Font(family = 'Helvetica', size = 13, weight = "bold")

def dash():
    GPIO.output(led,GPIO.HIGH)
    time.sleep(1.5)
    GPIO.output(led,GPIO.LOW)
    time.sleep(1)

def dot():
    GPIO.output(led,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led,GPIO.LOW)
    time.sleep(1)

def CONVERT_MORSE():
    input = INPUT.get()
    for letter in input:
        for symbol in code[letter.upper()]:
            if symbol == '-':
                dash()
            elif symbol == '.':
                dot()
            else:
                time.sleep(1)
    time.sleep(1)

def close():
    GPIO.cleanup()
    win.destroy()

INPUT = Entry(win, font = myFont, width=24, bg= 'white')
INPUT.grid(row=0, column=0)

ledButton = Button(win, text = 'Convert', font = myFont, command = CONVERT_MORSE, bg = 'grey', height = 1, width =24)
ledButton.grid(row=1,column=0)

exitButton = Button(win, text = 'Exit', font = myFont, command = close, bg = 'grey', height = 1, width =24)
exitButton.grid(row=2,column=0)

win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()

