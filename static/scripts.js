var links = document.querySelectorAll('.meuLink');

// Itera sobre os links e adiciona o evento de clique
links.forEach(function(link) {
  link.addEventListener('click', function() {
    // Remove a classe "ativo" de todos os links
    links.forEach(function(link) {
      link.classList.remove('ativo');
    });

    // Adiciona a classe "ativo" ao link clicado
    this.classList.add('ativo');
  });
});