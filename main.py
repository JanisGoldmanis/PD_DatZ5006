# import GraphVisualization as GV
# import Solution
import Graph

file = "prog_2022_sample_input_1.txt"

graph = Graph.generate_graph(file)

# solution = Solution.Solution()
# solution.graph = graph
# solution.taken_edges = graph.taken_edges
# solution.score = graph.score




# graph.print_graph()
#
# graph.visualize_graph()

# Add all negative

for edge in graph.edges.copy():
    if graph.edge_weight[edge] < 0:
        graph.score += Graph.remove_edge(graph, edge)



graph.taken_edges = sorted(graph.taken_edges)
print(graph.score)
print(graph.taken_edges)

# graph.print_graph()
# graph.visualize_graph()

path_list = []


# print(f'Edges: {len(graph.edges)}')
# print(graph.edges)

cycle = True

while cycle:
    min_path = len(graph.vertices)
    print(f'Starting min path: {min_path}')


    for edge in graph.edges:
        # print('Searching',edge)
        path = Graph.find_shortest_cycle(graph, edge)
        path_list.append(path)
        print(path)



    for path in path_list:
        # print(path)
        if len(path) < min_path:
            min_path = len(path)
    print(f'Actual min path: {min_path}')

    check_paths = []

    for path in path_list:
        if len(path) == min_path:
            check_paths.append(path)

    # for path in check_paths:
    #     print(path)

    min_edge = 200
    print(f'Finding min edge')
    for path in check_paths:
        path.append(path[0])
        print(path)
        # print(path)
        for index in range(len(path) - 1):
            min_vertice = min(path[index], path[index + 1])
            max_vertice = max(path[index], path[index + 1])
            edge = str(min_vertice) + '-' + str(max_vertice)
            try:
                print(f'Weight: {graph.edge_weight[edge]}')
            except:
                testedge = (f'{path[0]}-{path[1]}')
                path = Graph.find_shortest_cycle(graph, testedge,True)

            if graph.edge_weight[edge] < min_edge:
                min_edge = graph.edge_weight[edge]
    print(f'Min edge: {min_edge}')


    flag = False
    for path in check_paths:
        for index in range(len(path) - 1):
            min_vertice = min(path[index], path[index + 1])
            max_vertice = max(path[index], path[index + 1])
            edge = str(min_vertice) + '-' + str(max_vertice)
            # print(f'Path: {path}')
            if graph.edge_weight[edge] == min_edge:
                print(f'Removing {edge}')
                solution.score += remove_edge(solution, edge)
                flag = True
                break
        if flag:
            break
    graph.visualize_graph()

print(solution.score)

# print(Graph.find_shortest_cycle(graph,'1-4',True))
