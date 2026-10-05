# Portfólio — Natanael Lima

Site estático em HTML, CSS e JavaScript puros (sem frameworks), publicado em `natanaellima.blog` (arquivo `CNAME`) pelo GitHub Pages.

O site existe em três idiomas:

| Idioma | Endereço |
| --- | --- |
| Português | `/` (`index.html`, `projects.html`, `blog.html`) |
| English | `/en/` |
| Español | `/es/` |

O seletor **PT · EN · ES** no topo e no rodapé leva para a mesma página no outro idioma.

## Estrutura

- `index.html`, `projects.html`, `blog.html` e as pastas `en/` e `es/`: páginas **geradas**. Não edite à mão.
- `css/style.css`: todo o visual. Cores e fontes ficam nas variáveis do topo (`:root`).
- `js/main.js`: menu mobile, terminal animado, link ativo, revelação ao rolar, carrossel, formulário de contato, troca de visualização dos projetos e filtro do blog.
- `img/`: imagens em WebP (e os PNG originais). `my-avatar.png` é usada na prévia de compartilhamento (`og:image`).
- `_build/`: gerador das páginas (só ferramentas; não é usado pelo site).
  - `i18n.py`: **todos os textos** nos três idiomas.
  - `gen.py`: monta as páginas a partir dos textos.
  - `sprite.html`: ícones SVG.
- `.nojekyll`: faz o GitHub Pages publicar os arquivos como estão, sem a etapa Jekyll.

## Editar textos ou conteúdo

1. Altere o texto em `_build/i18n.py` (ou a lista de projetos/artigos em `_build/gen.py`).
2. Rode `python3 _build/gen.py` na raiz do repositório.
3. Faça commit das páginas geradas.

- **Novo artigo:** adicione um item em `POSTS` (`gen.py`) e o resumo traduzido em `POST_TX` (`i18n.py`).
- **Novo projeto:** adicione um item em `PROJECTS` (`gen.py`) e os textos em `PROJ` (`i18n.py`).
