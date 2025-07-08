import psycopg2
from dijkstra import dijkstra

def fetch_graph():
    conn = psycopg2.connect(
        dbname="your_db", user="your_user", password="your_password", host="localhost")
    cursor = conn.cursor()

    cursor.execute("SELECT source, destination, distance FROM routes")
    edges = cursor.fetchall()

    graph = {}
    for src, dst, dist in edges:
        graph.setdefault(src, []).append((dst, dist))
        graph.setdefault(dst, []).append((src, dist))  # undirected

    conn.close()
    return graph
