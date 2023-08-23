import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()

nodos = ['1','2','3','4','5','6','7','8','9']

g.add_nodes_from(nodos)

escenas_empalmadas = {
    '1' : ('1','20'),
    '2' : ('20','45'),
    '3' : ('20','30'),
    '4' : ('30','60'),
    '5' : ('40','80'),
    '6' : ('55','90'),
    '7' : ('80','100'),
    '8' : ('85','99'),
    '9' : ('90','100')
}

print(int (escenas_empalmadas.get( nodos[0])[1]) - int (escenas_empalmadas.get(nodos[1])[0]))

for i in range(len(nodos)):
    print()
    
print(g)