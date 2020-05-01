
from py2neo import Graph


### Add all the contrainsts

filenames = ['bank_fraud_detection/bank_fraud_data.txt']
delete_previous_nodes = 1

# Connecting to the Neo4j Graph Database
graph = Graph("http://127.0.0.1:7474", user='neo4j', password='password')
if delete_previous_nodes == 1:
    graph.delete_all()


# open the file with all the related queries and run them in the graph database
for file in filenames:
    with open(file) as file_content:
        for query in file_content:
            node = graph.run(query).data()

# for first query, find all the accoutn holders and see if there is any existing ring in the connections
with open('bank_fraud_detection/finding_fraud_rings.txt') as file:
    fraud_rings = file.read()
    print(fraud_rings)
    output = graph.run(fraud_rings).data()

# storing the results in a csv file
with open('bank_fraud_detection/finding_fraud_rings.csv','w') as file:
    file.write("FraudRing" + "," + "ContactType" + "," + "RingSize"+"\n")
    for each_dict in output:
        file.write(str(each_dict["FraudRing"]) + "," + str(each_dict["ContactType"]) + "," + str(each_dict["RingSize"]) + "\n")

print("\n\n")
with open('bank_fraud_detection/finance_loss_by_fraud_rings.txt') as file:
    finance_loss = file.read()
    print(finance_loss)
    output = graph.run(finance_loss).data()
# storing the results in a csv file
with open('bank_fraud_detection/finance_loss_by_fraud_rings.csv','w') as file:
    file.write("FraudRing" + "," + "ContactType" + "," + "RingSize" + "," + "FinancialRisk" + "\n")
    for each_dict in output:
        file.write(str(each_dict["FraudRing"]) + "," + str(each_dict["ContactType"]) + "," + str(each_dict["RingSize"]) + "," + str(each_dict["FinancialRisk"]) + "\n")
print("\n\n")


