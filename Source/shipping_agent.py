import mysql.connector

############################### SHIPPING AGENT MAN ##################################

def view_agent(Agent,agent_id):
    cursor = Agent.cursor()
    cursor.execute("Select agent_id, agent_name, email, curr_status, phone from shippingagent where agent_id = " + str(agent_id))
    val = cursor.fetchall()
    rows = ["agent_id", "agent_name", "email", "curr_status", "phone"]
    data = {}
    for i in range(0,5):
        data[rows[i]] = val[0][i]

    return (data)

#def update_agent():


def delete_agent(Agent,agent_id):
    cursor = Agent.cursor()
    cursor.execute("UPDATE shippingagent SET curr_status = '{}' WHERE agent_id = '{}'".format("NOT_WORKING", agent_id))
    Agent.commit()


############################### ORDER AGENT MAN ##################################

def view_orders(Agent, agent_id):
    cursor = Agent.cursor()
    cursor.execute("Select * from orders_info_for_shippingagent where agent_id = " + str(agent_id))
    val = cursor.fetchall()
    return (val)



############################### MAIN ################################################
def main(agent_id):
    Agent = mysql.connector.connect(host="localhost", user="agent", passwd="Agent_pass1@", database="ORS1")
    print(view_agent(Agent,agent_id))
    delete_agent(Agent,agent_id)
    print(view_agent(Agent, agent_id))

if __name__ == "__main__":
    main(9)