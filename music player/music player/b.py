from tkinter import *
from tkinter import filedialog


def play():
    print("The song is playing")

def search():
    song_name=entry.get()
    print('Results for '+ song_name+' are')

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)

def display():
    print(listbox.get(listbox.curselection()))

def open():
    filepath=filedialog.askopenfilename()
    file=open(filepath,'r')
    print(file.read())
    file.close()

window=Tk() #instantiates an instance of window
window.geometry("500x500")#size of the window
window.title("Music player")#title of the window

#to change the icon on the window
icon=PhotoImage(file='music.png')
window.iconphoto(True,icon)

#to change the style of window
window.config(background="black")

#opening a file
file=Button(window,text='open', command=open)
file.pack(side=BOTTOM)

#creating a label
label=Label(window,text="Listen to music!!",font=('Arial',25),fg='green',bg='black')
label.place(x=0,y=0)

#creating an entry box
entry=Entry(window, font=("Arial",20),fg='blue',bg='black')
entry.pack()

#creating a delete button
delete_button=Button(window,text="delete",font=("Arial",10),command=delete)
delete_button.pack()

#creating a button for search box
search_button=Button(window,text='submit',font=("Arial",10),command=search)
search_button.pack()

#creating a backspace button
backspace_button=Button(window,text='backspace', font=("Arial",10),command=backspace)
backspace_button.pack()

#creating a button, command=function name(call back)
play_button=Button(window,text='play',command=play)
play_button.pack(side=BOTTOM)

#creating a listbox
listbox=Listbox(window)
listbox.pack()
listbox.insert(1,'love story by TS')
listbox.insert(2,'Gorgeous by TS')
listbox.insert(3,'Style by TS')
listbox.insert(4,'Willow by TS')
listbox.insert(5,'Cardigan by TS')
listbox.insert(6,'You belong with me by TS')
listbox.config(height=listbox.size())

#creating a button for listbox submission
listbox_button=Button(window,text='submit', command=display)
listbox_button.pack()

window.mainloop()#places the window on the computer screen, listen for events
