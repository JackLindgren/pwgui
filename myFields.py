from Tkinter import *

# this will explain roughly how to do pages
# http://stackoverflow.com/questions/14817210
master = Tk()

entries = []

nLabel = Label(master, text="Name")
eLabel = Label(master, text="Email")
pLabel = Label(master, text="Password")
nLabel.grid(row=0)
eLabel.grid(row=1)
pLabel.grid(row=2)

name = Entry(master)
email = Entry(master)
password = Entry(master, show="*")
name.grid(row=0, column=1)
email.grid(row=1,column=1)
password.grid(row=2, column=1)

def callback():
	if email.get() and name.get() and password.get():
		entries.append({email.get(): name.get()})
		name.delete(0, 1000)
		email.delete(0,1000)
		password.delete(0,1000)
	print entries

def clearText():
	name.delete(0,1000)
	email.delete(0, 1000)
	password.delete(0, 1000)

b = Button(master, text="ENTER", width=10, command=callback)
b.grid(row=3, column=0)

c = Button(master, text="CLEAR", width=10, command=clearText)
c.grid(row=3, column=1)

mainloop()
