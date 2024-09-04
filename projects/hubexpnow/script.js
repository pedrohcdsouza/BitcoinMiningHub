// Função para salvar os dados do cliente no LocalStorage e redirecionar para a página do cliente
document.getElementById('formRegistro').addEventListener('submit', function (e) {
    e.preventDefault();

    const nome = document.getElementById('nome').value;
    const email = document.getElementById('email').value;

    const cliente = {
        nome: nome,
        email: email
    };

    // Salvar cliente no LocalStorage
    localStorage.setItem('clienteAtual', JSON.stringify(cliente));

    // Redirecionar para a página do cliente
    window.location.href = 'cliente.html';
});

// Carregar os dados do cliente na página cliente.html
document.addEventListener('DOMContentLoaded', function () {
    if (window.location.pathname.includes('cliente.html')) {
        const cliente = JSON.parse(localStorage.getItem('clienteAtual'));
        console.log(cliente); // Adicione este console.log para depurar

        if (cliente) {
            document.getElementById('clienteNome').innerText = cliente.nome;
            document.getElementById('clienteEmail').innerText = cliente.email;
        }
    }
});
