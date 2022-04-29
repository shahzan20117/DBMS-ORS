from tkinter import *
import tkinter.messagebox as messageBox
import mysql.connector
import test
import re

def view_customer_cart(page, customer_user, customer_id):
    page.destroy()
    customer_cart_page = Tk()
    customer_cart_page.title("Customer orders Page")
    customer_cart_page.geometry("800x600")
    ## fetch cutomer cart items
    cursor = customer_user.cursor()
    query = "SELECT place_status, delivery_status, return_status, orders_quantity, payment_method, final_cost, orders_date, address_line, delivery_date, product_name, seller_name, customer_id FROM cutomer_orders WHERE customer_id = '{}' AND place_status = '{}'".format(customer_id, "false")
    ##                 0                1                2             3               4               5           6            7               8            9            10           11
    cursor.execute(query)
    order_tuple_list = cursor.fetchall()
    customer_user.commit()

    ## show orders
    cart_shown = 0
    for i in order_tuple_list:
        rs = i[2] ## return status if null
        od = i[6] ## similarly oder date
        dd = i[8] ## again delivery date
        if (i[2] == None):
            rs = "---"
        if (i[6] == None):
            od = "---"
        if (i[8] == None):
            dd = "---"
        cart_button = Button(customer_cart_page, text = "place status: " + i[0] + "\ndelivery status: " + i[1] + "\nreturn status: " + rs + "\norder quantity: " + str(i[3]) +"\npayment method: " + i[4] + "\nfinal cost" + str(i[5]) + "\norder date:" + str(od) + "\naddress line: " +i[7] + "\ndelivery date: " + str(dd) + "\nproduct name: " + i[9] + "\nseller name: " + i[10], font = ("bold", 10), bg = "white", command = lambda: print("orders shown"))
        cart_button.grid(row = orders_shown, column = 0)
        cart_shown += 1
    customer_cart_page.mainloop()





def view_customer_orders(page, customer_user, customer_id):
    page.destroy()
    customer_orders_page = Tk()
    customer_orders_page.title("Customer orders Page")
    customer_orders_page.geometry("800x600")
    ## fetch customer order
    cursor = customer_user.cursor()
    query = "SELECT place_status, delivery_status, return_status, orders_quantity, payment_method, final_cost, orders_date, address_line, delivery_date, product_name, seller_name, customer_id FROM cutomer_orders WHERE customer_id = '{}' AND place_status = '{}'".format(customer_id, "true")
    ##                 0                1                2             3               4               5           6            7               8            9            10           11
    cursor.execute(query)
    order_tuple_list = cursor.fetchall()
    customer_user.commit()

    ## show orders
    orders_shown = 0
    for i in order_tuple_list:
        rs = i[2] ## return status if null
        od = i[6] ## similarly oder date
        dd = i[8] ## again delivery date
        if (i[2] == None):
            rs = "---"
        if (i[6] == None):
            od = "---"
        if (i[8] == None):
            dd = "---"
        order_button = Button(customer_orders_page, text = "place status: " + i[0] + "\ndelivery status: " + i[1] + "\nreturn status: " + rs + "\norder quantity: " + str(i[3]) +"\npayment method: " + i[4] + "\nfinal cost" + str(i[5]) + "\norder date:" + str(od) + "\naddress line: " +i[7] + "\ndelivery date: " + str(dd) + "\nproduct name: " + i[9] + "\nseller name: " + i[10], font = ("bold", 10), bg = "white", command = lambda: print("orders shown"))
        order_button.grid(row = orders_shown, column = 0)
        orders_shown += 1
    customer_orders_page.mainloop()

