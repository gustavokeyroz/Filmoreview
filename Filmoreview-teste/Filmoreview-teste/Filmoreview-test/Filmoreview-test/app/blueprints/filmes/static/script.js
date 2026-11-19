var header = document.getElementById('header');
var opcoesPesquisa = document.getElementById('opcoesPesquisa');

headerAltura = header.offsetHeight;
headerWidth = header.offsetWidth;
opcoesPesquisa.style.marginTop = `calc(${headerAltura}px + 1%)`;
opcoesPesquisa.style.width = `calc(${headerWidth}px)`

const carousel = document.querySelector('.carousel');
const lista = document.querySelector('.card-list');
let posicao = 0;

function mover(direcao) {
    const passo = carousel.clientWidth;                    // uma "página"
    const max = lista.offsetWidth - carousel.clientWidth;  // até onde pode ir

    posicao = Math.max(0, Math.min(posicao + direcao * passo, max));
    lista.style.transform = `translateX(${-posicao}px)`;
}

document.querySelector('.prev').onclick = () => mover(-1);
document.querySelector('.next').onclick = () => mover(1);