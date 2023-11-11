// selecione o elemento input
const inputCorAlimentos = document.querySelector('#cor-alimentos');

// adicione um ouvinte de eventos para o evento "change"
inputCorAlimentos.addEventListener('change', (event) => {
  // selecione a coluna de alimentos
  const colunaAlimentos = document.querySelectorAll('.coluna-alimentos');

  // defina a cor de fundo da coluna para a cor selecionada pelo usuário
  colunaAlimentos.forEach(coluna => {
    coluna.style.backgroundColor = event.target.value;
  });
});