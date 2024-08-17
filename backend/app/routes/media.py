from flask import Blueprint, request, jsonify
from app.utils.google_image_downloader import GoogleImageDownloader
from app.utils.images_handler import ImagesHandler


class MediaAPIs:
    def __init__(self):
        self.images_downloader = GoogleImageDownloader()
        self.image_handler = ImagesHandler()

    def download_images(self, search_terms):
        self.images_downloader.download_images(search_terms)
        return jsonify({"message": "Images downloaded successfully"})


media_bp = Blueprint('media', __name__)
media_apis = MediaAPIs()


@media_bp.route("/download-images", methods=['POST'])
def download_images():
    json_data = request.get_json()
    search_terms = json_data.get('search_terms', [])
    return media_apis.download_images(search_terms)
