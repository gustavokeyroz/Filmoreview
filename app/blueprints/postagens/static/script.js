var header = document.getElementById('header');
var post = document.getElementById('post');

headerAltura = header.offsetHeight;
headerWidth = header.offsetWidth;
post.style.marginTop = `calc(${headerAltura}px + 1%)`;
post.style.width = `calc(${headerWidth}px)`