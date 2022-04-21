from tkinter import *
import tkinter.messagebox as messageBox
import mysql.connector

dba = mysql.connector.connect(host = "localhost", user = "root", passwd = "Hitsugaya1@", database = "ORS1")
# agent = mysql.connector.connect(host = "localhost",user = "agent",passwd = "Agent_pass1@", database = "ORS1")
seller = mysql.connector.connect(host = "localhost",user = "seller",passwd = "Seller_pass1@", database = "ORS1")


def confirm_customer_login(Logi_page, id, password):
    if (id == "" or password == ""):
        messageBox.showinfo("error", "must fill all the fields")
    elif (not id.isdigit()):
        messageBox.showinfo("error", "ids can only be numbers")
    elif (len(id) != len(str(int(id)))):
        messageBox.showinfo("error", "ids cannot have leading zeroes")
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
    elif (not id.isdigit()):
        messageBox.showinfo("error", "id must be numeric")
    elif (len(id) != len(str(int(id)))):
        messageBox.showinfo("error", "no leading zeroes allowed in id")


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

def display_customer_Login_Register_page(choose_user_page):
    choose_user_page.destroy()

    Loin_Register_page = Tk()
    Loin_Register_page.title("Amazon ki copy")
    Loin_Register_page.geometry("800x600")

    Register_button = Button(Loin_Register_page, text = "Register", font = ("bold, 15"), bg = "white", command = lambda : go_to_customer_register_page(Loin_Register_page))
    Login_button = Button(Loin_Register_page, text = "Login", font = ("bold, 15"), bg = "white", command = lambda : go_to_customer_login_page(Loin_Register_page))

    Login_button.place(x = 20, y = 140)
    Register_button.place(x = 20, y = 200)

    Loin_Register_page.mainloop()

def register_seller_account(seller_register_page, seller_name, seller_email, seller_password, seller_phone, seller_id ):
    print("heyo")



def go_to_seller_register_page(Loin_Register_page):
    Loin_Register_page.destroy()
    seller_register_page = Tk()
    seller_register_page.title("Amazon ki copy")
    seller_register_page.geometry("800x600")


    ## text for enter seller name 
    Enter_seller_name = Label(seller_register_page, text = "Enter Name", font = ("bold", 10))
    Enter_seller_name.place(x = 30, y = 40)
    seller_textbox = Entry()
    seller_textbox.place(x = 260, y = 40)

    ## text for enter seller email
    Enter_email = Label(seller_register_page, text = "Enter Email", font = ("bold", 10))
    Enter_email.place(x = 30, y = 80)
    Enter_email_textbox = Entry()
    Enter_email_textbox.place(x = 260, y = 80)

    ## text for enter seller password
    Enter_seller_password = Label(seller_register_page, text = "Enter password", font = ("bold", 10))
    Enter_seller_password.place(x = 30, y = 120)
    seller_password_textbox = Entry()
    seller_password_textbox.place(x = 260, y = 120)

    ## text for enter seller phone
    Enter_phone = Label(seller_register_page, text = "Enter phone", font = ("bold", 10))
    Enter_phone.place(x = 30, y = 160)
    phone_textbox = Entry()
    phone_textbox.place(x = 260, y = 160)

    ## enter seller id
    Enter_id = Label(seller_register_page, text = "Enter id", font = ("bold", 10))
    Enter_id.place(x = 30, y = 160)
    id_textbox = Entry()
    id_textbox.place(x = 260, y = 200)

    ## register button
    seller_Register_button = Button(seller_register_page, text = "Register", font = ("bold", 10), bg = "white", command = lambda: register_seller_account(seller_register_page, seller_textbox.get(), Enter_email_textbox.get(), seller_password_textbox.get(), phone_textbox.get(), id_textbox.get() ) )
    seller_Register_button.place(x = 200, y = 240)




    seller_register_page.mainloop()

def confirm_seller_login(seller_login_page, seller_id, seller_password):
    pass



def go_to_seller_login_page(Loin_Register_page):
    Loin_Register_page.destroy()
    seller_login_page = Tk()
    seller_login_page.title("Amazon ki copy")
    seller_login_page.geometry("800x600")

    ## text and textbox for enter id
    Enter_id = Label(seller_login_page, text = "Enter id", font = ("bold", 10))
    Enter_id.place(x = 30, y = 40)
    Enter_id_textbox = Entry()
    Enter_id_textbox.place(x = 260, y = 40)

    ## text and textbox for enter password
    Enter_password = Label(seller_login_page, text = "Enter Password", font = ("bold", 10))
    Enter_password.place(x = 30, y = 80)
    Enter_password_textbox = Entry()
    Enter_password_textbox.place(x = 260, y = 80)

    ## Login button
    Login_button = Button(seller_login_page, text = "Login", font = ("bold", 10), bg = "white", command = lambda: confirm_seller_login(seller_login_page, Enter_id_textbox.get(), Enter_password_textbox.get()))
    Login_button.place(x = 200, y = 200)



    Login_page.mainloop()
    
pass








def display_seller_Login_Register_page(choose_user_page):
    choose_user_page.destroy()
    Loin_Register_page = Tk()
    Loin_Register_page.title("Amazon ki copy")
    Loin_Register_page.geometry("800x600")

    Register_button = Button(Loin_Register_page, text = "Register", font = ("bold, 15"), bg = "white", command = lambda : go_to_seller_register_page(Loin_Register_page))
    Login_button = Button(Loin_Register_page, text = "Login", font = ("bold, 15"), bg = "white", command = lambda : go_to_seller_login_page(Loin_Register_page))

    Login_button.place(x = 20, y = 140)
    Register_button.place(x = 20, y = 200)

    Loin_Register_page.mainloop()


