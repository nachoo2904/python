import networkx as nx
import matplotlib.pyplot as plt



nodos = ['1', '2' , '3' , '4' , '5' , '6' , '7' , '8']
    
aristas = [('2', '4', 4) , ('2', '1', 5) , ('2', '3', 2) , ('3', '1', 3) , ('4', '1', 4) ,
            ('7', '5', 3) , ('1' , '5' , 3) , ('1' , '6' , 7) , ('8' , '4' , 2) ,
            ('6', '8', 1) , ('8', '7', 6), ('6', '7' , 8), ('5', '3', 2)]

g = nx.Graph()
dijkstra = []
dijkstra_distancia = 0


def armar_y_recorrer_grafo():
        g.add_nodes_from(nodos)
        g.add_weighted_edges_from(aristas)
        dijkstra.extend(nx.dijkstra_path(g, nodos[1] , nodos[6])) 
        dijkstra_distancia = nx.dijkstra_path_length(g, nodos[1] , nodos[6])
        pos = nx.spring_layout(g)
        nx.draw_networkx(g, pos)
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels) 
        print(dijkstra)
        #plt.show()     

        print(dijkstra_distancia)
        calles_cambiables = []
        numero_calle = 1
        for arista in aristas:
            calle_cambiada = [arista[1], arista[0]]
            for i in range(1, len(dijkstra)):
                if(dijkstra[i-1] == calle_cambiada[0] and dijkstra[i] == calle_cambiada[1]):
                    calles_cambiables.append(numero_calle)
            numero_calle += 1
            
        print(calles_cambiables)
        
              
armar_y_recorrer_grafo()