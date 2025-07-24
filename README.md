# 🚜 Mineração de Texto no Reddit sobre Agronegócio

Projeto para coletar e analisar posts e comentários sobre "agro" em subreddits brasileiros.

## Funcionalidades

- Busca automatizada de posts e comentários em diversos subreddits do Brasil
- Filtro inteligente para acentos e maiúsculas/minúsculas
- Exportação dos resultados para CSV com título/comentário, score, data, subreddit e link
- Scripts separados para posts e comentários
- Expansão opcional para buscar empresas do agro via tickers (`Stocktickers.txt`)

## Como Usar

1. Configure o arquivo `config.py` com suas credenciais do Reddit
2. Execute os scripts principais:
   - `search_agronegocio_topbr.py` (posts)
   - `search_agronegocio_comments_topbr.py` (comentários)
3. Resultados em `posts_agronegocio_topbr.csv` e `comments_agronegocio_topbr.csv`
4. Para buscar empresas do agro, adapte para usar os tickers do arquivo `Stocktickers.txt`
5. Adicione `config.py` ao `.gitignore` para não subir suas credenciais

## Estrutura dos CSVs

- **Posts:** `title,score,date,subreddit,url`
- **Comentários:** `comment,score,date,subreddit,url`

## Possíveis Expansões

- Análise de sentimento (NLTK)
- Visualizações (gráficos, nuvem de palavras)
- Busca por empresas do agro
- Integração com outras fontes de dados

---

Feito para facilitar pesquisas e análises sobre o agronegócio no Reddit brasileiro.
