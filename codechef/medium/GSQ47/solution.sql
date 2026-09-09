SELECT department, AVG(payout) AS avg_payout
FROM employee
GROUP BY department
HAVING SUM(payout) > 40