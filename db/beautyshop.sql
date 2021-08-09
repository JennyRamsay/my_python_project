DROP TABLE IF EXISTS appointments;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS treatments;

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255),
    customership VARCHAR(255),
    status VARCHAR(255)
);

CREATE TABLE treatments (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    day_of_week VARCHAR(255),
    time VARCHAR(255),
    capacity INT
);

CREATE TABLE appointments (
    id SERIAL PRIMARY KEY,
    customer_id SERIAL REFERENCES customers(id),
    treatment_id SERIAL REFERENCES treatments(id) ON DELETE CASCADE
);