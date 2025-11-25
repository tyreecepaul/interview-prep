class Node:
    def __init__(self, value):
        self.value = value
        self.neighbours = []

def dfs(graph, start, target):
    if start not in graph:
        return []

    visited = set()
    path = []

    def dfs_path(node):
        visited.add(node)
        path.append(node)
        
        if node == target:
            return True
        for neighbour in node.neighbours:
            if neighbour not in visited and dfs_path(neighbour):
                return True

        path.pop()
        return False

    if dfs_path(start):
        return path
    return []

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
    
    path = dfs(graph, n1, n3)
    print([node.value for node in path])

if __name__ == "__main__":
    main()

