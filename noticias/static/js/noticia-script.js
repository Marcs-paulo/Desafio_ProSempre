// Alternar o menu de compartilhamento
function toggleShareMenu(button) {
    const dropdown = button.nextElementSibling;
    const allDropdowns = document.querySelectorAll('.share-dropdown');
    
    // fechar outros menus abertos
    allDropdowns.forEach(d => {
        if (d !== dropdown) {
            d.classList.remove('active');
        }
    });
    
    // clicar no botão para abrir/fechar o menu
    dropdown.classList.toggle('active');
}

// fechar o menu de compartilhamento ao clicar fora
document.addEventListener('click', function(event) {
    if (!event.target.closest('.share-wrapper')) {
        const allDropdowns = document.querySelectorAll('.share-dropdown');
        allDropdowns.forEach(dropdown => {
            dropdown.classList.remove('active');
        });
    }
});

// Menu de navegação para mobile
const navToggle = document.getElementById('navToggle');
const navMenu = document.querySelector('.nav-menu');

navToggle.addEventListener('click', () => {
    navMenu.classList.toggle('active');
    navToggle.classList.toggle('active');
});

// funcionalidade dos botões de compartilhamento
document.querySelectorAll('.share-item').forEach(item => {
    item.addEventListener('click', function(e) {
        e.preventDefault();
        
        const shareType = this.textContent.trim();
        const url = window.location.href;
        const title = document.title;
        
        switch(shareType) {
            case 'WhatsApp':
                window.open(`https://wa.me/?text=${encodeURIComponent(title + ' ' + url)}`);
                break;
            case 'X':
                window.open(`https://twitter.com/intent/tweet?text=${encodeURIComponent(title)}&url=${encodeURIComponent(url)}`);
                break;
            case 'Copiar Link':
                navigator.clipboard.writeText(url).then(() => {
                    alert('Link copiado para a área de transferência!');
                });
                break;
            case 'Email':
                window.location.href = `mailto:?subject=${encodeURIComponent(title)}&body=${encodeURIComponent(url)}`;
                break;
            case 'Instagram':
                alert('Por favor, copie o link e compartilhe no Instagram Stories ou Direct.');
                navigator.clipboard.writeText(url);
                break;
        }
    });
});
function toggleShareMenu(btn) {
  const dropdown = btn.nextElementSibling;
  dropdown.classList.toggle('active');
}

// Função para abrir WhatsApp
function shareWhatsApp(event) {
  event.preventDefault();
  const url = window.location.href;
  const text = encodeURIComponent("Olha este post: " + url);
  window.open(`https://wa.me/?text=${text}`, "_blank");
}

// Função para compartilhar no X/Twitter
function shareX(event) {
  event.preventDefault();
  const url = window.location.href;
  const text = encodeURIComponent("Olha este post:");
  window.open(`https://twitter.com/intent/tweet?url=${url}&text=${text}`, "_blank");
}

// Copiar link para a área de transferência
function copyLink(event) {
  event.preventDefault();
  const url = window.location.href;
  navigator.clipboard.writeText(url).then(() => {
    alert("Link copiado para a área de transferência!");
  });
}

// Compartilhar por Email
function shareEmail(event) {
  event.preventDefault();
  const url = window.location.href;
  const subject = encodeURIComponent("Veja este post");
  const body = encodeURIComponent("Olha este post interessante: " + url);
  window.location.href = `mailto:?subject=${subject}&body=${body}`;
}
