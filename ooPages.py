import Tkinter as tk
from threading import Thread
import time

entries = []

class Page(tk.Frame):
	def __init__(self, *args, **kwargs):
		tk.Frame.__init__(self, *args, **kwargs)
	def show(self):
		self.lift()

class LoginScreen(Page):
	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)

		# using trace on the status as a wonky way to get changes when a form is submitted
		# self.status = tk.IntVar()
		# self.status.set(1)
		# print self.status.get()

		self.status = tk.StringVar()
		self.status.set("working")
		print self.status.get()

		def clearText():
			name.delete(0,1000)
			email.delete(0,1000)
			password.delete(0,1000)
		
		def submitEntry():
			print "login status before submission", self.status.get()
			if email.get() and name.get() and password.get():
				entries.append([email.get(), name.get(), password.get()])
				clearText()
				print entries
				self.status.set("done")
				print self.status.get()
				# self.status.set(0)	# change the status - this will prompt trace, which will call to go to the success screen
									# we only want to change the status if the form was submitted
									# otherwise, let the status stay the same	
		# labels
		nLabel = tk.Label(self, text="Name")
		eLabel = tk.Label(self, text="Email")
		pLabel = tk.Label(self, text="Password")
		nLabel.grid(row=0)
		eLabel.grid(row=1)
		pLabel.grid(row=2)
		
		# entries
		name = tk.Entry(self)
		email = tk.Entry(self)
		password = tk.Entry(self, show="*")
		name.grid(row=0, column=1)
		email.grid(row=1,column=1)
		password.grid(row=2, column=1)
		
		#buttons
		enter = tk.Button(self, text="ENTER", width=10, command=submitEntry)
		enter.grid(row=3, column=0)
		clear = tk.Button(self, text="CLEAR", width=10, command=clearText)
		clear.grid(row=3, column=1)

class SuccessScreen(Page):
	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)
		self.status = tk.IntVar()
		self.status.set(1)

		def goBackLogin():
			self.status.set(0)
			self.status.set(1)

		def continueGoing():
			self.status.set(2)

		message = tk.Label(self, text="Success!")
		retButton = tk.Button(self, text="Go Back", width=10, command=goBackLogin)
		retButton.pack()
		continueButton = tk.Button(self, text="continue", width=10, command=continueGoing)
		continueButton.pack()


class NextScreen(Page):
	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)
		message = tk.Label(self, text="Third page")
		message.pack()

class MainView(tk.Frame):
	def __init__(self, *args, **kwargs):
		tk.Frame.__init__(self, *args, **kwargs)

		def goToSuccess(arg1, arg2, arg3):
			if login.status.get() == "done":		# if the login page's status was changed (if the form was submitted)
				success.show()				# show the success page

		def afterLogin(arg1,arg2,arg3):
			if success.status.get() == 1:
				login.show()
				login.status.set("working")
				print "login status", login.status.get()
			elif success.status.get() == 2:
				third.show()
				print "login status", login.status.get()

		login = LoginScreen(self)
		success = SuccessScreen(self)
		third = NextScreen(self)

		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)

		login.place(in_=container,   x=0, y=0, relwidth=1, relheight=1)
		success.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
		third.place(in_=container, 	 x=0, y=0, relwidth=1, relheight=1)

		login.status.trace('w', goToSuccess)		# if login status is changed, go to success
		success.status.trace('w', afterLogin)	# if succes's status is changed, return to login

		login.show()

if __name__ == "__main__":
	root = tk.Tk()
	main = MainView(root)
	main.pack(side="top", fill="both", expand=True)
	root.wm_geometry("400x400")
	root.mainloop()