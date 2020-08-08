import tkinter as tk     #importing library tkinter for gui
from tkinter import *
from functools import partial
import backend          #importing custom module named backend
n=0
def get_selected_row(): #function for retriving number from entry
      pass
def sum(num):
    global n
    n=int(num.get())
    list.delete(0,n)
def view_command():  #function for retriving and showing entry in a listbox
    global n
    End=n
    i=0
    for rows in  backend.view():
                if(i<n):
                      list.insert(End,rows)
                i=i+1            

win=Tk()  #creating window
win.wm_title('FETCHING REQUIRED DATA FROM LIST')
win.geometry('400x200')
l1=Label(win,text='Enter a number') #creating label
l1.grid(row=0,column=0)
num=StringVar()
e1=Entry(win,textvariable=num)
e1.grid(row=0,column=1)
sum=partial(sum,num)
b1=Button(win,text='Submit',width=12,pady=5,command=sum)#add command and button
b1.grid(row=1,column=1)
view_command=partial(view_command)
b2=Button(win,text='View',width=12,pady=5,command=view_command)#add command for view button
b2.grid(row=2,column=1)
list=Listbox(win,height=30,width=200,relief= GROOVE) #listbox
list.grid(row=4,column=0,rowspan=5,columnspan=5)
sb=Scrollbar(win)
sb.grid(row=4,column=5,rowspan=5)
list.bind('<<ListboxSelection>>',get_selected_row)
win.mainloop()
