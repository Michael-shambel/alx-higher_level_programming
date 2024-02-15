-- Import in hbtn_0c_0 database this table dump: download

-- Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
-- USE hbtn_0c_0;
-- SOURCE temperatures.sql;

SELECT `city`, AVG(`VALUE`) AS `avg_temp` 
FROM `temperatures` 
GROUP BY `city` 
ORDER BY `avg_temp` DESC;
