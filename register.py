from tkinter import * 

def register():
	screen1 = Toplevel1(screen)
	screen1.title("Register")
	screen1.geometry("300x250")

	username = StrinVar()
	password = StrinVar()

	Label(screen1, text = "Username * ").pack()
	Entry(screen1, textvariable = username)
	Label(screen1, text = "Password * ").pack()
	Entry(screen1, textvariable = password)


def login():
	print("Login session started")

def main_screen():
	global screen
	screen = Tk()
	screen.geometry("300x250")
	screen.title("Notes 1.0")
	Label(text = "Notes 1.0", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
	Label(text = "").pack()
	Button(text = "Login", height = "2", width = "30", command = login).pack()
	Label(text = "").pack()
	Button(text = "Register", height = "2", width = "30", command = register).pack()

	screen.mainloop()

main_screen()