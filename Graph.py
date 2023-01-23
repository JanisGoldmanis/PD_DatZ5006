import GraphVisualization as GV


def get_end_points(edge):
    vertices = edge.split('-')
    return int(vertices[0]), int(vertices[1])


def find_shortest_cycle(graph, edge, debug=False):
    if debug:
        print('Starting search of BFS shortest cycle')
    start, end = get_end_points(edge)
    first_neighborhood = graph.neighbors[start][:]
    first_neighborhood.remove(end)

    visited = set()
    next_cycle = set()
    current_cycle = set()
    parent = {}
    visited.add(start)

    for node in first_neighborhood:
        current_cycle.add(node)
        visited.add(node)
        parent[node] = start

    if debug:
        print(f'Start: {start}, End: {end}')
        print(f'First adjacent: {first_neighborhood}')
        print(f'Visited: {visited}')
        print(f'Current cycle: {current_cycle}')
        print(f'Parrent: {parent}')

    if len(current_cycle) == 0:
        return None

    flag = False
    cycle = True

    while len(current_cycle) > 0:
        for node in current_cycle:
            adjacent = graph.neighbors[node]
            adjacent = [x for x in adjacent if x not in visited]
            for destination in adjacent:
                if destination == end:
                    parent[end] = node
                    flag = True
                    break
                else:
                    parent[destination] = node
                    next_cycle.add(destination)
                    visited.add(destination)
            if flag:
                break
        if flag:
            break

        if debug:
            print(f'Next cycle: {next_cycle}')

        current_cycle.clear()
        for vertice in next_cycle:
            current_cycle.add(vertice)
        if len(next_cycle) == 0:
            cycle = False
            break
        next_cycle.clear()

    if not cycle:
        return None

    if debug:
        print(f'Parents: {parent}')

    path = []
    father = end
    child = parent[end]
    path.append(start)
    path.append(father)

    while True:
        path.append(child)
        father = child
        child = parent[father]
        if child == start:
            break

    return path


def get_all_shortest_cycles(graph, debug=False):
    if debug:
        print('Starting method of getting all shortest cycles')
    paths = []
    for edge in graph.edges:
        path = find_shortest_cycle(graph, edge, debug)
        if path is not None:
            paths.append(path)

    min_len = len(graph.vertices)
    for path in paths:
        if len(path) < min_len:
            min_len = len(path)

    paths_to_check = []
    for path in paths:
        if len(path) == min_len:
            paths_to_check.append(path)
    return paths_to_check


def remove_edge(graph, edge):
    taken_edges = graph.taken_edges
    edge_set = graph.edges
    edge_weight = graph.edge_weight
    adjacent_vertices = graph.neighbors
    vertices = edge.split('-')
    start = int(vertices[0])
    end = int(vertices[1])
    taken_edges.add(edge)
    edge_set.remove(edge)
    weight = edge_weight[edge]
    adjacent_vertices[start].remove(end)
    adjacent_vertices[end].remove(start)
    return weight


def remove_best_edge(graph, cycles, debug=False):
    if debug:
        print('Starting method of removing best edge')
    min_edge_weight = 200
    min_edge = ''
    for cycle in cycles:

        for index in range(len(cycle) - 1):
            if index == 0:
                start = min(cycle[0], cycle[-1])
                end = max(cycle[0], cycle[-1])
            else:
                start = min(cycle[index], cycle[index + 1])
                end = max(cycle[index], cycle[index + 1])
            edge = f'{start}-{end}'
            weight = graph.edge_weight[edge]
            if weight < min_edge_weight:
                min_edge_weight = weight
                min_edge = edge
    if debug:
        print(f'Removing edge: {min_edge} with weight: {graph.edge_weight[min_edge]}')
    graph.score += remove_edge(graph, min_edge)


