from graph import Graph


def buid_graph():
    knight_graph = Graph()

    def get_neighbors(row, column):
        nerighbors = []
        for i, j in [(-1, -2), (-1, 2), (1, -2), (1, 2),
                     (-2, 1), (-2, -1), (2, 1), (2, -1)]:
            new_row = row + i
            new_column = column + j
            if 0 <= new_row < n and 0 <= new_column < n:
                nerighbors.append(new_row * n + new_column)
        return nerighbors

    for i in range(0, n):
        for j in range(0, n):
            item = i * n + j
            for nerighbor in get_neighbors(i, j):
                knight_graph.add_edge(item, nerighbor)
    return knight_graph


def find_route(path, start):
    if len(path) == n ** 2 - 1:
        path.append(start)
        knight_graph.get_vertex(start).color = 'black'
        return True

    path.append(start)
    knight_graph.get_vertex(start).color = 'black'

    for neighbor in knight_graph.get_edge(start):
        if neighbor.color == 'white':
            done = find_route(path, neighbor.value)
            if done:
                return True
            else:
                path.pop()
                neighbor.color = 'white'
    return False


n = 5
knight_graph = buid_graph()

path = []
print(find_route(path, 0))
print(path)
