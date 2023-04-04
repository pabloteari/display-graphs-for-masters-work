import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import scipy


class Graphs:
    def __init__(self, vertex):
        self.graph = nx.DiGraph()
        self.vertex = vertex


    def generate_graph(self):

        # Add nodes / vertex
        self.graph \
            .add_nodes_from(
                [1, self.vertex]
            )