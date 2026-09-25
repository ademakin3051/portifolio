# Portfólio — Natanael Lima

Site estático em HTML, CSS e JavaScript puros (sem frameworks). Publicado em `natanaellima.blog` (arquivo `CNAME`).

## Estrutura

- `index.html`: home (hero, sobre, skills, experiência, projetos, recomendações e contato)
- `projects.html`: case studies, próximos projetos e estatísticas
- `blog.html`: artigo em destaque, arquivo com filtro por categoria e tópicos
- `css/style.css`: todo o visual. As cores e fontes ficam nas variáveis do topo (`:root`)
- `js/main.js`: menu mobile, terminal animado, link ativo, revelação ao rolar, troca de visualização dos projetos e filtro do blog
- `img/`: imagens em WebP. `my-avatar.png` é usada na prévia de compartilhamento (og:image)
- `favicon.svg`

## Editar conteúdo

- **Novo artigo:** copie um bloco `<a class="post" ...>` em `blog.html`. O valor de `data-cat` precisa ser igual ao de um botão de filtro.
- **Novo projeto:** copie um bloco `<article class="case">` em `projects.html` e uma linha `<a class="proj-row">` em `index.html`.
- **Ícones:** SVG embutidos no topo de cada página, usados com `<use href="#i-nome">`.
