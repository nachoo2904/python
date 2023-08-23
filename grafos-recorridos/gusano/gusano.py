import networkx as nx
import matplotlib.pyplot as plt

nodos = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17']

aristas = [('1','3',2),('1','2',3),('3','4',2),('2','5',4),('4','5',4),
    ('11','10',2),('12','10',3),('10','5',1),('5','6',2),('6','15',3),('6','8',3),
    ('5','8',1),('10','13',4),('8','7',1),('8','9',2),('8','14',1),('13','14',2)]

g = nx.Graph()
g.add_nodes_from(nodos)
g.add_weighted_edges_from(aristas)
pos = nx.circular_layout(g)
nx.draw_networkx(g, pos)
labels = nx.get_edge_attributes(g, 'weight')
nx.draw_networkx_edge_labels(g, pos, edge_labels=labels) 
plt.show()
