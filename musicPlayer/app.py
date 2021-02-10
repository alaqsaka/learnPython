# Setup the app (import libraries)

import pygame 
import tkinter as tkr 
from tkinter.filedialog import askdirectory
import os 
import tkinter.messagebox

# Create app window
musicPlayer = tkr.Tk()

musicPlayer.title("My Music Player") # Title of the application

musicPlayer.geometry("450x350") # Setting the dimension of the app

def greet():
   tkr.messagebox.showinfo("Welcome to My Music Player", "Please Select directory of your music playlist")

greet()

# Ask for music directory 
directory = askdirectory() # prompting user to choose music directory

# Setting music directory to the current working directory 
os.chdir(directory) # responsible for changing current working directory

# Creating songList
# oslistdir() returns a list containing the names of the entries int the directory given by the path 
songList = os.listdir() # returns a list containing names of entries in the given directory

# Creating a playlist
playlist = tkr.Listbox(musicPlayer,font ="Cambria 14 bold", bg = "#1f1f1f", fg="#fff", selectmode=tkr.SINGLE)

# Adding songs from songList to playlist
for song in songList:
    pos=0
    playlist.insert(pos, song)
    pos +=1

pygame.init() # Initializing modules
pygame.mixer.init()

# function for play button
def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play() # method  to play music

# function for stop button
def exitMusicPLayer():
    pygame.mixer.music.stop() # method to stop music

# function for pause button
def pause():
    pygame.mixer.music.pause() # method pause music

# function for resume button
def resume():
    pygame.mixer.music.unpause() 

# Creating button apps

# Play Button
buttonPlay = tkr.Button(musicPlayer, height=3, width=5, text="Play Music", font="Helvetica 14 bold", command=play, bg="#1F1F1F", fg="#FFF")
buttonPlay.pack(fill="x") 


# Pause Button
buttonPause = tkr.Button(musicPlayer, height=3, width=5, text="Pause Music", font="Helvetica 14 bold", command=pause, bg="#1F1F1F", fg="#FFF")
buttonPause.pack(fill="x")

# Stop Button 
buttonStop = tkr.Button(musicPlayer, height=3, width=5, text="Stop Music", font="Helvetica 14 bold", command=exitMusicPLayer, bg="#1F1F1F", fg="#FFF")
buttonStop.pack(fill="x")

# Resume Button 
buttonResume = tkr.Button(musicPlayer, height=3, width=5, text="Resume Music", font="Helvetica 14 bold", command=resume, bg="#1F1F1F", fg="#FFF")
buttonResume.pack(fill="x")

label = tkr.Label(text="Play Queue", font="Helvetica 18 bold", background="#1F1F1F", fg="#FFF")

label.pack(fill="x")

playlist.pack(fill="both", expand="yes")

var = tkr.StringVar()
songTitle = tkr.Label(musicPlayer, font="Helvetica 14 bold", textvariable=var)

songTitle.pack()
musicPlayer.mainloop() #  to run musicPlayer continuously
