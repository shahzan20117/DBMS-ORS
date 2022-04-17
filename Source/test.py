from tkinter import *
import tkinter.messagebox as messageBox
import mysql.connector

dba = mysql.connector.connect(host = "localhost", user = "root", passwd = "Hitsugaya1@", database = "ORS1")

def confirm_customer_login(Logi_page, id, password):
    if (id == "" or password == ""):
        messageBox.showinfo("error", "must fill all the fields")
    else:
        cursor = dba.cursor()
        cursor.execute("SELECT customer_id, customer_password FROM customer")
        possible_login_credentials = cursor.fetchall()
        print(possible_login_credentials)
        if (int(id), password) in possible_login_credentials:
            messageBox.showinfo("Log in successfull", "YAY!")
        else:
            messageBox.showinfo("Log in Unsuccessful", "wrong id or password")



def register_customer_account(Register_page, first_name, last_name, password, id):
    if (first_name == "" or last_name == "" or password == "" or id == ""):
        messageBox.showinfo("error", "must fill all the fields")
    else:
        int_id = int(id)
        cursor = dba.cursor()
        cursor.execute("SELECT customer_id FROM customer")
        existing_cust_ids = cursor.fetchall()
        print(existing_cust_ids)
        if (int_id,) in existing_cust_ids:
            messageBox.showinfo("error", "id already taken, try again")
        else:
            query = "INSERT INTO customer (customer_id, first_name, last_name, wallet, customer_password) VALUES(%s, %s, %s, %s, %s)"
            tuple = (int_id, first_name, last_name, 0, password)
            cursor.execute(query, tuple)
            dba.commit()
            messageBox.showinfo("account added", "registered successfully \n      your id is: " + str(int_id))
            go_to_customer_login_page(Register_page)




            





def go_to_customer_register_page(Loin_Register_page):
    Loin_Register_page.destroy()
    Register_page = Tk()
    Register_page.title("Register page")
    Register_page.geometry("800x600")
    ## text for enter first name 
    Enter_first_name = Label(Register_page, text = "Enter First Name", font = ("bold", 10))
    Enter_first_name.place(x = 30, y = 40)
    first_name_textbox = Entry()
    first_name_textbox.place(x = 260, y = 40)

    ## text for enter last name
    Enter_last_name = Label(Register_page, text = "Enter Last Name", font = ("bold", 10))
    Enter_last_name.place(x = 30, y = 80)
    last_name_textbox = Entry()
    last_name_textbox.place(x = 260, y = 80)

    ## text for enter password
    Enter_password = Label(Register_page, text = "Enter password", font = ("bold", 10))
    Enter_password.place(x = 30, y = 120)
    password_textbox = Entry()
    password_textbox.place(x = 260, y = 120)

    ## text for enter id
    Enter_id = Label(Register_page, text = "Enter id", font = ("bold", 10))
    Enter_id.place(x = 30, y = 160)
    id_textbox = Entry()
    id_textbox.place(x = 260, y = 160)

    ## register button
    Register_button = Button(Register_page, text = "Register", font = ("bold", 10), bg = "white", command = lambda: register_customer_account(Register_page, first_name_textbox.get(), last_name_textbox.get(), password_textbox.get(), id_textbox.get()) )
    Register_button.place(x = 200, y = 200)




    Register_page.mainloop()
    
    

def go_to_customer_login_page(Login_register_page):
    Login_register_page.destroy()
    Login_page = Tk()
    Login_page.title("Login page")
    Login_page.geometry("800x600")

    ## text and textbox for enter id
    Enter_id = Label(Login_page, text = "Enter id", font = ("bold", 10))
    Enter_id.place(x = 30, y = 40)
    Enter_id_textbox = Entry()
    Enter_id_textbox.place(x = 260, y = 40)

    ## text and textbox for enter password
    Enter_password = Label(Login_page, text = "Enter Password", font = ("bold", 10))
    Enter_password.place(x = 30, y = 80)
    Enter_password_textbox = Entry()
    Enter_password_textbox.place(x = 260, y = 80)

    ## Login button
    Login_button = Button(Login_page, text = "Login", font = ("bold", 10), bg = "white", command = lambda: confirm_customer_login(Login_page, Enter_id_textbox.get(), Enter_password_textbox.get()))
    Login_button.place(x = 200, y = 200)



    Login_page.mainloop()

def display_customer_homepage(choose_user_page):
    choose_user_page.destroy()

    Loin_Register_page = Tk()
    Loin_Register_page.title("Amazon ki copy")
    Loin_Register_page.geometry("800x600")

    Register_button = Button(Loin_Register_page, text = "Register", font = ("bold, 15"), bg = "white", command = lambda : go_to_customer_register_page(Loin_Register_page))
    Login_button = Button(Loin_Register_page, text = "Login", font = ("bold, 15"), bg = "white", command = lambda : go_to_customer_login_page(Loin_Register_page))

    Login_button.place(x = 20, y = 140)
    Register_button.place(x = 20, y = 200)

    Loin_Register_page.mainloop()

def display_seller_homepage(choose_user_page):
    choose_user_page.destroy()
    Loin_Register_page = Tk()
    Loin_Register_page.title("Amazon ki copy")
    Loin_Register_page.geometry("800x600")

    Register_button = Button(Loin_Register_page, text = "Register", font = ("bold, 15"), bg = "white", command = lambda : go_to_register_page(Loin_Register_page))
    Login_button = Button(Loin_Register_page, text = "Login", font = ("bold, 15"), bg = "white", command = lambda : go_to_login_page(Loin_Register_page))

    Login_button.place(x = 20, y = 140)
    Register_button.place(x = 20, y = 200)

    Loin_Register_page.mainloop()

def display_agent_homepage(choose_user_page):
    choose_user_page.destroy()
    Loin_Register_page = Tk()
    Loin_Register_page.title("Amazon ki copy")
    Loin_Register_page.geometry("800x600")

    Register_button = Button(Loin_Register_page, text = "Register", font = ("bold, 15"), bg = "white", command = lambda : go_to_register_page(Loin_Register_page))
    Login_button = Button(Loin_Register_page, text = "Login", font = ("bold, 15"), bg = "white", command = lambda : go_to_login_page(Loin_Register_page))

    Login_button.place(x = 20, y = 140)
    Register_button.place(x = 20, y = 200)

    Loin_Register_page.mainloop()

def display_choose_user_page():
    choose_user_page = Tk()
    choose_user_page.title("choose user")
    choose_user_page.geometry("800x600")

    customer_button = Button(choose_user_page, text = "Customer", font = ("bold", 10), bg = "white", command = lambda : display_customer_homepage(choose_user_page))
    agent_button = Button(choose_user_page, text = "Shipping Agent", font = ("bold", 10), bg = "white", command = lambda : display_agent_homepage(choose_user_page))
    seler_page = Button(choose_user_page, text = "Seller", font = ("bold", 10), bg = "white", command = lambda : display_seller_homepage(choose_user_page))
    
    customer_button.place(x = 400, y = 100)
    agent_button.place(x = 400, y = 300)
    seler_page.place(x = 400, y = 500)

    choose_user_page.mainloop()

display_choose_user_page()



