-- NG
SELECT person_name FROM cte ORDER BY bar, baz;

-- NG
SELECT person_name FROM cte ORDER BY bar;

-- OK
SELECT person_name FROM cte ORDER BY person_id, person_name;