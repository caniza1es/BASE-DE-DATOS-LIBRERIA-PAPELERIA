CREATE OR REPLACE VIEW total_employees AS (
SELECT * FROM employees
ORDER by branch
);

CREATE OR REPLACE VIEW total_books AS (
SELECT B.id,B.title, B.editorial,B.author,B.genre,SUM(I.amount) as total
FROM books as B, products as P, inventories as I
WHERE B.id = p.id
AND I.product = P.id
GROUP BY B.id,B.title,B.editorial,B.author,B.genre
);

CREATE OR REPLACE VIEW total_stationers AS(
SELECT S.id, S.des, S.company, SUM(I.amount) AS total
FROM stationers as S, products as P, inventories as I
WHERE S.id = P.id
AND I.product = P.id
GROUP BY S.id,S.des,S.company
);
