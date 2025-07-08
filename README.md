# 🚚 Inventory & Delivery Optimization System

An algorithm-focused backend project that simulates real-world delivery route optimization and inventory tracking. Built using Python and PostgreSQL, and structured for scalability and performance.

## 🔧 Technologies
- Python 3
- PostgreSQL
- Dijkstra’s Algorithm
- SQL (normalized schema & optimized queries)
- Flask (optional API layer)

## 📦 Features

- 🚛 **Route Optimization**: Uses Dijkstra’s algorithm to find shortest paths between warehouse and shops.
- 📊 **Scalable Inventory Schema**: Normalized PostgreSQL database for clean data operations.
- ⚙️ **Efficient Querying**: Indexes, joins, and query plans considered for performance.
- 🌐 **REST API (Optional)**: Expose optimization endpoints using Flask.

## 📁 Schema Overview

```sql
TABLE inventory (
  id SERIAL PRIMARY KEY,
  product_name VARCHAR,
  quantity INT
)

TABLE locations (
  id SERIAL PRIMARY KEY,
  name VARCHAR
)

TABLE routes (
  id SERIAL PRIMARY KEY,
  source INT,
  destination INT,
  distance FLOAT
)

Sample Data

The `data/` folder contains CSVs to simulate real-world data:

- `sample_locations.csv`: Warehouses and shops
- `sample_routes.csv`: Route network with distances
- `sample_inventory.csv`: Product quantities available

Setup
Clone the repo

Setup PostgreSQL and run db/schema.sql + db/seed.sql

Run main.py to test the optimizer

(Optional) Run app.py to start the Flask API

Algorithm: Dijkstra’s
This project includes a clean implementation of Dijkstra’s algorithm using Python’s heapq, allowing fast route optimization from the warehouse to multiple shops.

Example Output
Shortest distances from Warehouse:
Location 1: 0 km
Location 2: 5 km
Location 3: 8 km
Location 4: 10 km
