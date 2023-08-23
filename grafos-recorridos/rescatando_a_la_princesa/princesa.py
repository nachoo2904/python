import networkx as nx
import matplotlib.pyplot as plt

nodos = ['1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']

aristas = [('1','2',3),('1','3',2),('2','3',4),('2','6',1),('3','8',1)
           ,('8','6',5),('4','5',2),('3','4',2),('3','6',2),('6','9',3)]


#creamos grafo
g = nx.Graph()
g.add_weighted_edges_from(aristas)
g.add_nodes_from(nodos)

#creamos digrafo
g2 = nx.DiGraph()
g2.add_nodes_from(nodos)
g2.add_weighted_edges_from(aristas)


#posicion donde se encuentra el principe, la princesa y los dragones
posicion_principe = nodos[0]
posicion_princesa = nodos[8]
dragones = [nodos[7], nodos[4]]

#preguntamos si hay camino entre principe y princesa
def hay_camino():
    if(nx.has_path(g2, posicion_principe, posicion_princesa) != True):
        return("NO HAY CAMINO")

#copiamos digrafo y le removemos los nodos con dragones para ver si igual hay camino hacia la princesa   
def recorrer_por_dijkstra():
    subdigraph = g2.copy()
    subdigraph.remove_nodes_from(dragones)
    if(nx.has_path(subdigraph, posicion_principe, posicion_princesa) != True):
        print("INTERCEPTADO")
    else:
        recorrido()


#dibujamos subgrafo y copiamos el grafo para crear un subgrafo que no tenga los nodos con dragones
def recorrido():
    sg = g.copy() 
    sg.remove_nodes_from(dragones)
    sub_dijkstra = nx.dijkstra_path(sg, posicion_principe , posicion_princesa)
    pos = nx.random_layout(sg)
    nx.draw_networkx(sg, pos)
    labels = nx.get_edge_attributes(sg, 'weight')
    nx.draw_networkx_edge_labels(sg, pos, edge_labels=labels) 
    plt.show()
    print(sub_dijkstra)
    
print(hay_camino())
recorrer_por_dijkstra()

 