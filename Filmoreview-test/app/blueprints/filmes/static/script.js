var header = document.getElementById('header');
var opcoesPesquisa = document.getElementById('opcoesPesquisa');

headerAltura = header.offsetHeight;
headerWidth = header.offsetWidth;
opcoesPesquisa.style.marginTop = `calc(${headerAltura}px + 1%)`;
opcoesPesquisa.style.width = `calc(${headerWidth}px)`

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
    const passo = carousel.clientWidth; // uma "página"

    posicao = Math.max(0, Math.min(posicao + direcao * passo, limiteMaximo()));
    lista.style.transform = `translateX(${-posicao}px)`;
    atualizarBotoes();
}

prev.onclick = () => mover(-1);
next.onclick = () => mover(1);

// Reajusta se a janela mudar de tamanho
window.addEventListener('resize', () => mover(0));

atualizarBotoes();