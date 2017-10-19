CREATE TABLE IF NOT EXISTS sensores(id INTEGER PRIMARY KEY,
                                    nome TEXT NOT NULL,
                                    temperatura REAL, umidade REAL,
                                    tempo TIMESTAMP DEFAULT (DATETIME('now')))

INSERT INTO sensores(temperatura, umidade, nome)
            VALUES(27.5, 71.0, 'TESTE1')

SELECT * FROM sensores ORDER BY datetime(tempo) ASC

SELECT * FROM sensores ORDER BY datetime(tempo) DESC LIMIT 10
