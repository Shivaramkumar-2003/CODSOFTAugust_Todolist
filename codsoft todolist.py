import tkinter
from tkinter import *
from tkinter import messagebox
l = []
c = 1
def entryError():
    if insertField.get() == "":
        messagebox.showerror("Error!. Please give input again")
        return 0
    return 1
def insertTask():
    global c
    value = entryError()
    if (value == 0):
        return
    var = insertField.get() + "\n"
    l.append(var)
    TextArea.insert('end -1 chars', str(c) + "---> " + var)
    c = c + 1
    del_tf()
def del_nf():
    nf.delete(0.0, END)
def del_tf():
    insertField.delete(0, END)
def delete():
    global c
    if (len(l) == 0):
        messagebox.showerror("There are no tasks")
        return
    number = nf.get(1.0, END)
    if (number == "\n"):
        messagebox.showerror("input error")
        return
    else:
        task_no = int(number)
    del_nf()
    l.pop(task_no - 1)
    c = c - 1
    TextArea.delete(1.0, END)
    for i in range(len(l)):
        TextArea.insert('end -1 chars', str(i + 1) + "---> " + l[i])
if (__name__ == "__main__"):
    window = Tk()
    window.configure(background="black")
    window.title("CODSOFT TodoList")
    window.geometry("350x350")
    enterTask = Label(window, text="Enter your Tasks", bg="yellow")
    insertField = Entry(window)
    Submit = Button(window, text="Submit", fg="Black", bg="light green", command=insertTask)
    TextArea = Text(window, height=8, width=30, font="times 13")
    taskNumber = Label(window, text="Remove Task number", bg="cyan")
    nf = Text(window, height=1, width=5, font="times 13")
    delete = Button(window, text="Delete", fg="Black", bg="orange", command=delete)
    Exit = Button(window, text="X", fg="Black", bg="Red", command=exit)
    enterTask.grid(row=0, column=2)
    insertField.grid(row=1, column=2, ipadx=30)
    Submit.grid(row=2, column=2)
    TextArea.grid(row=3, column=2, padx=10, sticky=W)
    taskNumber.grid(row=4, column=2, pady=5)
    nf.grid(row=5, column=2)
    delete.grid(row=6, column=2, pady=5)
    Exit.grid(row=7, column=10)

    window.mainloop()