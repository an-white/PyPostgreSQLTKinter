CREATE TABLE stundents(id Serial, name text, address text, age int)
INSERT INTO
    stundents(name, address, age)
VALUES
    ("Juan", "Casa", 25)
INSERT INTO
    stundents(name, address, age)
VALUES
    ("Pedro", "Casa Pedro", 28)
select
    *
from
    stundents