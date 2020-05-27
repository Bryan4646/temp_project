#Temperature Project Using IFTTT to relay a signal to RPi from Particle Argon
#This code will turn on LED when Desired Temperature is nto matched to reading on the sensor
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
import time 
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(10, GPIO.OUT)

GPIO.output(10, True)

master = tkinter.Tk()
master.title("User Details")

tkinter.Label(master, text = "Please Enter Name").grid(row=0) #allow user to enter their name
tkinter.Label(master, text = "Please Enter Desired Temperature: ").grid(row=1) #allow user to enter desired Temperature


f1 = tkinter.Entry(master)
f2 = tkinter.Entry(master)

f1.grid(row=0, column=1) #position of first field
f2.grid(row=1, column=1) #position of second field


def close(): #this code is used to destroy the first window
    master.destroy()


    
def Next(): #the button will create a new window and show the following elements
    newWindow = Toplevel() 
    newWindow.title("Smart Temperature")
    tkinter.Label(newWindow, text = "Name and Household Temperature Entered, Please click begin to start!").grid(row=0)
    
    beginbtn = Button(newWindow, text = 'Begin', command = lighton, height = 1, width = 6)
    beginbtn.grid(row=3, column=2)
    
    exitw2 = Button(newWindow, text = 'Exit', command = newWindow.destroy, height = 1, width = 6)
    exitw2.grid(row=3, column=1)
    
   

def lighton():
    GPIO.output(10, False)
    sleep(10)
    GPIO.output(10, True)
            
    
        #Something needs to be done to stop code !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Fix this
        
b1 = Button(master, text = 'Exit', command = close, height =  1, width = 6)
b1.grid (row=2, column=0)

b2 = Button(master, text = 'Next', command = Next, height = 1, width = 6)
b2.grid (row=2, column=1)
        


                    
master.mainloop()
     