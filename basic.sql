CREATE OR REPLACE VIEW total_employees AS (
SELECT * FROM employees
ORDER by branch
);

create view total_inventories AS (
SELECT P.des, P.id,SUM(I.amount) as TOTAl
FROM products as P, inventories as I
WHERE P.id = I.product
GROUP BY P.des,P.id
)
