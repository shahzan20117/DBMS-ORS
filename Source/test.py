from tkinter import *
import mysql.connector

def go_to_register_page(Loin_Register_page):
    Loin_Register_page.destroy()
    Register_page = Tk()
    Register_page.title("Register page")
    Register_page.geometry("800x600")
    
    Register_page.mainloop()
    
    

def go_to_login_page(Login_register_page):
    Login_register_page.destroy()


Loin_Register_page = Tk()
Loin_Register_page.title("Amazon ki copy")
Loin_Register_page.geometry("800x600")

Register_button = Button(Loin_Register_page, text = "Register", font = ("bold, 15"), bg = "white", command = lambda : go_to_register_page(Loin_Register_page))
Login_button = Button(Loin_Register_page, text = "Login", font = ("bold, 15"), bg = "white", command = lambda : go_to_login_page(Loin_Register_page))

Login_button.place(x = 20, y = 140)
Register_button.place(x = 20, y = 200)

Loin_Register_page.mainloop()