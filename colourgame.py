# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 12:23:24 2022

@author: Admin
"""

import tkinter 
import random
colours = ['Green', 'Blue', 'Red', 'Yellow', 'Pink', 'White', 'Orange', 'Black', 'Purple']
score = 0
timeleft = 30
def startGame(event):
    if timeleft == 30:
        countdown()
        
    nextColour()
    
def nextColour():
    global score
    global timeleft
    
    if timeleft > 0:
        e.focus_set()
        
        if e.get().lower() == colours[1].lower():
            score = score + 1
            
        e.delete(0, tkinter.END)
        random.shuffle(colours)
        label.config(fg = str(colours[1]), text = str(colours[0]))
        scoreLabel.config(text = "Score: " + str(score))
        
def countdown():
    global timeleft
    if timeleft > 0:
        timeleft = timeleft - 1
        timeLabel.config(text = "Time left:" + str(timeleft))
        timeLabel.after(1000, countdown)
       
root = tkinter.Tk()
root.title("ColorGame")
root.geometry("375x200")
instructions = tkinter.Label(root, text = "Please type the color which is displaying over the text, Dont type text which is displaying", font = ('Helvetica', 15))
instructions.pack()
scoreLabel = tkinter.Label(root, text = "Press enter to play the game", font = ('Helvetica', 15))
scoreLabel.pack()
timeLabel = tkinter.Label(root, text = "time left:" + str(timeleft), font = ('Helvetica',12))
timeLabel.pack()
label = tkinter.Label(root, font = ('Helvetica', 60))
label.pack()
e = tkinter.Entry(root)
root.bind('<Return>', startGame)
e.pack()
e.focus_set()
root.mainloop()
