CREATE TABLE IF NOT EXISTS sensores(id INTEGER PRIMARY KEY,
                                    temperatura REAL, umidade REAL, nome TEXT,
                                    tempo TIMESTAMP DEFAULT (DATETIME('now')))

INSERT INTO sensores(temperatura, umidade, nome)
            VALUES(temperatura, umidade, nome)

SELECT * FROM sensores ORDER BY datetime(tempo) ASC

SELECT * FROM sensores ORDER BY datetime(tempo) DESC LIMIT 10
