
<!--

- SELECT
- Aggregate functions like count, >, <, avg
- WHERE
- Group By
- Joins

to copy data in after creating a table use
\COPY <csv file> FROM <'path'> WITH CSV HEADER;


Join tables should be last because they have dependencies

EXPORT current schema of a database using POSTGRES DUMP from command line
pg_dump <name of database> > <file_name>.sql

---------------------------------------------
QUERIES  ARE CASE SENSITIVE
- SELECT gathers rows from a table
    SELECT * requests all columns and rows 
        SELECT * FROM car;
    SELECT <column_name, column_name> FROM car;
        SELECT make, model FROM car;
- WHERE makes query is more granular than every column
    SELECT * FROM car WHERE id=3;
    SELECT * FROM car WHERE make = 'FORD';
    SELECT id, make, model FROM car WHERE color = 'blue';
- Math operators
    > Greater than
    < Less Than
    = Equal to
        Variants of the above 3
- COUNT
    SELECT COUNT(*) FROM car;
    SELECT COUNT(*) WHERE price >20;
    SELECT COUNT(DISTINCT color) FROM car;  <-- only counts unique entries
- SUM
    SELECT SUM(price) AS total_revenue FROM service;
        total_revenue is an alias for the query, like a variable

- AVG (Average)
    SELECT AVG(price) AS average_price) FROM services;

-LIKE search substring
    SELECT name_of_service LIKE '%Brake%';
        % is a wildcard, returns anything with 'Brake' in value within column name_of_service

- AND / OR
    SELECT * FROM driver WHERE name LIKE '%Johnson%' AND age > 30;
        next OR statements within ()

- ILIKE (not case sensitive)
    SELECT * FROM driver WHERE name ILIKE '%johnson%';

- IN 
    SELECT * FROM driver WHERE id IN (1,4,5,9);

-LOWER
    SELECT * FROM car WHERE LOWER(color) IN ('blue','red');

- LIMIT
    SELECT * FROM driver LIMIT 5;

-DESC (descending)
    SELECT * FROM car ORDER BY year DESC LIMIT 3;
        Finds the three newest cars

- GROUP BY
    SELECT make, COUNT(*) AS car_count FROM car GROUP BY make;
        counts car makes and groups them by make
    SELECT color, COUNT(*) as car_colors FROM car GROUP BY color;
        lists the colors available and their counts listed in a group (column) called car_colors
    SELECT color, COUNT(*) AS car_colors FROM car WHERE LOWER(color) IN ('red','blue','green') GROUP BY color ORDER by car_color DESC;

- CASE  (conditional)
    SELECT CASE WHEN price <30 THEN 'low' WHEN price < 50 THEN 'medium' ELSE 'high' END AS price_range,
        COUNT(*) AS service_count FROM service GROUP BY price_range;

----------------------------------------------------------

Joins get data from multiple tables using foreign keys
    This is essentially a venn diagram

SELECT driver.name, car.make, car.model FROM car
JOIN driver ON car.driver = driver.id

Can add to it

SELECT driver.name, car.make, car.model FROM car
JOIN driver on car.driver = driver.id
WHERE driver.name ILIKE '%d%'
    returns a table merging car and driver tables where car.driver and driver.id martch and there is a 'd' in the name of the driver


LEFT/RIGHT JOIN LEFT/RIGHT OUTER/INNER JOIN, default is inner

SELECT driver.name AS the_driver_name, car.make, car.model FROM driver   <-- taking from driver table and car table
LEFT JOIN car   <-- left is the first talbe, in this case 'FROM driver' above and joins with data from car
ON driver.id = car.driver  <-- take instance where driver.id matches car.driver
WhHERE car.make IS NULL <-- Where the driver has no car
    Returns drivers without cars

Can join multiple tables, not just 2

SELECT driver.name AS the_driver_name, car.make AS car_make, car.model AS car_model, car_service.id as car_service_id, services.name_of_service, services.price
FROM driver
JOIN car ON driver.id = car.driver
JOIN car_service ON car.id = car_service.car_id
JOIN services ON car_service=car_id = services.id

SELECT car.make, car.model, plate.plate_number
FROM car
JOIN plate ON car.id = plate.car_id

