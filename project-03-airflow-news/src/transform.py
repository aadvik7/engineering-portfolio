def parse_article(article):
    return {
        'title': article.get('title', ''),
        'source': article.get('source', {}).get('name', ''),
        'description': article.get('description', ''),
        'url': article.get('url', ''),
        'published_at': article.get('publishedAt', ''),
        'content': article.get('content', '')
    }

def transform_articles(articles):
    parsed = [parse_article(a) for a in articles if a.get('title')]
    print(f"parsed {len(parsed)} articles")
    return parsed
