// DADOS DA EQUIPE
const teamData = [
    {
        name: "Ana Oliveira",
        role: "Curadora Chefe de Conteúdo",
        image: "Images/ana.png", 
        bio: "Vestibulum vitae iaculis nulla, at finibus sem. Cras sagittis mauris id  ante euismod tempus. Nam in lectus lorem. Aliquam mollis nisl neque, id  dictum dui imperdiet sed. Nulla tincidunt, odio sit amet mattis commodo, felis nulla feugiat leorio. Fusce  congue vehicula ex a suscipit. Cras a mi elementum, pulvinar velit vel,  congue nulla. Pellentesque consequat sem vitae pretium laoreet.  Suspendisse sodales euismod elit molestie finibus. Aliquam erat volutpat. Integer ultrices eros sit amet nunc commodo  commodo. Donec  pulvinar nibh vitae ipsum eleifend condimentum."
    },
    {
        name: "Alberto de Magalhões",
        role: "CEO ",
        image: "Images/betinho.png", 
        bio: "Vestibulum vitae iaculis nulla, at finibus sem. Cras sagittis mauris id  ante euismod tempus. Nam in lectus lorem. Aliquam mollis nisl neque, id  dictum dui imperdiet sed. Nulla tincidunt, odio sit amet mattis commodo, felis nulla feugiat leorio. Fusce  congue vehicula ex a suscipit. Cras a mi elementum, pulvinar velit vel,  congue nulla. Pellentesque consequat sem vitae pretium laoreet.  Suspendisse sodales euismod elit molestie finibus. Aliquam erat volutpat. Integer ultrices eros sit amet nunc commodo  commodo. Donec  pulvinar nibh vitae ipsum eleifend condimentum."
    },
    {
        name: "Marina Santos",
        role: "Editora de Ficção Científica",
        image: "Images/img1-blog.jpg", 
        bio: "Vestibulum vitae iaculis nulla, at finibus sem. Cras sagittis mauris id  ante euismod tempus. Nam in lectus lorem. Aliquam mollis nisl neque, id  dictum dui imperdiet sed. Nulla tincidunt, odio sit amet mattis commodo, felis nulla feugiat leorio. Fusce  congue vehicula ex a suscipit. Cras a mi elementum, pulvinar velit vel,  congue nulla. Pellentesque consequat sem vitae pretium laoreet.  Suspendisse sodales euismod elit molestie finibus. Aliquam erat volutpat. Integer ultrices eros sit amet nunc commodo  commodo. Donec  pulvinar nibh vitae ipsum eleifend condimentum."
    },
    {
        name: "João Pereira",
        role: "Gerente de Comunidade",
        image: "Images/joao.jpg",
        bio: "Vestibulum vitae iaculis nulla, at finibus sem. Cras sagittis mauris id  ante euismod tempus. Nam in lectus lorem. Aliquam mollis nisl neque, id  dictum dui imperdiet sed. Nulla tincidunt, odio sit amet mattis commodo, felis nulla feugiat leorio. Fusce  congue vehicula ex a suscipit. Cras a mi elementum, pulvinar velit vel,  congue nulla. Pellentesque consequat sem vitae pretium laoreet.  Suspendisse sodales euismod elit molestie finibus. Aliquam erat volutpat. Integer ultrices eros sit amet nunc commodo  commodo. Donec  pulvinar nibh vitae ipsum eleifend condimentum."
    }
];
function closeTeamModal(index) {
    const modal = document.getElementById(`teamModal${index}`);
    modal.style.display = 'none';
}

// LÓGICA DO CARROSSEL DA EQUIPE
const teamTrack = document.querySelector('.team-track');
const teamCards = document.querySelectorAll('.team-card');
let currentSlide = 0;

// Função para calcular quantos cards exibir com base na tela
function getCardsPerView() {
    if (window.innerWidth < 768) return 1;
    if (window.innerWidth < 1200) return 2;
    return 3;
}

function moveCarousel(direction) {
    if (!teamTrack || teamCards.length === 0) return; // Evita erros se os elementos não existirem

    const cardsPerView = getCardsPerView();
    const maxSlide = teamCards.length - cardsPerView;
    
    currentSlide += direction;
    
    if (currentSlide < 0) {
        currentSlide = 0;
    } else if (currentSlide > maxSlide) {
        currentSlide = maxSlide;
    }
    
    // O cálculo baseado no tamanho real do card e no gap do CSS
    const cardWidth = teamCards[0].offsetWidth;
    const gap = parseInt(window.getComputedStyle(teamTrack).gap) || 30;
    const translateX = currentSlide * -(cardWidth + gap);
    
    teamTrack.style.transform = `translateX(${translateX}px)`;
}

//LÓGICA DO MODAL DA EQUIPE
function openTeamModal(index) {
    const modal = document.getElementById('teamModal');
    if (!modal) return;

    // Preenche o modal com os dados do membro da equipe selecionado
    modal.querySelector('#modalImage').src = teamData[index].image;
    modal.querySelector('#modalImage').alt = `Foto de ${teamData[index].name}`;
    modal.querySelector('#modalName').textContent = teamData[index].name;
    modal.querySelector('#modalRole').textContent = teamData[index].role;
    modal.querySelector('#modalBio').textContent = teamData[index].bio;
    
    // Exibe o modal
    modal.classList.add('active'); 
    document.body.classList.add('modal-open');
}

function closeTeamModal() {
    const modal = document.getElementById('teamModal');
    if (!modal) return;

    modal.classList.remove('active');
    document.body.classList.remove('modal-open');
}

// Event listener para fechar o modal com a tecla ESC
document.addEventListener('keydown', (e) => {
    const modal = document.getElementById('teamModal');
    if (e.key === 'Escape' && modal && modal.classList.contains('active')) {
        closeTeamModal();
    }
});

// O carrossel se ajusta ao redimensionar a janela
window.addEventListener('resize', () => {
    if (teamTrack) {
        currentSlide = 0;
        teamTrack.style.transform = 'translateX(0)';
    }
});