import praw
import os
from dotenv import load_dotenv
import pandas as pd
import unicodedata

load_dotenv()

# Lista dos 20 maiores subreddits brasileiros (pode ser ajustada conforme ranking atual)
subreddits = [
    # Gerais e populares
    'brasil', 'brasilivre', 'conversas', 'desabafos', 'perguntereddit', 'botecodoreddit',
    'memesbr', 'diretodozapzap', 'eu_nvr', 'famil', 'investimentos',
    # Norte
    'acre', 'riobranco', 'amapa', 'macapa', 'amazonas', 'manaus', 'para', 'belem', 'rondonia', 'portovelho', 'roraima', 'boavista', 'tocantins', 'palmas',
    # Nordeste
    'alagoas', 'maceio', 'bahia', 'salvador', 'ceara', 'fortaleza', 'maranhao', 'saoluis', 'paraiba', 'joaopessoa', 'pernambuco', 'recife', 'piaui', 'teresina', 'riograndedonorte', 'natal', 'sergipe', 'aracaju',
    # Centro-Oeste
    'distritofederal', 'brasilia', 'goias', 'goiania', 'matogrosso', 'cuiaba', 'matogrossodosul', 'campogrande',
    # Sudeste
    'espiritosanto', 'vitoria', 'minasgerais', 'belohorizonte', 'riodejaneiro', 'saopaulo',
    # Sul
    'parana', 'curitiba', 'riograndedosul', 'portoalegre', 'santacatarina', 'florianopolis'
]

reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    username=os.getenv('REDDIT_USERNAME'),
    password=os.getenv('REDDIT_PASSWORD'),
    redirect_uri="http://localhost:8080",
    user_agent=os.getenv('REDDIT_USER_AGENT')
)

def normaliza(texto):
    if texto is None:
        return ""
    return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII').lower()


queries = ['agro']
results = []
for sub in subreddits:
    print(f'Buscando em r/{sub}...')
    for q in queries:
        q_norm = normaliza(q)
        for submission in reddit.subreddit(sub).search(q, sort='new', limit=None):
            title_norm = normaliza(submission.title)
            # Garante que o termo buscado está no título normalizado
            if q_norm in title_norm:
                post_date = pd.to_datetime(submission.created_utc, unit='s').strftime('%Y-%m-%d %H:%M:%S')
                results.append({
                    'title': submission.title,
                    'score': submission.score,
                    'date': post_date,
                    'subreddit': sub,
                    'url': f"https://reddit.com{submission.permalink}"
                })

df = pd.DataFrame(results)
print(f"Posts encontrados com {queries} nos maiores subreddits brasileiros ({len(df)}):")
print(df[['title', 'score', 'date', 'subreddit', 'url']])
df[['title', 'score', 'date', 'subreddit', 'url']].to_csv('posts_agronegocio_topbr.csv', index=False, encoding='utf-8')
print("Arquivo 'posts_agronegocio_topbr.csv' salvo com sucesso com links dos posts.")
