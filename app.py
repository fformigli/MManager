#!/usr/bin/python
from gui import Login, MainMenu


class Main:
	def __init__(self):
		self.authentication_done = False
		self.authenticated_username = ""

		Login(self)

		if self.authentication_done:
			MainMenu(self)

if __name__ == "__main__":
	Main()
