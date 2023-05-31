from tkinter import*

def display():
    if(x.get()==1):
        print("You agree")
    else:
        print("You dont agree")


window=Tk()
x=IntVar()

#creating a check button
check_button=Checkbutton(window,text="I agree",variable=x,onvalue=1,offvalue=0)
check_button.pack()

window.mainloop()
