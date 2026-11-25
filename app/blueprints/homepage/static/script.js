var bannerHomePage = document.getElementById('bannerHomePage')

bannerHomePage.src = 'https://image.tmdb.org/t/p/original/cV233Rnd50BBQgya18Bp4WZ7epN.jpg';

const carousel = document.querySelector('.carousel');
const lista = document.querySelector('.card-list');
const prev = document.querySelector('.carousel-btn.prev');
const next = document.querySelector('.carousel-btn.next');

let posicao = 0;

function limiteMaximo() {
    return lista.offsetWidth - carousel.clientWidth;
}

function atualizarBotoes() {
    prev.disabled = posicao <= 0;
    next.disabled = posicao >= limiteMaximo();
}

function mover(direcao) {
    const passo = carousel.clientWidth;

    posicao = Math.max(
        0,
        Math.min(posicao + direcao * passo, limiteMaximo())
    );

    lista.style.transform = `translateX(${-posicao}px)`;

    atualizarBotoes();
}

prev.onclick = () => mover(-1);
next.onclick = () => mover(1);

window.addEventListener('resize', () => {
    posicao = Math.min(posicao, limiteMaximo());
    lista.style.transform = `translateX(${-posicao}px)`;
    atualizarBotoes();
});

atualizarBotoes();