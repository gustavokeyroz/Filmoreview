var header = document.getElementById('header');
var divFilmes = document.getElementById('filmes');

headerAltura = header.offsetHeight;
headerWidth = header.offsetWidth;

divFilmes.style.marginTop = `calc(${headerAltura}px + 1%)`;
divFilmes.style.width = `calc(${headerWidth}px)`;

const carrosseis = document.querySelectorAll('.carousel');

carrosseis.forEach(carousel => {

    const lista = carousel.querySelector('.card-list');

    const controles = carousel.previousElementSibling
        .previousElementSibling
        .querySelector('.carousel-controls');

    const prev = controles.querySelector('.carousel-btn.prev');
    const next = controles.querySelector('.carousel-btn.next');

    let posicao = 0;

    function limiteMaximo() {
        return Math.max(0, lista.scrollWidth - carousel.clientWidth);
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
});