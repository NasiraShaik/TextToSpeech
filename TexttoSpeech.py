import tkinter
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import filedialog
import pyttsx3
import os
root=tkinter.Tk()
root.title("Text To Speech")
root.geometry("900x450")
root.resizable(False,False)
root['background']='blueviolet'
engine=pyttsx3.init()
###################################################### speak function ################################################
def speak():
    text=text_box.get(1.0,END)
    gender=gender_combobox.get()
    speed=speed_combox.get()
    voices=engine.getProperty('voices')
    ################################################### setting the voice function  ##################################
    def setvoice():
        if gender=="Male":
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            engine.say(text)
            engine.runAndWait()
################################################# voice speed #######################################################
    if(text):
        if speed=="Fast":
            engine.setProperty('rate',250)
            setvoice()
        elif speed=="Normal":
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()
###################################################### save audio function ##########################################
def savevoice():
    text=text_box.get(1.0,END)
    gender=gender_combobox.get()
    speed=speed_combox.get()
    voices=engine.getProperty('voices')
    def setvoice():
        if gender=="Male":
            engine.setProperty('voice',voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
#################################### Save audio file as audio.mp3 ###################################################
            engine.save_to_file(text,'audio.mp3')
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
#################################### Save audio file as audio.mp3 ###################################################
            engine.save_to_file(text,'audio.mp3')
            engine.say(text)
            engine.runAndWait()
    if(text):
        if speed=="Fast":
            engine.setProperty('rate',250)
            setvoice()
        elif speed=="Normal":
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()
#################################### Top frame #####################################################################
top_frame=Frame(root,width=900,height=100)
top_frame.place(x=0,y=0)
Label(top_frame,text="TEXT TO SPEECH",font="arial 20 bold",bg="white",fg="black").place(x=300,y=30)
################################### text box #######################################################################
text_box=Text(root,font="Robote 20",bg="White",relief=GROOVE,wrap=WORD)
text_box.place(x=10,y=150,width=500,height=250)
Label(root,text="VOICE",font="arial 15 bold",bg="blueviolet",fg="white").place(x=580,y=160)
Label(root,text="SPEED",font="arial 15 bold",bg="blueviolet",fg="white").place(x=760,y=160)
################################### combo box for gender ###########################################################
gender_combobox=Combobox(root,values=['Female','Male'],font="arial 14",state='r',width=10)
gender_combobox.place(x=550,y=200)
################################### set the default gender to Male #################################################
gender_combobox.set("Male")
################################### combo box for gender ###########################################################
speed_combox=Combobox(root,values=['Fast','Normal','Slow'],font="arial 14",state='r',width=10)
speed_combox.place(x=730,y=200)
################################### set the default speed to Normal ################################################
speed_combox.set("Normal")
################################### button for speak ##############################################################
sbtn=Button(root,text="Speak",width=10,font="arial 14 bold",command=speak)
sbtn.place(x=550,y=280)
################################### button for save ###############################################################
savebtn=Button(root,text="Save",width=10,font="arial 14 bold",command=savevoice)
savebtn.place(x=730,y=280)
root.mainloop()