# ###############################################################################################
# def delete_agent_profile():
#     ### ................ Shahzan !!!


# ###############################################################################################


# ###############################################################################################
# # def agent_current_order():
# #     ### ................ Shahzan !!!


# ###############################################################################################

# ###################################################################################################
# def agent_post_profile(page_to_destroy):

#     page_to_destroy.destroy()
#     profile_page = Tk()
#     profile_page.title("Profile Page")
#     profile_page.geometry("800x600")
#     delete_account_button = Button(agent_post,text = "Profile",font = ("bold,15"),bg = "white",command = lambda:delete_agent_profile(profile_page))
#     edit_profile_or_logout_button = Button(agent_post,text = "Edit Profile Or Logout",font = ("bold,15"),bg = "white",command = lambda:agent_current_order(profile_page))



# ###################################################################################################

# ###################################################################################################
# def agent_current_order():


# ###################################################################################################

# ######################################################################################################

# def agent_post_page(somethinghere):
#     somethinghere.destroy()
#     agent_post = Tk()
#     agent_post.title("Agent Post Details")
#     agent_post.geometry("800x600")

#     profile_button = Button(agent_post,text = "Profile",font = ("bold,15"),bg = "white",command = lambda:agent_post_profile(agent_post,...))
#     current_orders_button = Button(agent_post,text = "Current Orders",font = ("bold,15"),bg = "white",command = lambda:agent_current_order(agent_post,...))

#     profile_button.place(x = 20,y=140)
#     current_orders_button.place(x = 20, 200)

# ######################################################################################################

# #######################################################################################################

# def register_agent_account(register_agent_account_page,name,email,passwd,id,phone):
#     register_agent_account_page.destroy()
#     if (name == "" or email == "" or passwd == "" or id == "" or phone == ""):
#         messageBox.showinfo("error", "must fill all the fields")
#     elif (not id.isdigit()):
#         messageBox.showinfo("error", "id must be numeric")
#     elif (len(id) != len(str(int(id)))):
#         messageBox.showinfo("error", "no leading zeroes allowed in id")




# #######################################################################################################

# #######################################################################################################

# def go_to_agent_register_page(Loin_agent_Register_page):
#     Loin_agent_Register_page.destroy()
#     Register_page = Tk()
#     Register_page.title("Register page")
#     Register_page.geometry("800x600")
#     ## text for enter first name 
#     Enter_first_name = Label(Register_page, text = "Enter Agent Name", font = ("bold", 10))
#     Enter_first_name.place(x = 30, y = 40)
#     first_name_textbox = Entry()
#     first_name_textbox.place(x = 260, y = 40)

#     ## text for enter the email
#     Enter_email = Label(Register_page, text = "Email", font = ("bold", 10))
#     Enter_email.place(x = 30, y = 80)
#     email_textbox = Entry()
#     email_textbox.place(x = 260, y = 80)

#     ## text for enter password
#     Enter_password = Label(Register_page, text = "Enter password", font = ("bold", 10))
#     Enter_password.place(x = 30, y = 120)
#     password_textbox = Entry()
#     password_textbox.place(x = 260, y = 120)

#     ## text for enter id
#     Enter_id = Label(Register_page, text = "Enter Agent id", font = ("bold", 10))
#     Enter_id.place(x = 30, y = 160)
#     id_textbox = Entry()
#     id_textbox.place(x = 260, y = 160)

#     ## text for phone
#     phone = Label(Register_page, text = "Enter Phone No", font = ("bold", 10))
#     phone.place(x = 30, y = 200)
#     phone_textbox = Entry()
#     phone_textbox.place(x = 260, y = 200)

#     agent_register_button = Button(Register_page, text = "Register", font = ("bold, 15"), bg = "white", command = lambda : register_agent_account(Register_page, first_name_textbox.get(), email_textbox.get(), password_textbox.get(), id_textbox.get(), phone_textbox.get()))
#     agent_register_button.place(x = 200, y = 280)



# #################################################################################################################

# ###################################################################

# def display_agent_homepage(choose_user_page):
#     choose_user_page.destroy()
#     Loin_agent_Register_page = Tk()
#     Loin_agent_Register_page.title("Amazon ki copy")
#     Loin_agent_Register_page.geometry("800x600")

#     Register_button = Button(Loin_agent_Register_page, text = "Register", font = ("bold, 15"), bg = "white", command = lambda : go_to_agent_register_page(Loin_agent_Register_page))
#     Login_button = Button(Loin_agent_Register_page, text = "Login", font = ("bold, 15"), bg = "white", command = lambda : go_to_agent_login_page(Loin_agent_Register_page))

#     Login_button.place(x = 20, y = 140)
#     Register_button.place(x = 20, y = 200)

#     Loin_agent_Register_page.mainloop()

# ####################################################################


def display_choose_user_page():
    choose_user_page = Tk()
    choose_user_page.title("choose user")
    choose_user_page.geometry("800x600")

    customer_button = Button(choose_user_page, text = "Customer", font = ("bold", 10), bg = "white", command = lambda : display_customer_Login_Register_page(choose_user_page))
    agent_button = Button(choose_user_page, text = "Shipping Agent", font = ("bold", 10), bg = "white", command = lambda : display_agent_homepage(choose_user_page))
    seler_page = Button(choose_user_page, text = "Seller", font = ("bold", 10), bg = "white", command = lambda : display_seller_Login_Register_page(choose_user_page))
    
    customer_button.place(x = 400, y = 100)
    agent_button.place(x = 400, y = 300)
    seler_page.place(x = 400, y = 500)

    choose_user_page.mainloop()

display_choose_user_page()

