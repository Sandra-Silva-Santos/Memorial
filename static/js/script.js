document.addEventListener('DOMContentLoaded', function() {
  var botaoNovaPesquisa = document.getElementById('nova_pesquisa');
  
  if (botaoNovaPesquisa) {
    botaoNovaPesquisa.addEventListener('click', function() {
      document.getElementById('search').value = '';
      document.getElementById('data_falecimento').value = '';
      document.getElementById('data_sepultamento').value = '';
    });
  }
});