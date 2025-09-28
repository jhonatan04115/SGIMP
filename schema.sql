-- database: :memory:
-- Esquema do banco de dados SQLite
CREATE TABLE IF NOT EXISTS kits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo TEXT UNIQUE NOT NULL,
    serie TEXT,
    descricao TEXT,
    localizacao TEXT,
    status TEXT,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ferramentas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kit_id INTEGER,
    codigo TEXT NOT NULL,
    descricao TEXT,
    numero_serie TEXT,
    estado TEXT,
    FOREIGN KEY (kit_id) REFERENCES kits(id)
);

CREATE TABLE IF NOT EXISTS movimentacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_type TEXT NOT NULL,
    item_id INTEGER NOT NULL,
    operador TEXT NOT NULL,
    tipo TEXT NOT NULL,
    data DATETIME DEFAULT CURRENT_TIMESTAMP,
    observacao TEXT
);

CREATE TABLE IF NOT EXISTS documentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    tipo TEXT,
    relacionado_type TEXT,
    relacionado_id INTEGER,
    arquivo_path TEXT,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT UNIQUE NOT NULL,
    senha_hash TEXT NOT NULL,
    papel TEXT NOT NULL
);
