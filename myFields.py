from Tkinter import *

def raise_frame(frame):
	frame.tkraise()

def goBack():
	raise_frame(loginPage)

def callback():
	if email.get() and name.get() and password.get():
		entries.append({email.get(): name.get()})
		name.delete(0, 1000)
		email.delete(0,1000)
		password.delete(0,1000)
	print entries
	raise_frame(sucesPage)

def clearText():
	name.delete(0,1000)
	email.delete(0, 1000)
	password.delete(0, 1000)

master = Tk()

loginPage = Frame(master)
sucesPage = Frame(master)

for frame in (loginPage, sucesPage):
	frame.grid(row=0, column=0, sticky='news')

entries = []

# create the labels
nLabel = Label(loginPage, text="Name")
eLabel = Label(loginPage, text="Email")
pLabel = Label(loginPage, text="Password")
nLabel.grid(row=0)
eLabel.grid(row=1)
pLabel.grid(row=2)

sLabel = Label(sucesPage, text="Success!")
sLabel.grid(row=0)
rButton = Button(sucesPage, text="RETURN", width=10, command=goBack)
rButton.grid(row=1)

# create the entries:
name = Entry(loginPage)
email = Entry(loginPage)
password = Entry(loginPage, show="*")
name.grid(row=0, column=1)
email.grid(row=1,column=1)
password.grid(row=2, column=1)

b = Button(loginPage, text="ENTER", width=10, command=callback)
b.grid(row=3, column=0)

c = Button(loginPage, text="CLEAR", width=10, command=clearText)
c.grid(row=3, column=1)

raise_frame(loginPage)
mainloop()
