-- database: :memory:
-- Esquema do banco de dados SQLite

CREATE TABLE IF NOT EXISTS ferramentas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kit_id INTEGER,
    codigo TEXT NOT NULL,
    descricao TEXT,
    numero_serie TEXT,
    estado TEXT,
    FOREIGN KEY (kit_id) REFERENCES kits(id)
);

CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT UNIQUE NOT NULL,
    senha_hash TEXT NOT NULL,
    papel TEXT NOT NULL
);

