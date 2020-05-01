
from py2neo import Graph, Node, Relationship
import re

### Add all the contrainsts

filenames = ['credit_card_fraud_detection_dataset/customers.txt','credit_card_fraud_detection_dataset/merchants.txt']
delete_previous_nodes = 1

# Connecting to the Neo4j Graph Database
graph = Graph("http://127.0.0.1:7474", user='neo4j', password='password')
if delete_previous_nodes == 1:
    graph.delete_all()

for file in filenames:
    with open(file) as file_content:
        for query in file_content:
            node = graph.run(query).data()
            #print(node)

person_names_list = graph.run("MATCH (a:Person) RETURN a.name LIMIT 20").data()

person_names = []
for name in person_names_list:
    person_names.append(name['a.name'])
#print(person_names)

merchant_names_list = graph.run("MATCH (a:Merchant) RETURN a.name LIMIT 20").data()

merchant_names = []
for name in merchant_names_list:
    merchant_names.append(name['a.name'])

#print(merchant_names)

transaction_file = 'credit_card_fraud_detection_dataset/transactions.txt'
with open(transaction_file) as tran_file:
    for transaction in tran_file:
        connecting_nodes = re.findall('\(([^)]+)', transaction)
        tran_str = 'MERGE ('+  connecting_nodes[0] +':Person {name:"'+ connecting_nodes[0] + '"}) MERGE (' + connecting_nodes[1] +':Merchant {name:"' + connecting_nodes[1]+ '"})' + transaction
        graph.run(tran_str)


# Narrow down all fraudulent transactions
with open('credit_card_fraud_detection_dataset/fraud_transactions.txt') as file:
    fraud_transactions = file.read()
    print(fraud_transactions)
    output = graph.run(fraud_transactions).data()

with open('credit_card_fraud_detection_dataset/fraud_transactions.csv','w') as file:
    file.write("Customer Name" + "," + "Store Name" + "," + "Amount" + "," + "Transaction Time"+"\n")
    for each_dict in output:
        file.write(each_dict["Customer Name"] + "," + each_dict["Store Name"] + "," + each_dict["Amount"] + ","  + each_dict["Transaction Time"] +"\n")

print("\n\n")
# Find the Undisputed transactions which happened right before the disputed transaction happened
with open('credit_card_fraud_detection_dataset/point_of_origin.txt') as file:
    point_of_origin = file.read()
    print(point_of_origin)
    output = graph.run(point_of_origin).data()

with open('credit_card_fraud_detection_dataset/point_of_origin.csv','w') as file:
    file.write("Customer Name" + "," + "Store Name" + "," + "Amount" + "," + "Transaction Time" +"\n")
    for each_dict in output:
        file.write(each_dict["Customer Name"] + "   " + each_dict["Store Name"] + "   " + each_dict["Amount"] + "   "  + each_dict["Transaction Time"] +"\n")

print("\n\n")
# Find the Origin of Culprit in the Disputed transactions above.
with open('credit_card_fraud_detection_dataset/culprit_query.txt') as file:
    culprit_query = file.read()
    print(culprit_query)
    output = graph.run(culprit_query).data()

with open('credit_card_fraud_detection_dataset/culprit_query.csv','w') as file:
    file.write("Suspicious Store" + "," + "Count" + "," + "Victims"+"\n")
    for each_dict in output:
        file.write(each_dict["Suspicious Store"] + "," + str(each_dict["Count"]) + "," + str(each_dict["Victims"]) + "\n")

print("\n\n")