def view_customer_profile(page, customer_user, customer_id):
    page.destroy()
    customer_profile_page = Tk()
    customer_profile_page.title("Customer orders Page")
    customer_profile_page.geometry("800x600")
    ## fetch user profile
    cursor = customer_user.cursor()
    query = "SELECT first_name, last_name, wallet, customer_id FROM customer WHERE customer_id = '{}'".format(customer_id)
    ##                  0           1         2        3      
    cursor.execute(query)
    customer_profile = cursor.fetchall()
    customer_user.commit()
    cursor.close()


    ## customer_id
    customer_id_lable = Label(customer_profile_page, text = "Id", font = ("bold", 10))
    customer_id_lable.grid(row = 0, column = 0)
    customer_id_textbox = Entry()
    customer_id_textbox.insert(0, customer_profile[0][3])
    customer_id_textbox.grid(row = 0, column = 1)
    customer_id_textbox.config(state = DISABLED)

    ## user first name
    customer_first_name = Label(customer_profile_page, text = "first name", font = ("bold", 10))
    customer_first_name.grid(row = 1, column = 0)
    customer_first_name_textbox = Entry()
    customer_first_name_textbox.insert(0, customer_profile[0][0])
    customer_first_name_textbox.grid(row = 1, column = 1)

    ## user last name
    customer_last_name = Label(customer_profile_page, text = "last name", font = ("bold", 10))
    customer_last_name.grid(row = 2, column = 0)
    customer_last_name_textbox = Entry()
    customer_last_name_textbox.insert(0, customer_profile[0][1])
    customer_last_name_textbox.grid(row = 2, column = 1)

    ## wallet
    customer_wallet = Label(customer_profile_page, text = "wallet", font = ("bold", 10))
    customer_wallet.grid(row = 3, column = 0)
    customer_wallet_textbox = Entry()
    customer_wallet_textbox.insert(0, customer_profile[0][2])
    customer_wallet_textbox.grid(row = 3, column = 1)

    customer_profile_page.mainloop()

def see_reviews(page, customer_user, customer_id, product_id, seller_id):
    page.destroy()
    reviews_page = Tk()
    reviews_page.title("review page")
    reviews_page.geometry("800x600")

    ## create review lables
    cursor = customer_user.cursor()
    query = "SELECT * FROM Product_Reviews WHERE product_id = '{}' AND seller_id = '{}'".format(product_id, seller_id)
    cursor.execute(query)
    reviews = cursor.fetchall()
    customer_user.commit()
    cursor.close()
    ## display reviews
    reviews_displayed = 0
    for i in reviews:
        review_label = Label(reviews_page, text = "reviewer name: " + i[0] + " " + i[1] + "\nreview_comment: " + i[2] + "\nrating: " + str(i[3]) + "\nreview date: " + str(i[4]), bd = 1, relief = "sunken" )
        review_label.grid(row = reviews_displayed, column = 0)
        reviews_displayed += 1




def add_listing_to_cart(page, customer_user, customer_id, product_id, seller_id):
    page.destroy()
    add_to_cart = Tk()
    add_to_cart.title("seller options")
    add_to_cart.geometry("800x600")

    ## choose address label
    choose_address_label = Label(add_to_cart, text = "choose address: ", font = ("bold", 10))
    choose_address_label.grid(row = 0, column = 0)

    ## fetch address list of customer
    cursor = customer_user.cursor()
    query = "SELECT * FROM shippingInfo WHERE customer_id = '{}'".format(customer_id)
    cursor.execute(query)
    customer_address_list = cursor.fetchall()
    customer_user.commit()
    cursor.close

    ## make string address list
    string_address_list = []
    for i in customer_address_list:
        string_address_list.append(i[4])

    if (not len(string_address_list) == 0):
        ## choose address menu
        address_line = StringVar()

        seller_id_menu = OptionMenu(add_to_cart, address_line, *string_address_list)
        seller_id_menu.grid(row = 0, column = 1)

        ## insert into orders
        cursor1 = customer_user.cursor()
        query = "INSERT INTO orders (orders_id, place_status, delivery_status, return_status, orders_quantity, payment_method, final_cost, orders_date, phone, city, country, addressline,          state, pin_code, customer_id, agent_id, seller_id, product_id, delivery_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,)"                                     
        ##                              0             1              2                3             4                5             6            7         8     9     10          11                  12      13          14         15         16         17          18                 0    1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17
        tuple = (                      None,      "false",        "false",          None,         quantity1,      method1,        cost1,      None,     None,  None , None,   address_line.get(),    None,   None,    customer_id,   None,   seller_id,  product_id,  None                                                                                         )
        cursor1.execute(query, tuple)
        customer_user.commit()
        cursor1.close()





