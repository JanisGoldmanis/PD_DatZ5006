import GraphVisualization as GV

# Opening and parsing input file

f = open("prog_2022_sample_input_1.txt", "r")
lines = f.readlines()
numbers = []
for line in lines:
    numbers += line.split()
numbers = [int(x) for x in numbers]

# Generating meta data regarding graph

number_of_nodes = numbers[0]
number_of_edges = int((len(numbers) - 1) / 3)

vertice_set = set()
edge_set = set()
taken_edges = set()
edge_weight = {}
adjacent_vertices = {}

for index in range(number_of_edges):
    i = index * 3 + 1
    vertice_set.add(numbers[i])
    vertice_set.add(numbers[i + 1])
    edge_format = f'{min(numbers[i], numbers[i + 1])}-{max(numbers[i], numbers[i + 1])}'
    edge_set.add(edge_format)
    edge_weight[edge_format] = numbers[i+2]

print(f'Vertices: {vertice_set}')
print(f'Edges: {edge_set}')

for vertice in vertice_set:
    adjacent_vertices[vertice] = []

# print(f'Adjacent vertices: {adjacent_vertices}')

for edge in edge_set:
    vertices = edge.split('-')
    start = int(vertices[0])
    end = int(vertices[1])
    adjacent_vertices[start].append(end)
    adjacent_vertices[end].append(start)

for vertice in adjacent_vertices.keys():
    adjacent_vertices[vertice] = sorted(adjacent_vertices[vertice])

# for vertice in adjacent_vertices.keys():
#     print(f'Vertice {vertice:>3}: {adjacent_vertices[vertice]}')

score = 0
graph = (vertice_set, edge_set, edge_weight, adjacent_vertices)
solution = (graph, taken_edges, score)


def remove_edge(solution, edge):
    graph = solution[0]
    taken_edges = solution[1]
    vertice_set = graph[0]
    edge_set = graph[1]
    edge_weight = graph[2]
    adjacent_vertices = graph[3]
    vertices = edge.split('-')
    start = int(vertices[0])
    end = int(vertices[1])

    taken_edges.add(edge)
    edge_set.remove(edge)
    weight = edge_weight[edge]
    adjacent_vertices[start].remove(end)
    adjacent_vertices[end].remove(start)
    return weight


def print_graph(graph):
    print('Printing graph:')
    print(graph[0])
    print(graph[1])
    for vertice in graph[3].keys():
        print(f'Vertice {vertice:>3}: {adjacent_vertices[vertice]}')
    print()


print(score)
print(taken_edges)

print_graph(graph)

# Add all negative


for edge in edge_set.copy():
    if edge_weight[edge] < 0:
        score += remove_edge(solution, edge)

taken_edges = sorted(taken_edges)
print(score)
print(taken_edges)

print_graph(graph)

# Driver code
G = GV.GraphVisualization()
G.addEdge(0, 2)
G.addEdge(1, 2)
G.addEdge(1, 3)
G.addEdge(5, 3)
G.addEdge(3, 4)
G.addEdge(1, 0)
G.visualize()
