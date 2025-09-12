// Função para alternar menu mobile
function toggleMobileMenu() {
  const nav = document.getElementById("navigation");
  nav.classList.toggle("active");
  // Animar ícone do hambúrguer
  const toggle = document.querySelector(".mobile-menu-toggle");
  toggle.classList.toggle("active");
}

