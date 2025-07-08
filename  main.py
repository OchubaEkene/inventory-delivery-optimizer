from optimizer.route_optimizer import fetch_graph
from optimizer.dijkstra import dijkstra

if __name__ == "__main__":
    graph = fetch_graph()
    start = 1  # Warehouse ID
    distances = dijkstra(graph, start)
    print("Shortest distances from Warehouse:")
    for node, dist in distances.items():
        print(f"Location {node}: {dist} km")
