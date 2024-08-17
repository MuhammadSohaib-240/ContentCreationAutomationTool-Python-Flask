from flask import Blueprint

from .web_scraping import web_scraping_bp
from .text_to_speech import text_to_speech_bp
from .media import media_bp
from .record_create import record_create_bp

api_bp = Blueprint('api', __name__)

api_bp.register_blueprint(web_scraping_bp, url_prefix='/web_scraping')
api_bp.register_blueprint(text_to_speech_bp, url_prefix='/text_to_speech')
api_bp.register_blueprint(media_bp, url_prefix='/media')
api_bp.register_blueprint(record_create_bp, url_prefix="/record_create")