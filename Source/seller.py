import mysql.connector

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

def update_seller(Seller,seller_id,parameter,value):
    cursor = Seller.cursor()
    cursor.execute("update seller set " + str(parameter) + " = '" + str(value) + "' where seller_id = " + str(seller_id) + ";")
    Seller.commit()

def delete_seller(Seller,seller_id):
    cursor = Seller.cursor()
    cursor.execute("delete from seller where seller_id = " + str(seller_id))
    Seller.commit()


#################### LISTING TABLE MAN. ##############################################

def view_list(Seller, seller_id):
    cursor = Seller.cursor()
    cursor.execute("Select * from view_listings where seller_id = " + str(seller_id))
    val = cursor.fetchall()
    rows = ["seller_seller_id","avg_rating","selling_cost","selling_quantity","discount","product_id","product_name","curr_status"]
    data = {}

    for i in range(0,8):
        ar = []
        for j in range (0, len(val)):
            ar.append(str(val[j][i]))
        data[rows[i]] = ar
    return (data)

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
    rows = ["first_name", "last_name", "rating", "review_comment", "review_date"]
    data = {}

    for i in range (0,5):
        ar = []
        for j in range (0,len(val)):
            ar.append(str(val[j][i]))

        data[rows[i]] = ar
    return (data)

################################# MAIN ##############################################

def main(seller_id):
    Seller = mysql.connector.connect(host="localhost", user="seller", passwd="Seller_pass1@", database="ORS1")
    edit_list(Seller,seller_id, 16, "avg_rating", "3.0")

# if __name__ == "__main__":
#     main(16)