from tkinter import *
import os
from tkinter import filedialog
from pygame import mixer
import fnmatch




window = Tk()
window.geometry("600x300")#size of the window
window.title("Music player")#title of the window

rootpath="C:\\Users\srava\Downloads\music"
pattern="*.mp3"
mixer.init()

prev_img=PhotoImage(file='prev.png')
next_img=PhotoImage(file='next.png')
play_img=PhotoImage(file='play.png')
pause_img=PhotoImage(file='pause.png')


listbox=Listbox(window, fg='cyan', bg='black', width=100, font=('poppins',15))
listbox.pack(padx=15, pady=15)

for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        listbox.insert('end',filename)
        listbox.config(height=listbox.size())

label=Label(window, text='', bg='black', fg='yellow')
label.pack(pady=15)

top=Frame(window,bg='black')
top.pack(padx=10, pady=5, anchor='center')

def select():
    label.config(text=listbox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listbox.get("anchor"))
    mixer.music.play()
    

def play_next():
    next_song=listbox.curselection()
    next_song=next_song[0]+1
    next_song_name=listbox.get(next_song)
    label.config(text=next_song_name)
    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()
    listbox.select_clear(0,'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)

def play_prev():
    next_song=listbox.curselection()
    next_song=next_song[0]-1
    next_song_name=listbox.get(next_song)
    label.config(text=next_song_name)
    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()
    listbox.select_clear(0,'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)

def pause():
    if pause_button["text"]=="pause":
        mixer.music.pause()
        pause_button["text"]="play"
    else:
        mixer.music.unpause()
        pause_button["text"]="pause"


prev_button=Button(window, text='prev', image=prev_img, bg='white', borderwidth=0,height=50, width=50, command=play_prev)
prev_button.pack(pady=15, in_=top, side='left')

next_button=Button(window, text='next', image=next_img, bg='white', borderwidth=0,height=50, width=50, command=play_next)
next_button.pack(pady=15, in_=top, side='left')

play_button=Button(window, text='play', image=play_img, bg='white', borderwidth=0,height=50, width=50, command=select)
play_button.pack(pady=15, in_=top, side='left')

pause_button=Button(window, text='pause', image=pause_img, bg='white', borderwidth=0,height=50, width=50, command=pause)
pause_button.pack(pady=15, in_=top, side='left')

#to change the style of window
window.config(background="black")

window.mainloop()

