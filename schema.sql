CREATE DATABASE IF NOT EXISTS filmoreview;
USE filmoreview;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nomeCompleto VARCHAR(100) NOT NULL,
    nomeUsuario VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    dataNascimento DATE NOT NULL,
    senha VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS filmes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nomeFilme VARCHAR(100) NOT NULL,
    anoLancamento YEAR NOT NULL,
    descricaoFilme TEXT,
    imageUrl VARCHAR(500) NOT NULL
);

CREATE TABLE IF NOT EXISTS generoFilmes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fkIdFilme INT NOT NULL,
    genero VARCHAR(50) NOT NULL,

    FOREIGN KEY (fkIdFilme) REFERENCES filmes(id)
);

CREATE TABLE IF NOT EXISTS reviewFilmes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nota TINYINT NOT NULL CHECK (nota BETWEEN 1 AND 5),
    comentario VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fkIdFilme INT NOT NULL,
    fkIdUsuario INT NOT NULL,

    UNIQUE (fkIdUsuario, fkIdFilme),

    FOREIGN KEY (fkIdFilme) REFERENCES filmes(id),
    FOREIGN KEY (fkIdUsuario) REFERENCES usuarios(id)
);