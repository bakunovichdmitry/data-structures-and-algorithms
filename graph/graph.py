from copy import copy

graph = {
    "A": {"B": 1},
    "B": {"C": 2},
    "C": {"D": 2, "E": 4},
    "D": {"C": 3, "B": 1},
    "E": {"D": 5},
}


class PathQueue:
    def __init__(self):
        self.holder = []

    def enqueue(self, val):
        self.holder.append(val)

    def dequeue(self):
        value = None
        try:
            value = self.holder[0]
            if len(self.holder) == 1:
                self.holder = []
            else:
                self.holder = self.holder[1:]
        except IndexError:
            pass
        return value

    def is_empty(self):
        result = False
        if len(self.holder) == 0:
            result = True
        return result


def get_all_way(graph, start, end, q):
    temp_path = [start]
    q.enqueue(temp_path)
    while not q.is_empty():
        tmp_path = q.dequeue()
        last_node = tmp_path[len(tmp_path) - 1]
        if last_node == end:
            print(tmp_path)
        for link_node in graph[last_node]:
            if link_node not in tmp_path:
                new_path = list()
                new_path = tmp_path + [link_node]
                q.enqueue(new_path)


def dijkstra(graph, node1, node2):
    labels = {}
    order = {}
    for i in graph.keys():
        if i == node1:
            labels[i] = 0
        else:
            labels[i] = float("inf")
    temp_drop_labels = copy(labels)
    while len(temp_drop_labels) > 0:
        min_node = min(temp_drop_labels, key=temp_drop_labels.get)
        for _ in graph[min_node]:
            if labels[_] > (labels[min_node] + graph[min_node][_]):
                labels[_] = labels[min_node] + graph[min_node][_]
                temp_drop_labels[_] = labels[min_node] + graph[min_node][_]
                order[_] = min_node
        del temp_drop_labels[min_node]
    return labels[node2]


def find_center(min_way_array):
    inverted_list = [[] for _ in min_way_array]
    for i in range(len(min_way_array)):
        for j in range(len(min_way_array)):
            inverted_list[i].append(min_way_array[j][i])
    graph_center = min(max(i) for i in inverted_list)
    return graph_center


label_list = ["A", "B", "C", "D", "E"]
path_queue = PathQueue()

print("All way from node to node:")
get_all_way(graph, "A", "D", path_queue)

print("\nМinimum way weight:", dijkstra(graph, "A", "E"))

value_matrix = list()
for i in label_list:с
    temp_list = list()
    for j in label_list:
        temp_list.append(dijkstra(graph, node1=i, node2=j))
    value_matrix.append(temp_list)
print("Center: ", find_center(value_matrix))
