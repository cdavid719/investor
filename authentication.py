DROP TABLE IF EXISTS auth


CREATE TABLE auth
(
    username text NOT NULL,
    pass text NOT NULL,
    role text NOT NULL
)

CREATE TABLE houses
(
    house text NOT NULL,
    price int NOT NULL,
)


INSERT INTO auth VALUES
('investor', 'passw', 'user')


SELECT * FROM auth

COMMIT
