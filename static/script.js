const btnHoje = document.getElementById('btnHoje');
const btnAmanha = document.getElementById('btnAmanha');

btnHoje.addEventListener('click', () => {
    const hoje = new Date();
    const hojeFormatado = hoje.toISOString().split('T')[0];
    const inputDataConclusao = document.getElementById('data-conclusao');
    inputDataConclusao.value = hojeFormatado;
});

btnAmanha.addEventListener('click', () => {
    const amanha = new Date();
    amanha.setDate(amanha.getDate() + 1);
    const amanhaFormatado = amanha.toISOString().split('T')[0];
    const inputDataConclusao = document.getElementById('data-conclusao');
    inputDataConclusao.value = amanhaFormatado;
});