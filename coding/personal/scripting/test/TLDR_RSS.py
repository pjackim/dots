import requests
from bs4 import BeautifulSoup
from feedgen.feed import FeedGenerator
from datetime import datetime, timezone

class TLDRNewsletterToRSS:

    def __init__(self, url):
        self.url = url

    def fetch_newsletter_content(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return response.text

    def parse_newsletter(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        articles = []

        for article in soup.select('.news'):
            title = article.select_one('.news__title').get_text(strip=True)
            link = article.select_one('.news__link')['href']
            summary = article.select_one('.news__summary').get_text(strip=True)

            articles.append({
                'title': title,
                'link': link,
                'summary': summary
            })

        return articles

    def generate_rss_feed(self, articles):
        fg = FeedGenerator()
        fg.title("TLDR; AI Newsletter")
        fg.link(href=self.url, rel='alternate')
        fg.description("TLDR; AI Newsletter - Daily AI news summaries")
        fg.language('en')
        fg.pubDate(datetime.now(timezone.utc))

        for article in articles:
            fe = fg.add_entry()
            fe.title(article['title'])
            fe.link(href=article['link'])
            fe.description(article['summary'])
            fe.pubDate(datetime.now(timezone.utc))

        return fg.rss_str(pretty=True).decode('utf-8')

    def save_feed_to_file(self, rss_feed, file_name='tldr_ai_newsletter_rss.xml'):
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(rss_feed)

    def convert_newsletter_to_rss(self, output_file='tldr_ai_newsletter_rss.xml'):
        content = self.fetch_newsletter_content()
        articles = self.parse_newsletter(content)
        rss_feed = self.generate_rss_feed(articles)
        self.save_feed_to_file(rss_feed, output_file)



tldr_url = "https://tldr.tech/api/latest/ai"
converter = TLDRNewsletterToRSS(tldr_url)
converter.convert_newsletter_to_rss("tldr_ai_rss_feed.xml")