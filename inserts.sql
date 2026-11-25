USE filmoreview;

INSERT INTO filmes
(nomeFilme, anoLancamento, descricaoFilme, imageUrl)
VALUES
(
    'Interstellar',
    2014,
    'Um grupo de exploradores viaja pelo espaço em busca de um novo lar para a humanidade.',
    'https://www.themoviedb.org/t/p/w600_and_h900_face/tR1XVa5bxgdh2bRw2u0DzrgkO2l.jpg'
);

INSERT INTO generoFilmes (fkIdFilme, genero)
SELECT id, 'Ficção científica' FROM filmes WHERE nomeFilme = 'Interstellar';