def remove_best_edges(graph, cycles, debug=False):
    if debug:
        print('Starting method of removing multiple best edges')
        print(f'Length of cycles = {len(cycles[0])}')

    # Generating list of cycles sorted by lightest edge in cycle
    sorted_list_of_cycles = []

    # Each list entry is tuple ( "cycle", "list of edges", "min weight", "edge with min weight".

    for cycle in cycles:
        if debug:
            print(f'Evaluating cycle {cycle}')
        edge_list = []
        min_edge_weight = 200
        min_edge = ''

        for index in range(len(cycle)):
            start = min(cycle[index - 1], cycle[index])
            end = max(cycle[index - 1], cycle[index])
            edge = f'{start}-{end}'
            edge_list.append(edge)
            weight = graph.edge_weight[edge]
            if debug:
                print(f'    Edge {edge}, Weight: {weight}, Min edge weight: {min_edge_weight}')
            if weight < min_edge_weight:
                min_edge_weight = weight
                min_edge = edge
        cycle_compilation = (cycle, edge_list, min_edge_weight, min_edge)
        if debug:
            print(f'    Sorting {cycle_compilation}, stack size {len(sorted_list_of_cycles)}')
        if len(sorted_list_of_cycles) == 0:
            sorted_list_of_cycles.append(cycle_compilation)
        elif cycle_compilation[2] >= sorted_list_of_cycles[-1][2]:
            sorted_list_of_cycles.append(cycle_compilation)
        else:
            for i in range(len(sorted_list_of_cycles)):
                if cycle_compilation[2] < sorted_list_of_cycles[i][2]:
                    sorted_list_of_cycles.insert(i, cycle_compilation)
                    break
    if debug:
        print(f'Starting cycle iteration')
    for cycle in sorted_list_of_cycles:
        if debug:
            print(f'    Evaluating {cycle}')
        flag = False
        for edge in cycle[1]:
            if edge in graph.taken_edges:
                if debug:
                    print(f'        {edge} in taken edges')
                flag = True
                break
        if not flag:
            if debug:
                print(f'Removing edge: {cycle[3]} with weight: {graph.edge_weight[cycle[3]]}')
            graph.score += remove_edge(graph, cycle[3])


def remove_negative_edges(graph, debug=False):
    count_before = len(graph.edges)
    if debug:
        print(f'Removing negative edges. Total edges: {count_before}')
    for edge in graph.edges.copy():
        if graph.edge_weight[edge] <= 0:
            graph.score += remove_edge(graph, edge)
    if debug:
        print(f'Removed {count_before - len(graph.edges)} edges')


class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = set()
        self.edge_weight = {}
        self.neighbors = {}
        self.taken_edges = set()
        self.score = 0

    def print_graph(self):
        print('Printing graph:')
        print(self.vertices)
        print(self.edges)
        for vertice in self.neighbors.keys():
            print(f'Vertice {vertice:>3}: {self.neighbors[vertice]}')
        print()

    def visualize_graph(self):
        # Driver code
        G = GV.GraphVisualization()
        for edge in self.edges:
            vertices = edge.split('-')
            G.addEdge(vertices[0], vertices[1], self.edge_weight[edge])
        G.visualize()


def generate_graph(path):
    f = open(path, "r")
    lines = f.readlines()
    numbers = []
    for line in lines:
        numbers += line.split()
    numbers = [int(x) for x in numbers]

    number_of_nodes = numbers[0]
    number_of_edges = int((len(numbers) - 1) / 3)

    vertices_set = set()
    edge_set = set()
    taken_edges = set()
    edge_weight = {}
    adjacent_vertices = {}

    for index in range(number_of_edges):
        i = index * 3 + 1
        vertices_set.add(numbers[i])
        vertices_set.add(numbers[i + 1])
        edge_format = f'{min(numbers[i], numbers[i + 1])}-{max(numbers[i], numbers[i + 1])}'
        edge_set.add(edge_format)
        edge_weight[edge_format] = numbers[i + 2]

    # print(f'Vertices: {vertices_set}')
    # print(f'Edges: {edge_set}')

    for vertice in vertices_set:
        adjacent_vertices[vertice] = []

    for edge in edge_set:
        vertices = edge.split('-')
        start = int(vertices[0])
        end = int(vertices[1])
        adjacent_vertices[start].append(end)
        adjacent_vertices[end].append(start)

    for vertice in adjacent_vertices.keys():
        adjacent_vertices[vertice] = sorted(adjacent_vertices[vertice])

    graph = Graph()
    graph.edges = edge_set
    graph.vertices = vertices_set
    graph.edge_weight = edge_weight
    graph.neighbors = adjacent_vertices
    graph.taken_edges = taken_edges
    graph.score = 0
    return graph
