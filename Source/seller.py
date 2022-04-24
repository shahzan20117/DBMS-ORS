from tkinter import *
import tkinter.messagebox as messageBox
import mysql.connector
import test
import re


## give the list of subcategories
def check_string_is_float(string_x, decimals):
    if (decimals == 2):
        regex = "[0]{1}\.[0-9]{1}|[0]{1}\.[0-9]{2}"
        if (re.fullmatch(regex, string_x)):
            return True
        else:
            return False
    elif(decimals == 1):
        regex = "[0]{1}\.[0-9]{1}"
        if (re.fullmatch(regex, string_x)):
            return True
        else:
            return False




def check_string_is_number(string_x):
    regex = "[0-9]+"
    if(re.fullmatch(regex, string_x)):
        return True
    else:
        return False



def give_product_id_name(seller_user, product_name_find, sub_category_find):
    cursor = seller_user.cursor()
    cursor.execute("SELECT product_id, product_name FROM product WHERE product_name = '{}' ".format( product_name_find ) )
    all_products = cursor.fetchall()
    seller_user.commit()
    return all_products

def give_all_subcategories(seller_user):
    cursor = seller_user.cursor()
    cursor.execute("SELECT sub_category FROM subCategory")
    all_subcategories = cursor.fetchall()
    seller_user.commit()
    return all_subcategories

    
