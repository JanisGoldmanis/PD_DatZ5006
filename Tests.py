import Graph

# graph = Graph.generate_graph('Test1.txt')
# graph.visualize_graph()
#
# print(Graph.find_shortest_cycle(graph,'1-2'))

graph = Graph.generate_graph('prog_2022_sample_input_3.txt')
# paths = Graph.get_all_shortest_cycles(graph)
# for path in paths:
#     print(path)
# graph.visualize_graph()
# print(Graph.find_shortest_cycle(graph, '1-2'))
#
# Graph.remove_edge(graph, '4-5')
#
# print(Graph.find_shortest_cycle(graph, '2-3'))
# print(Graph.find_shortest_cycle(graph, '2-5'))
# graph.visualize_graph()

# print()
# graph.visualize_graph()

while True:
    cycles = Graph.get_all_shortest_cycles(graph, debug=False)
    if len(cycles) == 0:
        break
    # graph.visualize_graph()
    Graph.remove_best_edge(graph, cycles, debug=False)
    # graph.visualize_graph()
    if len(graph.edges) % 100 == 0:
        print(len(graph.edges))

print(graph.score)
graph.visualize_graph()
