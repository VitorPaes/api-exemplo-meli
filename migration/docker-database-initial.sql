CREATE TABLE IF NOT EXISTS items
(
    title varchar ,
    price numeric,
    initial_quantity int,
    available_quantity int,
    sold_quantity int,
    condition varchar,
    id serial primary key
);
