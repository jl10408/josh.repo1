#Josh LIgon 2.9 Assignment 3
import tkinter as tk
from tkinter import messagebox

def displayData():
    first = entFirst.get()
    last = entLast.get()
    email = entEmail.get()
    phone = entPhone.get()
    messagebox.showinfo("Welcome to tkinter, " + first, "You entered:\nName: " + first + " " + last + "\nEmail: " + email + "\nPhone: " + phone)

def clear():
    entFirst.delete(0, tk.END)
    entLast.delete(0, tk.END)
    entEmail.delete(0, tk.END)
    entPhone.delete(0, tk.END)





root = tk.Tk()
root.title("tkinter Form")
root.geometry("500x300")

lblFrPerson = tk.LabelFrame(root, text="Personal Infomation")
lblFrPerson.pack()

lblFirst = tk.Label(lblFrPerson, text="*First Name:", bg="blue", fg="white")
lblFirst.grid(column= 0, row= 0)
entFirst = tk.Entry(lblFrPerson)
entFirst.grid(column= 1, row= 0)
lblLast = tk.Label(lblFrPerson, text="*Last Name:", bg="blue", fg="white")
lblLast.grid(column= 0, row= 1)
entLast = tk.Entry(lblFrPerson)
entLast.grid(column= 1, row= 1)
lblEmail = tk.Label(lblFrPerson, text="Email:")
lblEmail.grid(column= 0, row= 2)
entEmail = tk.Entry(lblFrPerson)
entEmail.grid(column= 1, row= 2)
lblPhone = tk.Label(lblFrPerson, text="Phone:")
lblPhone.grid(column= 0, row= 3)
entPhone = tk.Entry(lblFrPerson)
entPhone.grid(column= 1, row= 3)

fraButtons = tk.Frame(root)
fraButtons.pack()
btnS = tk.Button(fraButtons, text="Submit", width=5, command=displayData)
btnS.pack(side=tk.LEFT)
btnR = tk.Button(fraButtons, text="Reset", width=5, command=clear)
btnR.pack(side=tk.LEFT)
btnQ = tk.Button(fraButtons, text="Quit", width=5, command=root.destroy)
btnQ.pack(side=tk.LEFT)

root.mainloop()
