const nome = document.getElementById('nome');
const preco = document.getElementById('preco');
const detalhes = document.getElementById('detalhes');
const fundo = document.getElementById('fundo');

function verDetalhes(nome, preco) {
    document.getElementById("nome").innerText = nome;
    document.getElementById("preco").innerText = preco;
    detalhes.style.display = "block";
    fundo.style.display = "block";
}
function fecharDetalhes() {
    document.getElementById("detalhes").style.display = "none";
    fundo.style.display = "none";
}