def ucs(start, goal, graph):
    frontier = [(0, start, [start])]
    visited = set()

    while frontier:
        frontier.sort()
        cost, node, path = frontier.pop(0)

        if node == goal:
            return path, cost
        if node in visited:
            continue
        visited.add(node)
        for child, weight in graph.get(node, []):
            if child not in visited:
                frontier.append((cost + weight, child, path + [child]))
    return None, float('inf')


def buil_graph():
    graph = {}
    n = int(input("Enter the number of edges: "))
    print("Enter the edges as 'node1 node2 weight': ")
    for _ in range(n):
        u, v, w = input().split()
        w = int(w)
        graph.setdefault(u, []).append((v, w))
        graph.setdefault(v, [])
    return graph


graph = buil_graph()
start = input("Enter the start node: ").strip()
goal = input("Enter the goal node: ").strip()
result, total_cost = ucs(start, goal, graph)

if result:
    print("Path found:", "->".join(result))
    print("Total cost:", total_cost)
else:
    print("No path found")
        