def display_sellers_of_product(page, customer_user, customer_id, product_id, product_name):
    page.destroy()
    product_sellers = Tk()
    product_sellers.title("seller options")
    product_sellers.geometry("800x600")

    ## fetch all the listings corresponding to product_id
    cursor = customer_user.cursor()
    query = "SELECT * FROM view_listings WHERE product_id = '{}'".format(product_id)
    cursor.execute(query)
    listings = cursor.fetchall()
    customer_user.commit()
    cursor.close()

    ## create lisings list
    listings_displayed = 0
    for i in listings:
        lisitng_label = Label(product_sellers, text = "seller_id: " + str(i[0]) + "\navg rating: " + str(i[1]) + "\nselling cost: " + str(i[2]) + "\nselling quantity: " + str(i[3]) + "\ndiscount: " + str(i[4]) + "\nproduct name: " + i[6] + "\navailability: " + i[7], font = ("bold", 10), bd = 1, relief = "sunken")
        lisitng_label.grid(row = listings_displayed, column = 0)
        listings_displayed += 1

    ## create seller_id string list
    seller_id_listings = []
    for i in listings:
        seller_id_listings.append(i[0])

    ## choose seller from drop down menu
    seller_listing_id = StringVar()
    seller_listing_id.set(seller_id_listings[0])

    seller_id_menu = OptionMenu(product_sellers, seller_listing_id, *seller_id_listings)
    seller_id_menu.grid(row = 0, column = 1)



    ## display corresponding buttons
    buttons_displayed = 0
    for i in listings:
        add_product_button = Button(product_sellers, text = "add to cart", bg = "lime", command = lambda: add_listing_to_cart(product_sellers, customer_user, customer_id, product_id, seller_listing_id.get() )  ) 
        add_product_button.grid(row = buttons_displayed, column = 2)

        see_review_button = Button(product_sellers, text = "view reviews", bg = "cyan", command = lambda: see_reviews(product_sellers, customer_user, customer_id, product_id, seller_listing_id.get() ) )
        see_review_button.grid(row = buttons_displayed, column = 3 )
        buttons_displayed += 1


    product_sellers.mainloop()

        










def display_products(page, customer_user, customer_id, sub_category_selected):
    page.destroy()
    show_products = Tk()
    show_products.title("search by category Page")
    show_products.geometry("800x600")

    ## fetch products of the subcategory
    cursor = customer_user.cursor()
    query = "SELECT product_name, product_id, curr_status FROM products_Of_subCategory WHERE sub_category = '{}'".format(sub_category_selected)
    ##                   0            1           2 
    cursor.execute(query)
    products_of_subcategory = cursor.fetchall()
    customer_user.commit()
    cursor.close()

    ##make string list of products
    string_list_products = []
    for i in products_of_subcategory:
        string_list_products.append(i[0])

    ## make menu of products
    product_name_selected = StringVar()
    product_name_selected.set(string_list_products[0])

    product_menu = OptionMenu(show_products, product_name_selected, *string_list_products)
    product_menu.grid(row = 0, column = 0)

    ## make dictionary for getting productid of productname
    product_name_id_dict = {}
    for i in products_of_subcategory:
        product_name_id_dict[i[0]] = i[1]

    ## button for choosing seller
    choose_seller_button = Button(show_products, text = "Choose\nBuying Option", bg = "lime", command = lambda: display_sellers_of_product(show_products, customer_user, customer_id, product_name_id_dict[product_name_selected.get()], product_name_selected.get())  ) 
    choose_seller_button.grid(row = 0, column = 1)

    show_products.mainloop()






def show_sub_categories(page, customer_user, customer_id, product_category):
    page.destroy()
    show_sub_categories_page = Tk()
    show_sub_categories_page.title("search by category Page")
    show_sub_categories_page.geometry("800x600")

    ## fetch sub categories
    cursor = customer_user.cursor()
    query = "SELECT sub_category FROM subCategory WHERE product_category = '{}'".format(product_category)
    cursor.execute(query)
    sub_categories_list = cursor.fetchall()
    customer_user.commit()
    cursor.close()

    ## make list of subcategory strings
    subcategory_string_list = []
    for i in sub_categories_list:
        subcategory_string_list.append(i[0])


    ## make menu for selecting subcategory
    sub_category_selected = StringVar()
    sub_category_selected.set(subcategory_string_list[0])

    sub_category_menu = OptionMenu(show_sub_categories_page, sub_category_selected, *subcategory_string_list)
    sub_category_menu.place(x = 50, y = 20)

    ## search product button
    search_product_button = Button(show_sub_categories_page, text = "search products", bg = "lime", command = lambda: display_products(show_sub_categories_page, customer_user, customer_id, sub_category_selected.get() ) ) 
    search_product_button.place(x = 200, y = 50)
    
    show_sub_categories_page.mainloop()






    

    show_sub_categories_page.mainloop()
        





