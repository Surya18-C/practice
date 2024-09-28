
use car


CREATE PROCEDURE car_car

@CARID INT

AS
BEGIN
    SELECT Car.CarID, Car.CarName, cd.CarDescription 
    FROM Car
    INNER JOIN CarDescription AS cd 
    ON Car.CarID = cd.CarID WHERE Car.CarID=@CARID
END;

-- To execute the procedure
EXEC car_car @CARID=201;



select * from car

select * from CarDescription
