f = open("prog_2022_sample_input_3.txt", "r")
values = [line.rstrip().replace(' ', '') for line in f]

numbers = []

for value in values:
    number = ''
    for index in range(len(value)):
        char = value[index]
        if char == '-' and len(number) == 0:
            number += char
        elif char.isnumeric():
            number += char
        elif len(number) > 0:
            numbers.append(int(number))
            number = ''
        else:
            pass
    if len(number) > 0:
        numbers.append(int(number))
        number = ''


n_nodes = numbers[0]

n_edges = int((len(numbers) - 1) / 3)

vertice_set = set()
edge_set = set()
edge_dict = {}
vertice_dict = {}

for index in range(n_edges):
    i = index * 3 + 1
    vertice_set.add(numbers[i])
    vertice_set.add(numbers[i + 1])
    edge_dict[f'{numbers[i]}-{numbers[i + 1]}'] = numbers[i + 2]
    edge_dict[f'{numbers[i + 1]}-{numbers[i]}'] = numbers[i + 2]
    edge_set.add(f'{min(numbers[i], numbers[i + 1])}-{max(numbers[i], numbers[i + 1])}')

for vertice in vertice_set:
    vertice_dict[vertice] = []


for edge in edge_dict.keys():
    vertices = edge.split('-')
    start = int(vertices[0])
    end = int(vertices[1])
    vertice_dict[start].append(end)


for vertice in vertice_dict.keys():
    sorted(vertice_dict[vertice])

print('Done')