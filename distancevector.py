##implementation of the distance vector algorithm 

import networkx as nx

#construct a graph
#the graph here is refered from readme
G=nx.Graph()
G.add_nodes_from([0,1,2,3,4,5,6,7,8])
G.add_weighted_edges_from([(0,1,4),(0,7,8),(1,2,8),(1,7,11),(2,3,7),(2,5,4),(2,8,2),(3,4,9),(3,5,14),(4,5,10),(5,6,2),(6,7,1),(6,8,6),(7,8,7)])

#convert to distance vector matrix
matrix=[]
for a in range(G.number_of_nodes()):
	matrix.append([])
	for b in range(G.number_of_nodes()):
		matrix[a].append(0)
store=G.edges()
for i in range(G.number_of_edges()):
    matrix[(store[i][0])][(store[i][1])]=G[(store[i][0])][(store[i][1])]['weight']
    matrix[(store[i][1])][(store[i][0])]=G[(store[i][0])][(store[i][1])]['weight']

for a in range(G.number_of_nodes()):
    for b in range(G.number_of_nodes()):
        if matrix[a][b]==0:
            matrix[a][b]=1000
            
for i in range(G.number_of_nodes()):
    matrix[i][i]=0

#
count = 1;
while(count != 0):
    count = 0
    for i in range(G.number_of_nodes()):
        for j in range(i+1,G.number_of_nodes()):
            m = 1000
            n = 0
            for k in range(G.number_of_nodes()):
                n = matrix[i][k] + matrix[k][j]
                if n<m:
                    m = n
            if matrix[i][j] != m:
                matrix[i][j] = m
                count = count + 1

#complete the other half side
for i in range(G.number_of_nodes()):
    for j in range(G.number_of_nodes()):
        matrix[j][i] = matrix[i][j]