## check email format
def check_email_format(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False
 


#################### SELLER TABLE MAN. ##############################################
def view_seller(Seller,seller_id):
    cursor = Seller.cursor()
    cursor.execute("Select seller_id, seller_name, curr_status, phone, email from seller where seller_id = " + str(seller_id))
    val = cursor.fetchall()
    rows = ["seller_id","seller_name","curr_status","phone","email"]
    data = {}
    for i in range(0,5):
        data[rows[i]] = val[0][i]
    return (data)


def view_seller_profile_page(seller_homepage, dba, seller_user, seller_id):
    seller_profile = view_seller(seller_user, seller_id)
    seller_homepage.destroy()
    seller_profile_page = Tk()
    seller_profile_page.title("seller profile")
    seller_profile_page.geometry("800x600")

    ## seller id
    seller_id_label = Label(seller_profile_page, text = "Seller Id", font = ("bold", 10))
    seller_id_label.place(x = 40, y = 40)

    seller_id_textbox = Entry()
    seller_id_textbox.insert(0, seller_profile["seller_id"])
    seller_id_textbox.place(x = 200, y = 40)
    seller_id_textbox.config(state = DISABLED)



    ## seller name  ==EDITABLE==
    seller_name = Label(seller_profile_page, text = "Seller Name", font = ("bold", 10))
    seller_name.place(x = 40, y = 80)

    seller_name_textbox = Entry()
    seller_name_textbox.insert(0, seller_profile["seller_name"])
    seller_name_textbox.place(x = 200, y = 80)

    ## seller curr status ==EDITABLE==
    new_curr_status = StringVar()
    new_curr_status.set(seller_profile["curr_status"])

    seller_curr = Label(seller_profile_page, text = "Seller Status", font = ("bold", 10))
    seller_curr.place(x = 40, y = 120)

    seller_curr_textbox = OptionMenu(seller_profile_page, new_curr_status, "WORKING", "NOT_WORKING")
    seller_curr_textbox.place(x = 200, y = 120)

    # seller_curr_textbox = Entry()
    # seller_curr_textbox.insert(0, seller_profile["curr_status"])
    # seller_curr_textbox.place(x = 200, y = 120)

    ##seller phone ==EDITABLE==
    seller_phone = Label(seller_profile_page, text = "Seller Phone", font = ("bold", 10))
    seller_phone.place(x = 40, y = 160)

    seller_phone_textbox = Entry()
    seller_phone_textbox.insert(0, seller_profile["phone"])
    seller_phone_textbox.place(x = 200, y = 160)

    ##seller email ==EDITABLE==
    seller_email = Label(seller_profile_page, text = "Seller Email", font = ("bold", 10))
    seller_email.place(x = 40, y = 200)

    seller_email_textbox = Entry()
    seller_email_textbox.insert(0, seller_profile["email"])
    seller_email_textbox.place(x = 200, y = 200)

    # ## store input
    # new_seller_name = seller_name_textbox.get()
    # new_seller_status = new_curr_status.get()
    # new_seller_phone = seller_phone_textbox.get()
    # new_seller_email = seller_email_textbox.get()

    ## logout button
    seller_logout_button = Button(seller_profile_page, text = "Log Out", font = ("bold", 10), bg = "red", command = lambda: test.go_to_seller_login_page(dba, seller_profile_page))
    seller_logout_button.place(x = 40, y = 270)

    ## update profile button
    seller_update_profile_button = Button(seller_profile_page, text = "Update Profile", font = ("bold", 10), bg = "lime", command = lambda: update_seller(seller_user,seller_id, seller_name_textbox.get(), new_curr_status.get(), seller_phone_textbox.get(), seller_email_textbox.get()))
    seller_update_profile_button.place(x = 200, y = 270)

    ## delete account button
    seller_delte_account_button = Button(seller_profile_page, text = "Delete Account", font = ("bold", 10), bg = "crimson", command = lambda: delete_seller(seller_user, seller_id))
    seller_delte_account_button.place(x = 400, y = 270)



    seller_profile_page.mainloop()









def update_seller(Seller,seller_id, seller_name, curr_status, seller_phone, seller_email):
    if ( seller_name == "" or curr_status == ""  or seller_phone == "" or seller_email == ""):
        messageBox.showinfo("error", "must not leave anything empty")
    elif (not seller_phone.isdigit()):
        messageBox.showinfo("error", "phone can only be number")
    elif (not check_email_format(seller_email)):
        messageBox.showinfo("error", "invalid email format")
    else:
        cursor = Seller.cursor()
        query = "UPDATE seller set seller_name = '{}', curr_status = '{}', phone = '{}', email = '{}' WHERE seller_id = '{}' ".format(seller_name, curr_status, seller_phone, seller_email, seller_id)
        cursor.execute(query)
        Seller.commit()
        messageBox.showinfo("YAY", "Updated Seller Profile")

def delete_seller(Seller,seller_id):
    cursor = Seller.cursor()
    cursor.execute("UPDATE seller SET curr_status = '{}' WHERE seller_id = '{}'".format("NOT_WORKING", seller_id) )
    Seller.commit()
    messageBox.showinfo("success", "account deleted")



#################### LISTING TABLE MAN. ##############################################

def view_list(Seller, seller_id):
    cursor = Seller.cursor()
    cursor.execute("Select * from view_listings where seller_id = " + str(seller_id))
    val = cursor.fetchall()
    return val
    # rows = ["seller_id","avg_rating","selling_cost","selling_quantity","discount","product_id","product_name","curr_status"]
    #              0              1             2               3               4           5             6             7
    # data = {}

    # for i in range(0,8):
    #     ar = []
    #     for j in range (0, len(val)):
    #         ar.append(str(val[j][i]))
    #     data[rows[i]] = ar
    # return (data)

def edit_particular_listing(seller_user, listing_discount, selling_cost, selling_quantity, listing_tuple):
    cursor = seller_user.cursor()
    seller_id = listing_tuple[0]
    product_id = listing_tuple[5]
    if (not check_string_is_float(listing_discount, 2)):
        messageBox.showinfo("error", "discount can only be float < 1 with 1 or 2 decimals")
    elif (not check_string_is_number(selling_cost) ):
        messageBox.showinfo("error", "cost can only be integer")
    elif (not check_string_is_number(selling_quantity)):
        messageBox.showinfo("error", "quantity can only be integer")
    else:
        query = "UPDATE sells SET selling_cost = '{}', selling_quantity = '{}', discount = '{}' WHERE seller_id = '{}' AND product_id = '{}' ".format(int(selling_cost), int(selling_quantity), float(listing_discount), int(seller_id), int(product_id) )
        cursor.execute(query)
        seller_user.commit()
        messageBox.showinfo("success", "listing updated successfully")




def view_listing_reviews(view_edit_particular_listing, seller_user, seller_id, product_id):
    view_edit_particular_listing.destroy()
    view_listing_reviews = Tk()
    view_listing_reviews.title("Listing Reviews")
    view_listing_reviews.geometry("800x600")

    review_tuples = view_rating(seller_user, seller_id, product_id)
    no_of_reviews_displayed = 0
    for i in review_tuples:
        review_button = Button(view_listing_reviews, text = "Reviewer Name: " + i[0] + " " + i[1] + "\nRating: " + str(i[2]) + "\nReview Comment: " + i[3] + "\nReview Date: " + str(i[4]) , font = ("bold", 10), bg = "white")
        review_button.grid(row = no_of_reviews_displayed, column = 0)
        no_of_reviews_displayed += 1




    





def view_edit_particular_listing(seller_listings_page, seller_user, listing_tuple):
    seller_listings_page.destroy()
    view_edit_particular_listing = Tk()
    view_edit_particular_listing.title("View and Edit Listing")
    view_edit_particular_listing.geometry("800x600")

    ## discount
    listing_discount = Label(view_edit_particular_listing, text = "Discount", font = ("bold", 10))
    listing_discount.place(x = 40, y = 40)

    listing_discount_textbox = Entry()
    listing_discount_textbox.insert(0, listing_tuple[4])
    listing_discount_textbox.place(x = 200, y = 40)

    ## selling cost
    selling_cost = Label(view_edit_particular_listing, text = "Selling Cost", font = ("bold", 10))
    selling_cost.place(x = 40, y = 80)

    selling_cost_textbox = Entry()
    selling_cost_textbox.insert(0, listing_tuple[2])
    selling_cost_textbox.place(x = 200, y = 80)
    
    ## selling quantity
    selling_quantity = Label(view_edit_particular_listing, text = "Selling Quantity", font = ("bold", 10))
    selling_quantity.place(x = 40, y = 120)

    selling_quantity_textbox = Entry()
    selling_quantity_textbox.insert(0, listing_tuple[3])
    selling_quantity_textbox.place(x = 200, y = 120)

    ## update button
    update_listing_button = Button(view_edit_particular_listing, text = "Update Listing", font = ("bold", 10), bg = "lime", command = lambda: edit_particular_listing(seller_user, listing_discount_textbox.get(), selling_cost_textbox.get(), selling_quantity_textbox.get(), listing_tuple))
    update_listing_button.place(x = 200, y = 160)

    ## delete lisiting
    delete_listing_button = Button(view_edit_particular_listing, text = "Delete Listing", font = ("bold", 10), bg = "red", command = lambda: delete_list(seller_user, int(listing_tuple[0]), int(listing_tuple[5])))
    delete_listing_button.place(x = 200, y = 200)

    ## view reviews button
    view_listing_review_button = Button(view_edit_particular_listing, text = "View Reviews", font = ("bold", 10), bg = "lime", command = lambda: view_listing_reviews(view_edit_particular_listing, seller_user, int(listing_tuple[0]), int(listing_tuple[5])))
    view_listing_review_button.place(x = 200, y = 240)



    view_edit_particular_listing.mainloop()



def add_listing(seller_user, seller_id, quantity, cost, discount, product_name, sub_category):
    if (quantity == "" or cost == "" or discount == "" or product_name == "" or sub_category == ""):
        messageBox.showinfo("error", "must not leave anything empty")
    elif( not ( check_string_is_number(quantity) ) ):
        messageBox.showinfo("error", "quantity can only be integer")
    elif(not check_string_is_number(cost)):
        messageBox.showinfo("error", "cost can only be integer")
    elif( not ( check_string_is_float(discount, 2) ) ):
        messageBox.showinfo("error", "discount should be float < 1 and 2 or 1 decimal places ")


    cursor1 = seller_user.cursor()
    query = "SELECT * FROM product WHERE product_name = '{}'".format(product_name)
    cursor1.execute(query)
    product_name_tuple_list = cursor1.fetchall()
    seller_user.commit()
    cursor1.close()
    ## if sells already has the entry


    if (len(product_name_tuple_list) == 0):
        cursor2 = seller_user.cursor()
        query = "INSERT INTO product(product_id, product_name, curr_status) VALUES (%s, %s, %s)"
        tuple = (None, product_name, "IN_STOCK")
        cursor2.execute(query, tuple)
        seller_user.commit()
        ## find the id inserted
        cursor2.execute("SELECT LAST_INSERT_ID()")
        inserted_product_id_tuple = cursor2.fetchall()
        inserted_product_id_value = inserted_product_id_tuple[0][0]
        print(inserted_product_id_tuple)
        seller_user.commit()

        ## find subcategory to be inserted
        print(sub_category)


        ## insert into belongsTo table
        query_belongTo = "INSERT INTO belongTo (product_id, sub_category) VALUES (%s, %s)"
        tuple_belongTo = (inserted_product_id_value, sub_category)
        cursor2.execute(query_belongTo, tuple_belongTo)
        seller_user.commit()

        ## insert into sells table
        query_sells = "INSERT INTO sells (seller_id, product_id, selling_cost, avg_rating, selling_quantity, discount) VALUES (%s, %s, %s, %s, %s, %s)"
        tuple_sells = (seller_id, inserted_product_id_value, cost, 0.00, quantity, discount)
        cursor2.execute(query_sells, tuple_sells)
        seller_user.commit()
        cursor2.close()

    else:
        ## find the product id first
        cursor3 = seller_user.cursor()
        query_id_4 = "SELECT product_id FROM product WHERE product_name = '{}'".format(product_name)
        cursor3.execute(query_id_4)
        id_tuple_list_4 = cursor3.fetchall()
        seller_user.commit()

        print(id_tuple_list_4)
        product_id_found_4 = id_tuple_list_4[0][0]

        ##check whether sells aready has that entry
        check_sells = "SELECT * FROM sells WHERE seller_id = '{}' AND product_id = '{}'".format(seller_id, product_id_found_4)
        cursor3.execute(check_sells)
        found_sells = cursor3.fetchall()
        seller_user.commit()
        print(found_sells)
        if (len(found_sells) != 0):
            messageBox.showinfo("error", "listing already exists you can update it ")
        else:
            ## product is already there in the product table
            cursor3.execute( "SELECT sub_category, product_name FROM products_Of_subCategory WHERE product_name = '{}'".format(product_name) )
            list_of_sub_category_and_product_name_tuples = cursor3.fetchall()
            seller_user.commit()

            print(list_of_sub_category_and_product_name_tuples) 

            ## find matching sub category
            name_category_found = False
            for i in list_of_sub_category_and_product_name_tuples:
                if ( i[0] == sub_category ):
                    name_category_found = True
                    break
            
            ## do the thing
            if (name_category_found == True):
                ## insert only in sells
                ## first find the product_id of the name_category_found
                query_id = "SELECT product_id FROM product WHERE product_name = '{}'".format(product_name)
                cursor3.execute(query_id)
                id_tuple_list = cursor3.fetchall()
                seller_user.commit()
                print(id_tuple_list)
                product_id_found = id_tuple_list[0][0]

                ## insert into sells table
                
                query_sells1 = "INSERT INTO sells (seller_id, product_id, selling_cost, avg_rating, selling_quantity, discount) VALUES (%s, %s, %s, %s, %s, %s)"
                tuple_sells1 = (seller_id, product_id_found, cost, 0.00, quantity, discount)
                cursor3.execute(query_sells1, tuple_sells1)
                seller_user.commit()
                cursor3.close()

            else:
                ## insert sells as well as blongTo
                ## find product_id
                query_id = "SELECT product_id FROM product WHERE product_name = '{}'".format(product_name)
                cursor3.execute(query_id)
                id_tuple_list = cursor3.fetchall()
                seller_user.commit()
                print(id_tuple_list)
                product_id_found = id_tuple_list[0][0]

                ## insert into sells table
                
                query_sells1 = "INSERT INTO sells (seller_id, product_id, selling_cost, avg_rating, selling_quantity, discount) VALUES (%s, %s, %s, %s, %s, %s)"
                tuple_sells1 = (seller_id, product_id_found, cost, 0.00, quantity, discount)
                cursor3.execute(query_sells1, tuple_sells1)
                seller_user.commit()

                ## insert into belongTo
                query_belongTo_1 = "INSERT INTO belongTo (product_id, sub_category) VALUES (%s, %s)"
                tuple_belongTo_1 = (product_id_found, sub_category)
                cursor3.execute(query_belongTo_1, tuple_belongTo_1)
                seller_user.commit()
                cursor3.close()



        

def add_listing_page(seller_homepage, dba, seller_user, seller_id):
    seller_homepage.destroy()
    add_listing_page = Tk()
    add_listing_page.title("add a new listing")
    add_listing_page.geometry("800x600")

    ## quantity
    selling_quantity = Label(add_listing_page, text = "Selling Quantity", font = ("bold", 10))
    selling_quantity.place(x = 40, y = 40)

    selling_quantity_textbox = Entry()
    selling_quantity_textbox.place(x = 200, y = 40)

    ## cost
    selling_cost = Label(add_listing_page, text = "Selling Cost", font = ("bold", 10))
    selling_cost.place(x = 40, y = 80)

    selling_cost_textbox = Entry()
    selling_cost_textbox.place(x = 200, y = 80)

    ## discount
    listing_discount = Label(add_listing_page, text = "Discount", font = ("bold", 10))
    listing_discount.place(x = 40, y = 120)

    listing_discount_textbox = Entry()
    listing_discount_textbox.place(x = 200, y = 120)

    ## product name
    listing_product_name = Label(add_listing_page, text = "Product Name", font = ("bold", 10))
    listing_product_name.place(x = 40, y = 160)

    listing_product_name_textbox = Entry()
    listing_product_name_textbox.place(x = 200, y = 160)

    ## product sub category
    all_subcategories = give_all_subcategories(seller_user)
    list_of_subcategories = []
    for i in all_subcategories:
        list_of_subcategories.append(i[0])


    sub_category = StringVar()

    choose_subcategory = Label(add_listing_page, text = "Choose category", font = ("bold", 10))
    choose_subcategory.place(x = 40, y = 200)

    choose_subcategory_menu = OptionMenu(add_listing_page, sub_category, *list_of_subcategories)
    choose_subcategory_menu.place(x = 200, y = 200)

    ## add listing button
    add_listing_button = Button(add_listing_page, text = "Add New Listing", font = ("bold", 10), bg = "lime", command = lambda: add_listing(seller_user, seller_id, selling_quantity_textbox.get(), selling_cost_textbox.get(), listing_discount_textbox.get(), listing_product_name_textbox.get(), sub_category.get() ))
    add_listing_button.place(x = 200, y = 270)

    add_listing_page.mainloop()













def display_seller_listings(seller_homepage, dba, seller_user, seller_id):
    seller_homepage.destroy()
    seller_listings_page = Tk()
    seller_listings_page.title("Seller Listings")
    seller_listings_page.geometry("800x600")


    seller_listings = view_list(seller_user, seller_id)
    no_of_listings_displayed = 0
    for i in seller_listings: ## i is tuple seller_seller_id","avg_rating","selling_cost","selling_quantity","discount","product_id","product_name","curr_status
        listing_button = Button(seller_listings_page, text = "Product Name: " + str(i[6]) + "\nDiscount: " + str(i[4]) + "\n Product Status: " + str(i[7]) + "\nSelling Quantity: " + str(i[3]) + "\nSelling Cost: " + str(i[2]) + "\nAverage Rating: " + str(i[1]), command = lambda: view_edit_particular_listing(seller_listings_page, seller_user, i) )
        listing_button.grid(row = no_of_listings_displayed, column = 0)
        no_of_listings_displayed += 1



def edit_list(Seller,seller_id, product_id,parameter,value):
    cursor = Seller.cursor()
    cursor.execute("update view_listings set " + str(parameter) + " = '" + str(value) + "' where seller_id = " + str(seller_id) + " and product_id = " +
                   str(product_id))
    Seller.commit()

def delete_list(Seller,seller_id, product_id):
    cursor = Seller.cursor()
    cursor.execute("delete from sells where seller_id = " + str(seller_id) + " and product_id = " + str(product_id))
    Seller.commit()


#################### RATING TABLE MAN. ##############################################

def view_rating(Seller, seller_id, product_id):
    cursor = Seller.cursor()
    cursor.execute("select first_name, last_name, rating, review_comment, review_date from reviews_for_seller_product where seller_id = " +
                   str(seller_id) +" and product_id = " + str(product_id))

    val = cursor.fetchall()
    return val

    # rows = ["first_name", "last_name", "rating", "review_comment", "review_date"]
    #             0             1           2           3                 4
    # data = {}

    # for i in range (0,5):
    #     ar = []
    #     for j in range (0,len(val)):
    #         ar.append(str(val[j][i]))

    #     data[rows[i]] = ar
    # return (data)

def display_seller_homepage(seller_login_page, dba, seller_user, seller_id):
    seller_login_page.destroy()
    seller_homepage = Tk()
    seller_homepage.title("seller homepage")
    seller_homepage.geometry("800x600")

    add_listing_button = Button(seller_homepage, text = "Add New Listing", font = ("bold", 10), bg = "white", command = lambda:  add_listing_page(seller_homepage, dba, seller_user, seller_id) )
    add_listing_button.place(x = 300, y = 300)

    view_listings_button = Button(seller_homepage, text = "View Listings", font = ("bold, 10"), bg = "white", command = lambda: display_seller_listings(seller_homepage, dba, seller_user, seller_id) )
    view_listings_button.place(x = 300, y = 200)

    view_profile_button = Button(seller_homepage, text = "View Profile", font = ("bold, 10"), bg = "white", command = lambda: view_seller_profile_page(seller_homepage, dba, seller_user, seller_id) )
    view_profile_button.place(x = 300, y = 400)
    




################################# MAIN ##############################################

def main(seller_login_page, dba, seller_id):
    Seller = mysql.connector.connect(host="localhost", user="seller", passwd="Seller_pass1@", database="ORS1")
    display_seller_homepage(seller_login_page, dba, Seller, seller_id)
    # edit_list(Seller,seller_id, 16, "avg_rating", "3.0")

# if __name__ == "__main__":
#     main(16)



## seller adds a listing

## seller will give only these things: 1.quantity  2.cost  3.discount          4.product_name  5.sub_category
## case1: the product name already exists in product table:
##            just fetch the product id from product table and insert into sells with avg rating = 0
##
## case2: the product name doesn't exist in product table:
##            add product to product table and add (product_id, subcategory) to belongs_to table
##
##            
##            
##            
##            
