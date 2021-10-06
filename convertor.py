from tkinter import *

App = Tk()
App.title('Length Convertor')
App.geometry('500x500')
scales = ['Meters', 'Inches', 'Foot']



_from = StringVar()

cho = Label(App, text="Choose Scale", font=('Times', 20), foreground="green")
cho.grid(row=0, column=0,  pady=5)

from_menu =OptionMenu(App,  _from, *scales)
from_menu.grid(row=0, column=1, pady=5, padx=25)

lbl = Label(App, text='To', font=('Times', 20), foreground='green')
lbl.grid(row=0, column=2)

to_ = StringVar()
to_menu = OptionMenu(App, to_, *scales)
to_menu.grid(row=0, column=3, pady=5, padx=25)


enterL = Label(App, text="Enter Length", font=('Times',20), foreground="green")
enterL.grid(row=1, column=0, columnspan=1, pady=5)


numE = Entry(App)
numE.grid(row=1, column=1, columnspan=2, pady=5, padx=25)


def convertor():
    From = _from.get()
    num = int(numE.get())
    To = to_.get()
    if From == 'Meters' and To == 'Inches':
        conv_num = num*39.37
    elif From == 'Meters' and To == 'Foot':
        conv_num = num * 3.28
    elif From == 'Inches' and To == 'Meters':
        conv_num = num / 39.37
    elif From == 'Inches' and To == 'Foot':
        conv_num = num / 12
    elif From == 'Foot' and To == 'Meters':
        conv_num = num / 3.28
    elif From == 'Foot' and To == 'Inches':
        conv_num = num * 12
    else:
        conv_num = num


    numL = Label(App, text=round(conv_num,2), width=10, font=('Times',20), foreground="red")
    numL.grid(row=1, column=3, columnspan=2, pady=5, padx=5)



conB = Button(App,text='Convert', command=convertor, font=('Times',15), foreground="white", background='grey')
conB.grid(row=2, column=0, pady=5, padx=50)


App.mainloop()




















