import collections


class Graph(object):
    def __init__(self):
        self.vertex_dict = {}
        self.graph = collections.defaultdict(set)

    def add_vertex(self, value):
        if value not in self.vertex_dict:
            self.vertex_dict[value] = Vertex(value)

    def add_edge(self, value1, value2):
        # 构建无向图
        self.add_vertex(value1)
        self.add_vertex(value2)
        self.graph[self.vertex_dict[value1]].add(self.vertex_dict[value2])
        self.graph[self.vertex_dict[value2]].add(self.vertex_dict[value1])

    def get_edge(self, value):
        return self.graph[self.get_vertex(value)]

    def get_vertex(self, value):
        return self.vertex_dict[value]

class Vertex(object):
    def __init__(self, value):
        self.value = value
        self.color = 'white'
