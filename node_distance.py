import collections


def node_distances(nodes_from, nodes_to, g_nodes, g_edges):
    graph = collections.defaultdict(list)

    for link in zip(nodes_from, nodes_to):
        graph[link[0]].append(link[1])
        graph[link[1]].append(link[0])

    print(f"Graph currently: {graph}")

    def find_cycle():
        cycle_nodes = set()
        visited = [False] * (g_nodes + 1)
        parent = [-1] * (g_nodes + 1)

        def dfs(u):
            visited[u] = True

            for v in graph[u]:
                if not visited[v]:
                    parent[v] = u
                    if dfs(v):
                        return True

                # found the cycle
                elif v != parent[u]:
                    cycle_nodes.add(v)

                    current = u

                    while current != v:
                        cycle_nodes.add(current)
                        # go back
                        current = parent[current]

                    return True

            return False

        for i in range(g_nodes):
            if visited[i]:
                continue
            if dfs(i):
                break

        return cycle_nodes

    cycle_nodes = find_cycle()

    distances = [-1] * (g_nodes + 1)

    for node in cycle_nodes:
        # obviously every node in the cycle is 0 distance from the cycle
        distances[node] = 0

    # use BFS to find the shortest distance from each node to the cycle node
    for i in range(1,g_nodes+1):
        print(f"Performing BFS on node {i}")
        if distances[i] == -1:
            continue

        queue = collections.deque([i])

        while queue:
            print(f"State of queue: {queue}")
            u = queue.popleft()
            for v in graph[u]:
                if distances[v] != -1:
                    continue
                else:
                    distances[v] = distances[u] + 1
                queue.append(v)

    return distances[1:]


# Test cases
nodes_from = [1, 2, 1, 3, 1, 2]
nodes_to = [2, 3, 3, 5, 4, 6]
g_nodes = 6
g_edges = 6

distances_from_cycle = node_distances(
    nodes_from=nodes_from, nodes_to=nodes_to, g_nodes=g_nodes, g_edges=g_edges
)

print(f"Distances from cycle: {distances_from_cycle}")

nodes_from = [1, 2, 1, 3, 3, 1, 2]
nodes_to = [2, 3, 4, 4, 5, 7, 6]
g_nodes = 7
g_edges = 7

distances_from_cycle = node_distances(
    nodes_from=nodes_from, nodes_to=nodes_to, g_nodes=g_nodes, g_edges=g_edges
)

print(f"Distances from cycle: {distances_from_cycle}")