CREATE OR REPLACE VIEW total_employees AS (
SELECT * FROM employees
ORDER by branch
);

CREATE OR REPLACE view total_inventories AS (
SELECT P.des, P.id,SUM(I.amount) as TOTAl
FROM products as P, inventories as I
WHERE P.id = I.product
GROUP BY P.des,P.id
);

CREATE VIEW total_books AS (
SELECT B.title, B.editorial,B.author,B.genre,SUM(I.amount) as total
FROM books as B, products as P, inventories as I
WHERE B.id = p.id
AND I.product = P.id
GROUP BY B.title,B.editorial,B.author,B.genre
);
