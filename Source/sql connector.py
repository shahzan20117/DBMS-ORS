import mysql.connector


def cred_verify(id,pas,type,CUS):
    Idv = False
    Passv = False

    if type == "customer":
        CUS.execute("select customer_id from customer")
        data = CUS.fetchall()

    elif type == "seller":
        CUS.execute("select seller_id from seller")
        data = CUS.fetchall()

    elif type == "SA":
        CUS.execute("select agent_id from shippingagent")
        data = CUS.fetchall()


    for i in range(0,len(data)):
        if data[i][0] == id:
            Idv = True
            break
    if Idv == True:
        if type == "customer":
            CUS.execute("select customer_password from customer where customer_id = " + str(id))

        elif type == "seller":
            CUS.execute("select seller_password from seller where seller_id = " + str(id))

        elif type == "SA":
            CUS.execute("select agent_password from shippingagent where agent_id = " + str(id))

        data = CUS.fetchall()
        if data[0][0] == pas:
            print('ok')
            Passv = True


    if Idv == True and Passv == True:
        return True

    else:
        return False


def C_Connect(CUS):
    Cid = int(input("Customer id:"))
    Pass = input("password:")
    print("verifying...")

    if cred_verify(Cid,Pass,"customer",CUS) == True:
        print("login succesful")

    else:
        print("login failed")


def S_Connect(CUS):
    Cid = int(input("Seller id:"))
    Pass = input("password:")
    print("verifying...")

    if cred_verify(Cid,Pass,"seller",CUS) == True:
        print("login succesful")

    else:
        print("login failed")

def A_Connect(CUS):
    Cid = int(input("Agent id:"))
    Pass = input("password:")
    print("verifying...")

    if cred_verify(Cid,Pass,"SA",CUS) == True:
        print("login succesful")

    else:
        print("login failed")

def main():

    mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database = "ors1")
    if (mydb):
        print("connection successful")

        type = int(input("login as: 1. customer, 2. seller, 3. shipping agent"))
        cursor = mydb.cursor()

        if type ==1:
            C_Connect(cursor)

        elif type ==2:
            S_Connect(cursor)

        elif type ==3:
            A_Connect(cursor)


    else:
        print("connection unsuccessful")


if __name__ == "__main__":
    main()