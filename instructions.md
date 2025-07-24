# Projeto: Mineração de Texto no Reddit sobre Agronegócio

## Visão Geral

Este projeto realiza mineração de texto no Reddit, focando em posts e comentários que mencionam o termo "agro" ou empresas do setor agropecuário. O objetivo é analisar discussões, tendências e menções ao agronegócio em subreddits brasileiros.

## Principais Funcionalidades

- Busca automatizada de posts e comentários em múltiplos subreddits brasileiros.
- Filtros robustos para acentos e maiúsculas/minúsculas (normalização Unicode).
- Exportação dos resultados para arquivos CSV, incluindo título/comentário, score, data, subreddit e link direto do post/comentário.
- Scripts separados para busca de posts (`search_agronegocio_topbr.py`) e comentários (`search_agronegocio_comments_topbr.py`).
- Possibilidade de expandir a busca para tickers de empresas do agro usando o arquivo `Stocktickers.txt`.

## Como Usar

1. Configure o arquivo `config.py` com suas credenciais do Reddit (client_id, client_secret, username, password, user_agent).
2. Execute os scripts principais:
   - `search_agronegocio_topbr.py`: Busca posts com "agro" nos principais subreddits brasileiros.
   - `search_agronegocio_comments_topbr.py`: Busca comentários com "agro" nos subreddits gerais/populares.
3. Os resultados serão salvos em `posts_agronegocio_topbr.csv` e `comments_agronegocio_topbr.csv`.
4. Para buscar por empresas do agro, adapte os scripts para ler tickers de `Stocktickers.txt` e buscar por eles.
5. Não suba o arquivo `config.py` para o GitHub (adicione ao `.gitignore`).

## Estrutura Recomendada dos CSVs

- Para posts: `title,score,date,subreddit,url`
- Para comentários: `comment,score,date,subreddit,url`

## Expansões Possíveis

- Análise de sentimento dos textos usando NLTK.
- Visualização dos resultados (gráficos, nuvem de palavras).
- Busca por tickers de empresas do agro para análise financeira.
- Integração com outras fontes de dados (notícias, Wikipedia, etc).