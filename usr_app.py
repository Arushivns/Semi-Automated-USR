# Tkinter GUI application for Semi Automated USR

from tkinter import *
import subprocess as sub


#write all the event handling functions here
def Write_str_and_do_morph(event):
    sentence=etext.get()
    print(sentence)
    with open("str_test","w") as f:
        f.write(sentence.encode('utf-8'))
    sub.call('/home/arushi/PycharmProjects/mlpackage01/doMorphAnal.sh')


#the following line root=Tk() is used to create the window which will hold all the widgets..
root=Tk()



theLabel=Label(root,text="Create USR CSV",bg="red",fg="white")
theLabel.grid(row=0)

txt=Label(root,text="Enter a sentence divided in its respective groups")
txt.grid(row=1)

etext=Entry(root)
etext.grid(row=3)
submit=Button(text="Submit",fg="red")
submit.grid(row=4)
submit.bind("<Button-1>",Write_str_and_do_morph)




#to hold the GUI untill we press close button
root.mainloop()

