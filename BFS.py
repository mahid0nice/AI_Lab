def bfs(graph,start,goal):
    queue = [start]
    visited ={start}
    parent = {start: None}
    while queue:
        node = queue.pop(0)
        if node == goal:
            return reconstruct_path(parent,start,goal)
        for child in graph.get(node, []):
            if child not in visited:
                visited.add(child)
                parent[child] = node
                queue.append(child)
    return None
def reconstruct_path(parent,start,goal):
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()
    return path

def build_graph():
    graph = {}
    n = int(input("Enter the number of edges: "))
    print("Enter the edges in the format 'node1 node2' :")
    for _ in range(n):
        u, v = input().split()
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, [])
    return graph


graph = build_graph()

start = input("enter start node: ").strip()
goal = input("enter goal node: ").strip()

result = bfs(graph,start,goal)
if result:
    print("Path found:", " -> ".join(result))
else:
    print("No path found from", start, "to", goal)