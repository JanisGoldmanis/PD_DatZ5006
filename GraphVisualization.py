# First networkx library is imported
# along with matplotlib
import networkx as nx
import matplotlib.pyplot as plt


# Defining a Class
class GraphVisualization:
    def __init__(self):
        self.visual = []

    def addEdge(self, a, b, weight):
        self.visual.append((a, b, weight))

    def visualize(self):
        G = nx.Graph()
        G.add_weighted_edges_from(self.visual)
        pos = nx.spring_layout(G, weight=None, k=0.5, iterations=100, scale=2, center=(0,0))
        nx.draw_networkx(G, pos)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=labels, label_pos=0.5)
        plt.show()


