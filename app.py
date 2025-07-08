from flask import Flask, jsonify
from optimizer.route_optimizer import fetch_graph
from optimizer.dijkstra import dijkstra

app = Flask(__name__)

@app.route("/optimize/<int:start_id>")
def optimize(start_id):
    graph = fetch_graph()
    distances = dijkstra(graph, start_id)
    return jsonify(distances)

if __name__ == "__main__":
    app.run(debug=True)
