'''from py2neo import Graph, Node, Relationship

graph = Graph("bolt://localhost:7687",user='neo5j', password='neo5j')
product = Node("item", name="Soap")
graph.create(product)'''

from py2neo import Graph, Node, Relationship
import csv
graph = Graph("bolt://localhost:7687", user='neo5j', password='neo5j')
graph.delete_all()
product_1 = []
product_2 = []
relation = [1000]
with open('card_1.csv') as card_csv, open('loan_1.csv') as loan_csv:
    card_csv_reader = csv.reader(card_csv, delimiter=',')
    loan_csv_reader = csv.reader(loan_csv, delimiter=',')
    line_count = 0
    i = 0

    for row in card_csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1

        else:
            line_count += 1
            current_node = Node("Card", card_id=row[0], disp_id=row[1], type=row[2], issued=row[3])
            print(current_node)
            graph.create(current_node)
            product_1.append(current_node)

    for row in loan_csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1

        else:
            line_count += 1
            current_node = Node("Loan", loan_id=row[0], account_id=row[1], date=row[2], amount=row[3],duration=row[4], payment= row[5], status=row[6])
            print(current_node)
            graph.create(current_node)
            product_2.append(current_node)

for i in range(0,len(product_1)):
    graph.create(Relationship(product_1[i], "Card on file for Loan", product_2[i+1]))


