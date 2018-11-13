from tkinter import ttk,Tk,S,SE,E


class Login:
	"""Interfaz Login"""
	@staticmethod
	def authenticate(self):
		"""Autentica las credenciales ingresadas"""
		print("Autenticado!!")
		self.main.authentication_done = True
		self.main.autenticated_username = self.eusername.get()
		self.root.destroy()

	def __init__(self, main):
		self.main = main
		self.root = Tk()
		self.root.title("Login")
		self.root.geometry("300x120")

		self.frame = ttk.Frame(self.root, padding="10 10 5 5")

		self.lusername = ttk.Label(self.frame, text="Usuario:")
		self.lusername.grid(row=1, column=0, sticky=E)

		self.eusername = ttk.Entry(self.frame)
		self.eusername.grid(row=1, column=1)
		self.eusername.focus()

		self.lpassword = ttk.Label(self.frame, text="Contraseña:")
		self.lpassword.grid(row=2, column=0)

		self.epassword = ttk.Entry(self.frame, show="*")
		self.epassword.grid(row=2, column=1, pady=10)

		self.root.bind("<Return>", (lambda event:self.authenticate(self)))

		self.blogin = ttk.Button(self.frame, text="Entrar", command=(lambda:self.authenticate(self)))
		self.blogin.grid(row=4, columnspan=2)

		self.bcancel = ttk.Button(self.frame, text="Cancelar", command=(lambda:self.root.destroy()))
		self.bcancel.grid(row=4, column=3)

		self.frame.pack()
		self.root.mainloop()


class MainMenu:
	"""Interfaz Principal"""
	def __init__(self, main):
		self.main = main
		self.root = Tk()
		self.root.title = "MManager"
		self.root.geometry("800x600")

		self.frame = ttk.Frame(self.root, padding="10 10 5 5")

		#TODO: menukuera

		ttk.Label(self.frame, text=self.main.autenticated_username).grid(sticky=SE)

		self.frame.pack()
		self.root.mainloop()