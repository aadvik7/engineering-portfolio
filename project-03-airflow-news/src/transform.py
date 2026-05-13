import re

def strip_html(text):
    if not text:
        return ''
    clean = re.sub(r'<[^>]+>', '', text)
    return clean.strip()

def parse_article(article):
    return {
        'title': article.get('title', ''),
        'source': article.get('source', {}).get('name', ''),
        'description': strip_html(article.get('description', '')),
        'url': article.get('url', ''),
        'published_at': article.get('publishedAt', ''),
        'content': strip_html(article.get('content', ''))
    }

def transform_articles(articles):
    parsed = [parse_article(a) for a in articles if a.get('title')]
    print(f"parsed {len(parsed)} articles")
    return parsed
