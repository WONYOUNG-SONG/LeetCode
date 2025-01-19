# Write your MySQL query statement below
SELECT p.firstName AS firstName, p.lastName AS lastName, a.city as city, a.state as state
FROM Person AS p
LEFT JOIN Address AS a
ON p.PersonId = a.PersonId
