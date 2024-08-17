import os
from flask import Flask, send_from_directory


def create_app():
    app = Flask(__name__, static_folder="media", static_url_path="/")

    # Register the API blueprint
    from .routes import api
    app.register_blueprint(api.api_bp, url_prefix='/api')

    @app.route('/get-image/<path:filename>', methods=['GET'])
    def send_image(filename):
        directory = "images"
        full_path = os.path.normpath(os.path.join(app.static_folder, directory, filename))
        print(full_path)
        return send_from_directory(os.path.join(app.static_folder, directory), filename)

    @app.route('/get-audio/<path:filename>', methods=['GET'])
    def play_audio(filename):
        directory = "audios"
        full_path = os.path.normpath(os.path.join(app.static_folder, directory, filename))
        print(full_path)
        return send_from_directory(os.path.join(app.static_folder, directory), filename, as_attachment=False)

    @app.route('/get-video/<path:filename>', methods=['GET'])
    def play_video(filename):
        directory = "edited"
        full_path = os.path.normpath(os.path.join(app.static_folder, directory, filename))
        print(full_path)
        return send_from_directory(os.path.join(app.static_folder, directory), filename, as_attachment=False,
                                   mimetype='video/mp4')

    return app
