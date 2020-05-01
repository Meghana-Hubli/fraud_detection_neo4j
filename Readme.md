Usage:

1. Install Neo4j Graph Database [https://neo4j.com/]

2. If Neo4j is running in the same machine as the python scripts, then no modifications are required. 

3. If the Database is runnning on a remote machine, then in the included code, please change the IP address from localhost (127.0.0.1) to the IP address of the remote machine. It should be in the same network, or routing would be required.

Versions:

Python 3.6 and Neo4j 4.0.3

Related datasets are stored in their respective directories.

For credit card fraud detection, all the input dataset queries and the fraud detection queries are stored in the "credit_card_fraud_detection_dataset"

The input queries are "customers.txt", "merchants.txt" and "transactions.txt". This will create all the relative Nodes and Relationships.

plot_cc_fraud.py - Python file for Creating Graph Database and running related queries for credit card fraud.

Query 1 - fraud_transactions.txt

Query 2 - point_of_origin.txt

Query 3 - culprit_query.txt

Each query will generate a related csv file with the stored output.


For Bank fraud detection, 

plot_bank_fraud.py - Python file for creating graph database and running related queries for bank fraud.

Query 1 - finding_fraud_rings.txt

Query 2 - finance_loss_by_fraud_rings.txt

Other related Queries include, mapping all the nodes, extracting the information, and looking for false positives which are part of the python code.
