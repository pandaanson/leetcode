-- CTE to count the bookings for each flight in order of their booking times
WITH RankedBookings AS (
  SELECT 
    p.passenger_id,
    p.flight_id,
    p.booking_time,
    f.capacity,
    ROW_NUMBER() OVER (PARTITION BY p.flight_id ORDER BY p.booking_time) AS booking_rank
  FROM 
    Passengers p
  JOIN Flights f ON p.flight_id = f.flight_id
)

-- Main query to determine the booking status for each passenger
SELECT 
  passenger_id,
  CASE 
    WHEN booking_rank <= capacity THEN 'Confirmed'
    ELSE 'Waitlist'
  END AS Status
FROM 
  RankedBookings
ORDER BY 
  passenger_id;
