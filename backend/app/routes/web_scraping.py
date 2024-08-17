from flask import Blueprint, request, jsonify
from app.utils.article_scrapper import ArticleScraper


class WebScrapingAPIs:
    def __init__(self):
        self.article_scrapper = ArticleScraper()

    def fetch_latest_updates(self):
        updates = self.article_scrapper.fetch_latest_updates()
        print(updates)
        return jsonify({"updates": updates})

    def get_current_updates(self):
        updates = self.article_scrapper.get_current_updates()
        return jsonify({"updates": updates})

    def generate_article(self, article_index):
        article = self.article_scrapper.fetch_article(article_index)
        return jsonify({"article": article})


web_scraping_bp = Blueprint('web_scraping', __name__)
web_scraping_apis = WebScrapingAPIs()


@web_scraping_bp.route('/scrape', methods=['GET'])
def scrape():
    return web_scraping_apis.fetch_latest_updates()


@web_scraping_bp.route('/get-current-updates', methods=['GET'])
def get_current_updates():
    return web_scraping_apis.get_current_updates()


@web_scraping_bp.route("/generate-article", methods=['POST'])
def generate_article():
    article_index = int(request.form.get('article_index'))
    return web_scraping_apis.generate_article(article_index)
