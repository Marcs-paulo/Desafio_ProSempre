// Funcionalidade do carrossel
let currentSlide = 0;

function moveCarousel(direction) {
  const track = document.querySelector(".carousel-track");
  const cards = document.querySelectorAll(".featured-card");
  const cardWidth = cards[0].offsetWidth + 30;

  currentSlide += direction;

  // Determinar quantos cards são visíveis com base na largura da tela
  let visibleCards = 3;
  if (window.innerWidth <= 968) visibleCards = 2;
  if (window.innerWidth <= 768) visibleCards = 1;

  const maxSlide = cards.length - visibleCards;

  if (currentSlide < 0) currentSlide = 0;
  if (currentSlide > maxSlide) currentSlide = maxSlide;

  track.style.transform = `translateX(-${currentSlide * cardWidth}px)`;
}

// Funcionalidade de dropdown (abrir/fechar)
function toggleDropdown(type) {
  const dropdownId = type === "filter" ? "filter-dropdown" : "sort-dropdown";
  const dropdown = document.getElementById(dropdownId);
  const otherDropdownId =
    type === "filter" ? "sort-dropdown" : "filter-dropdown";
  const otherDropdown = document.getElementById(otherDropdownId);

  // Fechar outro dropdown
  otherDropdown.classList.remove("active");

  // Atualizar estado do dropdown atual
  dropdown.classList.toggle("active");
}

// Fechar dropdowns ao clicar fora
document.addEventListener("click", function (event) {
  if (!event.target.closest(".dropdown-wrapper")) {
    document.querySelectorAll(".dropdown-menu").forEach((menu) => {
      menu.classList.remove("active");
    });
  }
});

// Funcionalidade de filtro
document.querySelectorAll("#filter-dropdown input").forEach((checkbox) => {
  checkbox.addEventListener("change", function () {
    console.log("Filtro alterado:", this.value, this.checked);
  });
});

// Funcionalidade de ordenação
document.querySelectorAll("#sort-dropdown input").forEach((radio) => {
  radio.addEventListener("change", function () {
    // Implementar lógica de ordenação aqui
    console.log("Ordenação alterada:", this.value);
  });
});

// Pagination functionality
document.querySelectorAll(".page-btn").forEach((btn) => {
  btn.addEventListener("click", function () {
    if (!this.classList.contains("page-dots")) {
      document.querySelector(".page-btn.active").classList.remove("active");
      this.classList.add("active");
      // Implement page change logic here
    }
  });
});

// Seleciona o elemento do modal no DOM
const modal = document.getElementById("blogModal");

// Função para abrir o modal e preencher com os dados do post
function openModal(postData) {
  if (!modal) return; // Garante que o modal exista

  // Preenche os elementos do modal com os dados do objeto 'postData'
  modal.querySelector("#modalImage").src = postData.image;
  modal.querySelector("#modalImage").alt = postData.title;
  modal.querySelector("#modalTitle").textContent = postData.title;
  modal.querySelector("#modalBody").textContent = postData.content;

  // Define a tag/categoria com a classe correta
  const tagElement = modal.querySelector("#modalTag");
  tagElement.textContent = postData.tag;

  // Remove todas as classes de tag existentes e adiciona a correta
  tagElement.className = "category-tag";
  const tagClass = getTagClass(postData.tag);
  if (tagClass) {
    tagElement.classList.add(tagClass);
  }

  // define autor e data
  modal.querySelector("#modalAuthor").textContent = postData.author;
  modal.querySelector("#modalDate").textContent = postData.date;

  // define o link para a página completa
  const linkElement = modal.querySelector("#modalLink");
  linkElement.href = postData.link;

  // exibe o modal
  modal.classList.add("active");
  document.body.classList.add("modal-open"); // Trava o scroll da página
}

// função auxiliar para determinar a classe CSS da tag
function getTagClass(tagName) {
  const tagClasses = {
    Resenha: "tag-resenha",
    "Dica de Leitura": "tag-dicas",
    Lançamentos: "tag-lancamentos",
    Notícia: "tag-noticia",
    Clássicos: "tag-classicos",
  };
  return tagClasses[tagName] || "";
}

// Função para fechar o modal
function closeModal() {
  if (!modal) return;

  modal.classList.remove("active");
  document.body.classList.remove("modal-open"); // Libera o scroll da página
}

// Evento para fechar o modal clicando fora do conteúdo
modal.addEventListener("click", (event) => {
  // Se o clique foi no fundo (lá ele) e não no conteúdo, fecha o modal
  if (event.target === modal) {
    closeModal();
  }
});

// Evento para fechar o modal com a tecla ESC
document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && modal.classList.contains("active")) {
    closeModal();
  }
});
