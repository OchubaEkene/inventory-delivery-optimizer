CREATE TABLE inventory (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    quantity INT
);

CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE routes (
    id SERIAL PRIMARY KEY,
    source INT REFERENCES locations(id),
    destination INT REFERENCES locations(id),
    distance FLOAT
);
