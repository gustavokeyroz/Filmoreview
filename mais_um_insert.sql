USE filmoreview;

INSERT INTO filmes (nomeFilme, anoLancamento, descricaoFilme, imageUrl)
VALUES (
    'Wildwood',
    '2026',
    'Prue McKeel embarca em uma jornada por uma floresta misteriosa para resgatar seu irmão.',
    'https://www.themoviedb.org/t/p/w600_and_h900_face/mcuUYNWGJHPEaRumOlgSZCzMRPc.jpg'
);

INSERT INTO generoFilmes (fkIdFilme, genero)
SELECT id, 'Fantasia'
FROM filmes
WHERE nomeFilme = 'Wildwood';