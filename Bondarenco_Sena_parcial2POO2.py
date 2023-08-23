import networkx as nx
import matplotlib.pyplot as plt

#conjunto de esquinas (nodos)
esquinas = ['1', '2', '3']
calles = [('1', '2', 4), ('2', '3', 5), ('3', '1', 2) ]

#creacion del grafo
g = nx.Graph()

#punto de inicio (nombre de esquina donde parte el colectivo)
colectivo = esquinas[0]
#punto de llegada (nombre donde se ubica la escuela)
colegio = esquinas[2]

#añadir nodos y aristas con peso del grafo 'g' creado
def crear_y_recorrer_grafo():
    g.add_nodes_from(esquinas)
    g.add_weighted_edges_from(calles)
    #recorrido minimo realizado teniendo en cuenta el punto de inicio y de llegada (recorrido de dijkstra)
    dijkstra = nx.dijkstra_path(g, colectivo, colegio)
    #dibujo y visualizacion del grafo
    pos = nx.spring_layout(g)
    nx.draw_networkx(g, pos)
    labels = nx.get_edge_attributes(g, 'weight')
    nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)
    plt.show()
    return dijkstra 

#logica para realizar el cambio de las manos de las calles
def cambiar_mano(camino):
    #crear variable de contador de calles
    contador_calle_num = 0
    #crear lista de calles a cambiar
    calles_a_cambiar = []
    #recorrer las calles (aristas)
    for calle in calles:
        #cambio de posicion de calle para luego ver si es necesario el cambio de mano o no
        calle_cambiada = [calle[1],calle[0], calle[2]]
        #recorrer el camino minimo
        for i in range(1, len(camino)):
            #comparar la posicion del camino con la calle cambiada, si es verdadero significa que la calle debe cambiar de mano
            if(camino[i-1] == calle_cambiada[0] and camino[i] == calle_cambiada[1]):
                #agregar la calle (arista con peso) a cambiar en la lista ya cambiada de sentido
                calles_a_cambiar.append(calle_cambiada)
        #aumento de contador de calle por iteracion para ir recorriendo cada una    
        contador_calle_num += 1
    return calles_a_cambiar       

#llamado a la funciones
camino = crear_y_recorrer_grafo()
#añadir a una variable la distancia recorrida por el minimo camino (peso minimo del grafo)
camino_distancia = nx.dijkstra_path_length(g, colectivo, colegio)
#añadir a una variable la mano ya cambiada
calles_a_cambiar = cambiar_mano(camino)

#mostrar por pantalla los resultados
print("El camino es:", camino)
print("La distancia es:", camino_distancia)
print("Las calles a cambiar son:", calles_a_cambiar)
