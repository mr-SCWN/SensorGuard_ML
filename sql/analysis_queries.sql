-- 1. Show the first 10 rows from the machine_measurements table
SELECT * 
FROM machine_measurements
LIMIT 10;


-- 2. Count all rows in the machine_measurements table
-- Your SQL query here:
SELECT COUNT(*)
FROM machine_measurements;

-- 3. Show all records where machine_failure equals 1
-- Your SQL query here:
SELECT udi, product_id, product_type, machine_failure , twf , hdf  ,pwf , osf , rnf 
FROM machine_measurements
WHERE machine_failure = 1;

-- 4. Show unique product types
-- Your SQL query here:
SELECT DISTINCT product_type
FROM machine_measurements;

-- 5. Count the number of records for each product type
-- Your SQL query here:
SELECT product_type,  COUNT(*) as records_count 
FROM machine_measurements
GROUP BY product_type ;

-- 6. Count the number of records for each machine_failure value
-- Your SQL query here:
SELECT machine_failure , COUNT(*) as records_count
FROM machine_measurements
GROUP BY machine_failure;

-- 7. Calculate the average torque and average tool wear for each product type
-- Your SQL query here:
SELECT product_type, AVG(torque_nm) as avg_torque_nm, AVG(tool_wear_min) as avg_tool_wear_min
FROM machine_measurements
GROUP BY product_type;

-- 8. Show product types where the average torque is greater than 40
-- Your SQL query here:
SELECT product_type, AVG(torque_nm) AS avg_torque_nm
FROM machine_measurements
GROUP BY product_type
HAVING AVG(torque_nm) > 40;

-- 9. Show the 10 records with the highest tool wear
-- Your SQL query here:
SELECT udi, product_id, product_type , tool_wear_min
FROM machine_measurements
ORDER BY tool_wear_min DESC
LIMIT 10;


-- 10. Calculate the total number of each failure type: twf, hdf, pwf, osf, rnf
-- Your SQL query here:
SELECT SUM(twf) AS total_twf, SUM(hdf) AS total_hdf, 
    SUM(pwf) AS total_pwf, SUM(osf) AS total_osf, 
    SUM(rnf) AS total_rnf
FROM machine_measurements;