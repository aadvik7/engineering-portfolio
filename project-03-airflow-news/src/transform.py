import re
import string

def strip_html(text):
    if not text:
        return ''
    clean = re.sub(r'<[^>]+>', '', text)
    return clean.strip()

def clean_text(text):
    if not text:
        return ''
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = ' '.join(text.split())
    return text

def parse_article(article):
    return {
        'title': article.get('title', ''),
        'source': article.get('source', {}).get('name', ''),
        'description': strip_html(article.get('description', '')),
        'url': article.get('url', ''),
        'published_at': article.get('publishedAt', ''),
        'content': strip_html(article.get('content', '')),
        'clean_title': clean_text(article.get('title', '')),
        'clean_description': clean_text(article.get('description', ''))
    }

def transform_articles(articles):
    parsed = [parse_article(a) for a in articles if a.get('title')]
    print(f"parsed {len(parsed)} articles")
    return parsed
