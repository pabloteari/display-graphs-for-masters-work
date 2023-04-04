import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import scipy

def main():
    #Create
    G = nx.DiGraph()
    #Cria 100 Vertices
    G.add_nodes_from([1,100])

    #Cria as arestas
    G.add_edges_from([(1,15)])
    G.add_edges_from([(2,3),(2,4)])
    G.add_edges_from([(3,4),(3,7)])
    G.add_edges_from([(4,7),(4,6)])
    G.add_edges_from([(5,6),(5,7)])
    G.add_edges_from([(6,7),(6,8)])
    G.add_edges_from([(7,8),(7,27)])
    G.add_edges_from([(8,27),(8,10)])
    G.add_edges_from([(9,10),(9,11)])
    G.add_edges_from([(11,11),(11,12)])
    G.add_edges_from([(12,11),(12,12)])
    G.add_edges_from([(13,11),(13,12)])
    G.add_edges_from([(14,11),(14,12)])
    G.add_edges_from([(15,11),(15,12)])
    G.add_edges_from([(16,11),(16,12)])
    G.add_edges_from([(17,11),(17,12)])
    G.add_edges_from([(18,11),(18,12)])
    G.add_edges_from([(19,11),(19,12)])
    G.add_edges_from([(20,11),(20,12)])
    G.add_edges_from([(11,11),(11,12)])
    G.add_edges_from([(12,11),(12,12)])
    G.add_edges_from([(13,11),(13,12)])
    G.add_edges_from([(14,11),(14,12)])
    G.add_edges_from([(15,11),(15,12)])
    G.add_edges_from([(16,11),(16,12)])
    G.add_edges_from([(17,11),(17,12)])
    G.add_edges_from([(18,11),(18,12)])
    G.add_edges_from([(19,11),(19,12)])
    G.add_edges_from([(20,11),(20,12)])
    G.add_edges_from([(21,11),(21,12)])
    G.add_edges_from([(22,11),(22,12)])
    G.add_edges_from([(23,11),(23,12)])
    G.add_edges_from([(24,11),(24,12)])
    G.add_edges_from([(25,11),(25,12)])
    G.add_edges_from([(27,12),(27,12)])
    G.add_edges_from([(28,13),(28,12)])
    G.add_edges_from([(29,14),(29,12)])
    G.add_edges_from([(30,15),(30,12)])
    G.add_edges_from([(31,16),(31,12)])
    G.add_edges_from([(32,17),(32,12)])
    G.add_edges_from([(33,18),(33,12)])
    G.add_edges_from([(34,19),(34,12)])
    G.add_edges_from([(35,20),(35,12)])
    G.add_edges_from([(36,11),(36,12)])
    G.add_edges_from([(37,12),(37,12)])
    G.add_edges_from([(38,13),(38,12)])
    G.add_edges_from([(39,14),(39,12)])
    G.add_edges_from([(40,15),(40,12)])
    G.add_edges_from([(41,16),(41,12)])
    G.add_edges_from([(42,17),(42,12)])
    G.add_edges_from([(43,18),(43,12)])
    G.add_edges_from([(44,19),(44,12)])
    G.add_edges_from([(45,20),(45,12)])
    G.add_edges_from([(46,21),(46,12)])
    G.add_edges_from([(47,22),(47,12)])
    G.add_edges_from([(48,23),(48,12)])
    G.add_edges_from([(49,24),(49,12)])
    G.add_edges_from([(50,25),(50,12)])


    pos = nx.shell_layout(G)
    i = 1
    uneven = True

    # Reposicionalo
    for y in range(1,7):
        for x in range(1,7):
            if uneven == True:
                pos[i] = ([(-1.0 + (3.0*(x-1))/10),(-1.0 + (3.0*(y-1))/10)])
                i=i+1
            else:
                pos[i] = ([(1.5 - (3.0*(x-1))/10),(-1.0 + (3.0*(y-1))/10)])
                i=i+1
        uneven = ~uneven

    nx.draw_networkx_nodes(G, pos)

    #Desenha as arestas
    nx.draw_networkx_edges(G, pos, arrows=True)

    #mostra e salva o desenho
    plt.savefig("Graph.png", format="PNG")
    plt.show()

if __name__ == "__main__":
    main()