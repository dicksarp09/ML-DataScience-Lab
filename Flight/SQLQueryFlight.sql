SELECT * FROM [dbo].[flights]

SELECT DISTINCT Airline from [dbo].[flights]
ORDER BY Airline

SELECT DISTINCT Airline,  Destination, 
from [dbo].[flights]

SELECT DISTINCT Airline, Destination, SUM (Price) AS Revenue
FROM [dbo].[flights]
WHERE Airline = 'Jet Airways'
GROUP BY Airline, Destination

SELECT DISTINCT Airline, Destination, SUM (Price) AS Revenue
FROM [dbo].[flights]
WHERE Airline = 'Air India'
GROUP BY Airline, Destination

SELECT DISTINCT Airline, Destination, SUM (Price) AS Revenue
FROM [dbo].[flights]
WHERE Airline = 'IndiGo'
GROUP BY Airline, Destination

SELECT DISTINCT Airline, Destination, SUM (Price) AS Revenue
FROM [dbo].[flights]
WHERE Airline = 'SpiceJet'
GROUP BY Airline, Destination

SELECT DISTINCT Airline, Destination, SUM (Price) AS Revenue
FROM [dbo].[flights]
WHERE Airline = 'Vistara'
GROUP BY Airline, Destination

SELECT DISTINCT Airline, Destination, SUM (Price) AS Revenue
FROM [dbo].[flights]
WHERE Airline = 'Air Asia'
GROUP BY Airline, Destination

SELECT DISTINCT Airline, Destination, SUM (Price) AS Revenue
FROM [dbo].[flights]
WHERE Airline = 'GoAir'
GROUP BY Airline, Destination

SELECT DISTINCT Airline, Destination, SUM (Price) AS Revenue
FROM [dbo].[flights]
WHERE Airline = 'SpiceJet'
GROUP BY Airline, Destination

SELECT Airline,SUM (Price) AS Revenue
FROM [dbo].[flights]
WHERE Airline = 'Air India'
GROUP BY Airline


SELECT
    Airline,
    COUNT(Destination) AS TotalFlights,
    COUNT(Price) * 100.0 / SUM(COUNT(Price)) OVER () AS MarketShare
FROM
    dbo.flights
GROUP BY
    Airline;


SELECT DISTINCT Destination FROM [dbo].[flights]