def search_products_by_category(customer_homepage, customer_user, customer_id):
    customer_homepage.destroy()
    search_by_category_page = Tk()
    search_by_category_page.title("search by category Page")
    search_by_category_page.geometry("800x600")

    ## fetch list of categories
    cursor = customer_user.cursor()
    query = "SELECT product_category FROM productCategory"
    cursor.execute(query)
    categories = cursor.fetchall()
    customer_user.commit()
    cursor.close()
    ## make list of categories
    category_string_list = []
    for i in categories:
        category_string_list.append(i[0])



    ## dropdown menu for categories
    category_selected = StringVar()
    category_selected.set(category_string_list[0])

    category_menu = OptionMenu(search_by_category_page, category_selected, *category_string_list)
    category_menu.place(x = 50, y = 20)


    ## button for searching subcategories categoires
    category_button = Button(search_by_category_page, text = "search subcategories", bg = "lime", command = lambda: show_sub_categories(search_by_category_page, customer_user, customer_id, category_selected.get() )  ) 
    category_button.place(x = 200, y = 50)
    
    search_by_category_page.mainloop()
    


    

def display_searched_products(page, customer_user, customer_id, product_name):
    cursor = customer_user.cursor()
    query = "SELECT * FROM product WHERE product_name LIKE '{}'".format("%" + product_name + "%")
    cursor.execute(query)
    names_fetched = cursor.fetchall()
    customer_user.commit()
    cursor.close()

    ## create string names list
    product_name_list = []
    for i in names_fetched:
        product_name_list.append(i[1])

    ## make dictionary from name to id
    dict_id_name = {}
    for i in names_fetched:
        dict_id_name[i[1]] = i[0]


    ## check if any results are there
    if (len(product_name_list) == 0):
        messageBox.showinfo("error", "no products found try again")
    else:
        ## create new page and display products
        page.destroy()
        search_products_page = Tk()
        search_products_page.title("search product by name")
        search_products_page.geometry("800x600")

        ## display product names in drop down menu
        product_name_chosen = StringVar()
        product_name_chosen.set(product_name_list[0])


        product_name_menu = OptionMenu(search_products_page, product_name_chosen, *product_name_list)
        product_name_menu.grid(row = 0, column = 0)

        ## button to choose seller
        choose_seller = Button(search_products_page, text = "choose seller", command = lambda: display_sellers_of_product(search_products_page, customer_user, customer_id, dict_id_name[product_name_chosen.get()], product_name_chosen.get()) ) 
        choose_seller.grid(row = 3, column = 1)


        search_products_page.mainloop()





    





def search_by_product_name(page, customer_user, customer_id):
    page.destroy()
    search_product_name_page = Tk()
    search_product_name_page.title("search product by name")
    search_product_name_page.geometry("800x600")

    ## label for enter product name
    enter_name = Label(search_product_name_page, text = "Enter product name:  ", font = ("bold", 10))
    enter_name.grid(row = 0, column = 0)

    ## text box for inputting product name
    product_name_textbox = Entry(search_product_name_page)
    product_name_textbox.grid(row = 0, column = 1)

    ## search button
    search_button = Button(search_product_name_page, text = "Search", command = lambda: display_searched_products(search_product_name_page, customer_user, customer_id, product_name_textbox.get()) ) 
    search_button.grid(row = 3, column = 1)



def display_customer_homepage(page, customer_user, customer_id ):
    page.destroy()
    ## create homepage
    customer_homepage = Tk()
    customer_homepage.title("Customer Home Page")
    customer_homepage.geometry("800x600")


    ## view orders ONGOING
    view_orders_button = Button(customer_homepage, text = "view orders", font = ("bold", 10), bg = "white", command = lambda: view_customer_orders(customer_homepage, customer_user, customer_id))
    view_orders_button.place(x = 200, y = 40)

    ## view cart
    view_cart_button = Button(customer_homepage, text = "view cart", font = ("bold", 10), bg = "white", command = lambda: view_customer_cart(customer_homepage, customer_user, customer_id) )
    view_cart_button.place(x = 200, y = 80)


    ## view profile
    view_profile_button = Button(customer_homepage, text = "view profile", font = ("bold", 10), bg = "white", command = lambda: view_customer_profile(customer_homepage, customer_user, customer_id) )
    view_profile_button.place(x = 200, y = 120)

    ## search by category
    searchby_category_button = Button(customer_homepage, text = "search by category", font = ("bold", 10), bg = "white", command = lambda: search_products_by_category(customer_homepage, customer_user, customer_id) )
    searchby_category_button.place(x = 200, y = 160)

    ## search by product
    searchby_product_butotn = Button(customer_homepage, text = "search product", font = ("bold", 10), bg = "white", command = lambda: search_by_product_name(customer_homepage, customer_user, customer_id) )
    searchby_product_butotn.place(x = 200, y = 200)

    customer_homepage.mainloop()








def main(dba, customer_login_page, customer_id):
    customer_user = mysql.connector.connect(host = "localhost", user = "customer", passwd = "Cus_pass1@", database = "ORS1")
    display_customer_homepage(customer_login_page, customer_user, customer_id)

