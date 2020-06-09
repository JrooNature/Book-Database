from tkinter import *
from backend import Database

database = Database("books.db")

def get_selected_row(event):
    try:
        global selected_tuple   # By declaring this variable "global" we don't need to return it. It can be accessed anywhere
        
        index = booklist.curselection()[0] 
        selected_tuple = booklist.get(index)
        
        titleE.delete(0,END)
        yearE.delete(0,END)
        authorE.delete(0,END)
        isbnE.delete(0,END)

        titleE.insert(END,selected_tuple[1])
        authorE.insert(END,selected_tuple[2])
        yearE.insert(END,selected_tuple[3])
        isbnE.insert(END,selected_tuple[4])
    except IndexError:
        pass



def view_command():
    booklist.delete(0,END)
    for row in database.view():
        booklist.insert(END, row)

def search_command():
    booklist.delete(0,END)
    for row in database.search(title_text.get(),author_text.get(), year_text.get(), isbn_text.get()):
        booklist.insert(END, row)

def add_command():
    booklist.delete(0,END)
    database.insert(title_text.get(),author_text.get(), year_text.get(), isbn_text.get())
    booklist.insert(END, (title_text.get(),author_text.get(), year_text.get(), isbn_text.get()))

def delete_command():
    database.delete(selected_tuple[0])
    view_command()

def update_command():
    database.update(selected_tuple[0], title_text.get(),author_text.get(), year_text.get(), isbn_text.get())
    view_command()
    


window = Tk()

window.wm_title("BookStore")

titleL = Label(window, text='Title')
titleL.grid(row=0, column=0, sticky=E)
title_text = StringVar()
titleE = Entry(window, textvariable=title_text)
titleE.grid(row=0, column=1, pady=5)

yearL = Label(window, text='Year')
yearL.grid(row=1, column=0, sticky=E)
year_text = StringVar()
yearE = Entry(window, textvariable=year_text)
yearE.grid(row=1, column=1, pady=5)

authorL = Label(window, text='Author')
authorL.grid(row=0, column=2)
author_text = StringVar()
authorE = Entry(window, textvariable=author_text)
authorE.grid(row=0, column=3, pady=5, padx=5)

isbnL = Label(window, text='ISBN')
isbnL.grid(row=1, column=2)
isbn_text = StringVar()
isbnE = Entry(window, textvariable=isbn_text)
isbnE.grid(row=1, column=3, pady=5, padx=5)

scroll = Scrollbar(window, orient=VERTICAL)
booklist = Listbox(window, height=10, width=50, yscrollcommand=scroll.set)
booklist.grid(row=2, column=0, rowspan=6, columnspan=2, padx=5, pady=5)
booklist.bind('<<ListboxSelect>>', get_selected_row)
scroll.grid(row=2, column=2, rowspan=6)
scroll.config(command=booklist.yview)


viewAllB = Button(window, text='View All', width=12, command=view_command)
viewAllB.grid(row=2, column=3)

searchEntryB = Button(window, text='Search Entry', width=12, command=search_command)
searchEntryB.grid(row=3, column=3)

addEntryB = Button(window, text='Add Entry', width=12, command=add_command)
addEntryB.grid(row=4, column=3)

updateB = Button(window, text='Update Selected', width=12, command=update_command)
updateB.grid(row=5, column=3)

deleteB = Button(window, text='Delete Selected', width=12, command=delete_command)
deleteB.grid(row=6, column=3)

closeB = Button(window, text='Close', width=12, command=window.destroy)
closeB.grid(row=7, column=3, pady=8)


window.mainloop()