def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    visited = set()
    while True:
        min_distance = float('inf')
        min_vertex = None
        for vertex, distance in distances.items():
            if vertex not in visited and distance < min_distance:
                min_distance = distance
                min_vertex = vertex
        if min_vertex is None:
            break
        visited.add(min_vertex)
        for neighbor, weight in graph[min_vertex]:
            if neighbor not in visited:
                distance_through_min = distances[min_vertex] + weight
                if distance_through_min < distances[neighbor]:
                    distances[neighbor] = distance_through_min
    
    return distances


graph = {
    'A': [('B', 3), ('C', 1)],
    'B': [('C', 7), ('D', 5)],
    'C': [('B', 7), ('D', 2)],
    'D': []
}

start_vertex = 'A'
shortest_distances = dijkstra(graph, start_vertex)
print("SSSP from starting vertex ", start_vertex)
print(shortest_distances)

