import Graph
import time

# graph = Graph.generate_graph('Test1.txt')
# graph.visualize_graph()
#
# print(Graph.find_shortest_cycle(graph,'1-2'))

start_time = time.time()

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

Graph.remove_negative_edges(graph, debug=False)

while True:
    cycles = Graph.get_all_shortest_cycles(graph, debug=False)
    if len(cycles) == 0:
        break
    # graph.visualize_graph()
    Graph.remove_best_edges(graph, cycles, debug=False)
    # graph.visualize_graph()

end_time = time.time()

elapsed_time = end_time - start_time

print("Elapsed time: ", elapsed_time, " seconds")

print(graph.score)
graph.visualize_graph()
