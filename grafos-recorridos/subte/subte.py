import networkx as nx
import matplotlib.pyplot as plt

nodos = ['1','2','3','4','5','6','7','8','9','10','11','12'] 

aristas = [('1','2'),('2','5'),('5','6'),('6','8'),('8','9'),('9','10'), #subte 1
           ('4','1'),('1','3'),('3','6'),('6','10'), #subte 2
           ('4','7'),('7','10'),('10','11'),('11','12')] #subte 3

g = nx.Graph()

partida = nodos[3]
llegada = nodos[1]

g.add_edges_from(aristas)
g.add_nodes_from(nodos)
dfs_edges = nx.dfs_edges(g, source=partida)
pos = nx.spring_layout(g)
nx.draw_networkx(g, pos)
labels = nx.get_edge_attributes(g, 'weight')
nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)
plt.show()


dfs = []

for edge in dfs_edges:
    dfs.append(edge)
    if((edge[1] == llegada) or (edge[0] == llegada)):
     break
    
print(dfs)

trasbordos = 0
subtes_trasbordados = []

for arista in aristas:
    arista_reves = (arista[1] , arista[0])
    for d in dfs:
        estacion_actual = d[0]
        estacion_siguiente = arista[1]
        if(d == arista or d == arista_reves):
            trasbordos+=1
                
print(trasbordos)



    