import networkx as nx

import matplotlib.pyplot as plt


vertices=["1", "2", "3", "4", "5", "6", "7", "8"]

aristas = [('1', '2'), ('1', '5'), ('2', '3'), ('2', '5'), ('2', '8',)  \

           , ('3', '4'), ('4', '5'), ('4', '6'), ('4', '7')\

           , ('7', '8')]

g = nx.Graph()


def crear_y_recorrer_grafo():
    g.add_nodes_from(vertices)
    g.add_edges_from(aristas)
    coloreo = nx.greedy_color(g)
    colores = ['gray' , 'red' , 'yellow' , 'lightblue' , 'green']
    node_colors = [colores[coloreo[node]] for node in g.nodes]
    nx.draw(g, with_labels=True, node_color=node_colors, edge_color='gray', arrows = True, arrowstyle = '->', arrowsize = 10)
    plt.show()
    return coloreo

def nodos_y_cantidad_pintados(coloreo):
    colores_por_numero = []
    colores_por_numero.extend(coloreo.values())
    aux = 0
    contador = []
    for i in range(0, len(colores_por_numero)):
        contador.append(0)
        if(colores_por_numero[i] == aux):
            contador[colores_por_numero[i]] += 1
        else:
            aux = colores_por_numero[i]
            contador[colores_por_numero[i]] += 1 
    for n in contador:
        contador.remove(0) 
    
    valor_max = max(contador)
    posicion_max = contador.index(valor_max)
    
    nodos_pintados = []     
    for c in coloreo:
        if(coloreo[c] == posicion_max):
            nodos_pintados.append(c)
    print(contador[posicion_max])
    print(nodos_pintados)
    
    
nodos_y_cantidad_pintados(crear_y_recorrer_grafo())
