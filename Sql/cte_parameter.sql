use car


DECLARE @CARID INT = 401;
--SET @CARID = 401;

WITH cte_car AS (
    SELECT c.carid, c.carname, cd.cardescription
    FROM car AS c
    INNER JOIN CarDescription AS cd ON c.CarID = cd.CarID
)

-- Use carid in the WHERE clause instead of cte_car
SELECT * 
FROM cte_car 
WHERE carid > @CARID;
