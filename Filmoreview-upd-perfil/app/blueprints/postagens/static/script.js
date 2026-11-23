var header = document.getElementById('header');
var opcoesPesquisa = document.getElementById('opcoesPesquisa');

headerAltura = header.offsetHeight;
headerWidth = header.offsetWidth;
opcoesPesquisa.style.marginTop = `calc(${headerAltura}px + 1%)`;
opcoesPesquisa.style.width = `calc(${headerWidth}px)`