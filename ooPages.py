import Tkinter as tk

entries = []

def show_page(page):
	page.tkraise()

class Page(tk.Frame):
	def __init__(self, *args, **kwargs):
		tk.Frame.__init__(self, *args, **kwargs)
	def show(self):
		self.lift()

class LoginScreen(Page):
	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)

		def clearText():
			name.delete(0,1000)
			email.delete(0,1000)
			password.delete(0,1000)
		
		def submitEntry():
			if email.get() and name.get() and password.get():
				entries.append([email.get(), name.get(), password.get()])
				clearText()
				print entries
				# success = SuccessScreen(self)
				# success.show()

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
		message = tk.Label(self, text="Success!")
		retButton = tk.Button(self, text="Go Back", width=10)
		retButton.pack()

class MainView(tk.Frame):
	def __init__(self, *args, **kwargs):
		tk.Frame.__init__(self, *args, **kwargs)
		login = LoginScreen(self)
		success = SuccessScreen(self)

		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		
		login.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
		success.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

		login.show()
		success.show()

		# login.show()
		# show(login)

# show_page(LoginScreen)
# show(LoginScreen)

# mainloop()

if __name__ == "__main__":
	root = tk.Tk()
	main = MainView(root)
	main.pack(side="top", fill="both", expand=True)
	root.wm_geometry("400x400")
	root.mainloop()