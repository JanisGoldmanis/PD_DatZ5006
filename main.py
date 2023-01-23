import time
import Graph


def analyze_graph(file_name, visualize, print_edges):
    start_time = time.time()
    graph = Graph.generate_graph(file_name)
    if visualize:
        graph.visualize_graph()
    Graph.remove_negative_edges(graph, debug=False)
    while True:
        cycles = Graph.get_all_shortest_cycles(graph, debug=False)
        if len(cycles) == 0:
            break
        Graph.remove_best_edges(graph, cycles, debug=False)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Elapsed time: ", round(elapsed_time, 4), " seconds")
    print(f'Graph score: {graph.score}')
    if print_edges:
        print('Removed edges:')
        for edge in graph.taken_edges:
            print(f'Edge: {edge}, Weight: {graph.edge_weight[edge]}')
    if visualize:
        graph.visualize_graph()


visualize = False
print_edges = False

while True:
    print()
    print('Menu:')
    print('1 - Load and analyze graph')
    print('2 - Settings')
    print('3 - exit')
    case = input('Input:')
    if case == '1':
        print('Graph input file name (e.g. prog_2022_sample_input_1.txt)')
        filename = input('File name:')
        analyze_graph(filename, visualize, print_edges)
    elif case == '2':
        print()
        print('Settings:')
        print('1: Turn on visualization')
        print('2: Turn on edge printout')
        print('3: Turn on visualization and edge printout')
        print('4: Turn off visualization and edge printout')
        print('Turning on these settings advised only for small graphs!')
        settings = input('Chosen option:')
        if settings == '1':
            print('Turning on visualization of graph')
            visualize = True
        elif settings == '2':
            print('Turning on edge printout')
            print_edges = True
        elif settings == '3':
            print('Turning on visualization and edge printout')
            visualize = True
            print_edges = True
        elif settings == '4':
            print('Turning off visualization and edge printout')
            visualize = False
            print_edges = False
    elif case == '3':
        print('Exit')
        break
    else:
        print('Invalid input')
