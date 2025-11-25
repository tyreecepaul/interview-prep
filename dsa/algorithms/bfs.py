from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbours = []

def bfs(graph, start, target):
    if start not in graph:
        return []

    visited = set()
    queue = deque([start])
    parent = {start: None} # keep track of parent

    while queue:
        node = queue.popleft()
        if node == target:
            path = []
            # reconstruct the path
            while node:
                path.append(node)
                node = parent[node]
            return path[::-1]

        visited.add(node)
        for neighbour in node.neighbours:
            if neighbour not in visited and neighbour not in parent:
                parent[neighbour] = node
                queue.append(neighbour)

    result = [] # target not found


def main():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    n1.neighbours = [n2, n3]
    n2.neighbours = [n1, n4]
    n3.neighbours = [n1, n4]
    n4.neighbours = [n2, n3]

    graph = {n1, n2, n3, n4}
    
    path = bfs(graph, n1, n3)
    print([node.value for node in path])

if __name__ == "__main__":
    main()
