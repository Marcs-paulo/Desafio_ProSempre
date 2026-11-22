# Desafio ProSempre

Site institucional feito em **Django** como desafio técnico: página inicial com planos, benefícios e avaliações de clientes, um **blog** com filtro por categoria, uma página de **notícias** e a página **Sobre nós** com a equipe. Todo o conteúdo (textos, planos, posts, fotos, contatos) é editado pelo painel de administração do Django, sem mexer no código.

## Tecnologias

- Python e Django 5.2
- SQLite
- HTML, CSS e JavaScript nos templates
- Pillow (imagens dos posts e da equipe) e django-phonenumber-field (telefone de contato)

## Estrutura

| Pasta | O que tem |
| :-- | :-- |
| `setup/` | configurações e rotas do projeto |
| `pagina/` | página inicial, planos, avaliações e configurações do site |
| `blog/` | posts do blog, com categorias e foto do autor |
| `noticias/` | página de leitura de uma notícia, com outras notícias ao lado |
| `sobre/` | página Sobre nós, com história e equipe |
| `media/` | imagens enviadas pelo painel |

## Como rodar

```bash
python -m venv .venv
source .venv/bin/activate        # no Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Abra http://localhost:8000. O painel fica em http://localhost:8000/admin; para criar um usuário de acesso:

```bash
python manage.py createsuperuser
```

A página `/noticias/` mostra um post do blog sorteado, então ela precisa de pelo menos um post cadastrado.
