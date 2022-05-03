CREATE OR REPLACE VIEW total_employees AS (
SELECT * FROM employees
ORDER by branch
);

CREATE OR REPLACE VIEW total_clients AS (
SELECT * FROM clients
ORDER BY name ASC
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

CREATE OR REPLACE VIEW products_sold AS(
SELECT P.id, COUNT(P.id) AS sold
FROM products as P,receipts_desc as R
WHERE R.product = P.id
GROUP BY P.id
);

CREATE OR REPLACE VIEW msold_product AS(
SELECT M.id, M.sold, 
  RANK () OVER ( 
		ORDER BY M.sold DESC
	) sold_rank
  FROM products_sold AS M
);

CREATE OR REPLACE VIEW msold_book AS(
	SELECT B.id,B.title,A.name,M.sold,
  	RANK () OVER ( 
		ORDER BY M.sold DESC
	) sold_rank 
  	FROM books as B, msold_product as M,authors as A
  	WHERE B.id = M.id
  	and A.id = B.author
);

CREATE OR REPLACE VIEW nor_employees AS (
WITH RECURSIVE branch_employees AS (
    SELECT
        cc,
        name,
        occupation,
        working_since,
  		email
    FROM
        employees
    WHERE
        employees.branch = 'Sucursal Norte'
    UNION
        SELECT
            e.cc,
            e.name,
            e.occupation,
  			e.working_since,
  			e.email
        FROM
            employees e
        INNER JOIN branch_employees s ON s.cc = e.cc
)
SELECT * FROM branch_employees
);

