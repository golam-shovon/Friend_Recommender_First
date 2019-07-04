import csv
import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter
import community

with open('userlist_updated.csv', 'r') as nodecsv: # Open the file
    nodereader = csv.reader(nodecsv) # Read the csv
    # Retrieve the data (using Python list comprhension and list slicing to remove the header row, see footnote 3)
    nodes = [n for n in nodereader][1:]

node_id = [n[0] for n in nodes] # Get a list of only the node ids

with open('friendlist_updated.csv', 'r') as edgecsv: # Open the file
    edgereader = csv.reader(edgecsv) # Read the csv
    edges = [tuple(e) for e in edgereader][1:]



G2 = nx.Graph()
G2.add_nodes_from(node_id)
G2.add_edges_from(edges)

university_dict = {}
city_dict = {}
sex_dict = {}


for node in nodes: # Loop through the list of nodes, one row at a time
    university_dict[node[0]] = node[1] # Access the correct item, add it to the corresponding dictionary
    city_dict[node[0]] = node[2]
    sex_dict[node[0]] = node[3]


# Add each dictionary as a node attribute to the Graph object
nx.set_node_attributes(G2, university_dict, 'university')
nx.set_node_attributes(G2, city_dict, 'city')
nx.set_node_attributes(G2, sex_dict, 'sex')




nx.draw(G2, with_labels=True)
plt.draw()
plt.show
