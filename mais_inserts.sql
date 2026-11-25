USE filmoreview;

INSERT INTO filmes (nomeFilme, anoLancamento, descricaoFilme, imageUrl)
VALUES
(
    'Clube da Luta',
    '1999',
    'Um homem insatisfeito com sua vida conhece Tyler Durden e juntos criam um clube de luta clandestino.',
    'https://image.tmdb.org/t/p/w500/bptfVGEQuv6vDTIMVCHjJ9Dz8PX.jpg'
),
(
    'La La Land',
    '2016',
    'Uma atriz aspirante e um pianista de jazz tentam realizar seus sonhos enquanto desenvolvem um relacionamento.',
    'https://image.tmdb.org/t/p/w500/uDO8zWDhfWwoFdKS4fzkUJt0Rf0.jpg'
),
(
    'Parasita',
    '2019',
    'Uma família de baixa renda encontra uma oportunidade de mudar de vida ao se infiltrar na rotina de uma família rica.',
    'https://image.tmdb.org/t/p/w500/7IiTTgloJzvGI1TAYymCfbfl3vT.jpg'
),
(
    'O Poderoso Chefão',
    '1972',
    'A história da família Corleone e de seu envolvimento com o crime organizado.',
    'https://image.tmdb.org/t/p/w500/3bhkrj58Vtu7enYsRolD1fZdja1.jpg'
),
(
    'Whiplash',
    '2014',
    'Um jovem baterista enfrenta métodos extremos de ensino enquanto busca se tornar um grande músico.',
    'https://image.tmdb.org/t/p/w500/7fn624j5lj3xTme2SgiLCeuedmO.jpg'
),
(
    'Matrix',
    '1999',
    'Um programador descobre que a realidade em que vive é uma simulação controlada por máquinas.',
    'https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg'
),
(
    'O Show de Truman',
    '1998',
    'Um homem começa a questionar sua realidade e descobre que sua vida pode não ser aquilo que parece.',
    'https://image.tmdb.org/t/p/w500/vuza0WqY239yBXOadKlGwJsZJFE.jpg'
),
(
    'Corra!',
    '2017',
    'Um jovem visita a família de sua namorada e percebe que há algo muito estranho naquele lugar.',
    'https://image.tmdb.org/t/p/w500/tFXcEccSQMf3lfhfXKSU9iRBpa3.jpg'
),
(
    'Toy Story',
    '1995',
    'Os brinquedos de um menino ganham vida quando não há humanos por perto.',
    'https://image.tmdb.org/t/p/w500/uXDfjJbdP4ijW5hWSBrPrlKpxab.jpg'
),
(
    'Homem-Aranha no Aranhaverso',
    '2018',
    'Miles Morales descobre seus poderes e conhece versões alternativas do Homem-Aranha.',
    'https://image.tmdb.org/t/p/w500/iiZZdoQBEYBv6id8su7ImL0oCbD.jpg'
),
(
    'Oppenheimer',
    '2023',
    'A trajetória do físico J. Robert Oppenheimer durante o desenvolvimento da primeira bomba atômica.',
    'https://image.tmdb.org/t/p/w500/ptpr0kGAckfQkJeJIt8st5dglvd.jpg'
);

INSERT INTO generoFilmes (fkIdFilme, genero)
SELECT id, 'Drama' FROM filmes WHERE nomeFilme = 'Clube da Luta';

INSERT INTO generoFilmes (fkIdFilme, genero)
SELECT id, 'Musical' FROM filmes WHERE nomeFilme = 'La La Land';

INSERT INTO generoFilmes (fkIdFilme, genero)
SELECT id, 'Drama' FROM filmes WHERE nomeFilme = 'Parasita';

INSERT INTO generoFilmes (fkIdFilme, genero)
SELECT id, 'Crime' FROM filmes WHERE nomeFilme = 'O Poderoso Chefão';

INSERT INTO generoFilmes (fkIdFilme, genero)
SELECT id, 'Drama' FROM filmes WHERE nomeFilme = 'Whiplash';

INSERT INTO generoFilmes (fkIdFilme, genero)
SELECT id, 'Ficção Científica' FROM filmes WHERE nomeFilme = 'Matrix';

INSERT INTO generoFilmes (fkIdFilme, genero)
SELECT id, 'Comédia' FROM filmes WHERE nomeFilme = 'O Show de Truman';

INSERT INTO generoFilmes (fkIdFilme, genero)
SELECT id, 'Terror' FROM filmes WHERE nomeFilme = 'Corra!';

INSERT INTO generoFilmes (fkIdFilme, genero)
SELECT id, 'Animação' FROM filmes WHERE nomeFilme = 'Toy Story';

INSERT INTO generoFilmes (fkIdFilme, genero)
SELECT id, 'Animação' FROM filmes WHERE nomeFilme = 'Homem-Aranha no Aranhaverso';

INSERT INTO generoFilmes (fkIdFilme, genero)
SELECT id, 'Drama' FROM filmes WHERE nomeFilme = 'Oppenheimer';