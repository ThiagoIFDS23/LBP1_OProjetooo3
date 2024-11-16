const botaoAbrir1 = document.getElementById('botaoAbrir1');
const botaoAbrir2 = document.getElementById('botaoAbrir2');
const botaoAbrir3 = document.getElementById('botaoAbrir3');
const botaoFechar1 = document.getElementById('botaoFechar1');
const botaoFechar2 = document.getElementById('botaoFechar2');
const botaoFechar3 = document.getElementById('botaoFechar3');
const detalhes = document.getElementById('detalhes');

botaoAbrir1.addEventListener('click', () => {
    detalhes.style.display = 'block';
});

botaoAbrir2.addEventListener('click', () => {
    detalhes.style.display = 'block';
});

botaoAbrir3.addEventListener('click', () => {
    detalhes.style.display = 'block';
});

botaoFechar1.addEventListener('click', () => {
    detalhes.style.display = 'none';
});

botaoFechar2.addEventListener('click', () => {
    detalhes.style.display = 'none';
});

botaoFechar3.addEventListener('click', () => {
    detalhes.style.display = 'none';
});