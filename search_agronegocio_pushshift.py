import requests
import pandas as pd
import unicodedata
from datetime import datetime

def normaliza(texto):
    if texto is None:
        return ""
    return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII').lower()

query = 'agronegócio'
query_norm = normaliza(query)

url = f'https://api.pushshift.io/reddit/search/submission/?q={query_norm}&size=500'
results = []
while url:
    print(f'Buscando: {url}')
    resp = requests.get(url)
    data = resp.json()
    posts = data.get('data', [])
    if not posts:
        break
    for post in posts:
        title = post.get('title', '')
        title_norm = normaliza(title)
        if query_norm in title_norm:
            score = post.get('score', 0)
            created_utc = post.get('created_utc', None)
            date = datetime.utcfromtimestamp(created_utc).strftime('%Y-%m-%d %H:%M:%S') if created_utc else ''
            subreddit = post.get('subreddit', '')
            results.append({'title': title, 'score': score, 'date': date, 'subreddit': subreddit})
    # Paginação: busca pelo último post
    if len(posts) < 500:
        break
    last_created = posts[-1]['created_utc']
    url = f'https://api.pushshift.io/reddit/search/submission/?q={query_norm}&size=500&before={last_created}'

df = pd.DataFrame(results)
print(f"Posts encontrados com '{query}' no título ({len(df)}):")
print(df[['title', 'score', 'date', 'subreddit']])
df[['title', 'score', 'date', 'subreddit']].to_csv('posts_agronegocio_pushshift.csv', index=False, encoding='utf-8')
print("Arquivo 'posts_agronegocio_pushshift.csv' salvo com sucesso.")
