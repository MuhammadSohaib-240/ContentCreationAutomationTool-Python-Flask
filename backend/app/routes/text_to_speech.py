import os
from flask import Blueprint, jsonify, request
from app.utils.audio_processor import AudioProcessor


class TextToSpeechAPIs:
    def __init__(self):
        self.audio_processor = AudioProcessor()
        self.media_directory = os.path.join("app", "media")
        self.audio_directory = os.path.join(self.media_directory, "audios")

    def text_to_speech(self, input_text):
        try:
            sentences = self.audio_processor.split_article_into_sentences(input_text)
            self.audio_processor.create_audio_files(sentences, self.audio_directory, additional_text=input_text)
            return jsonify({"message": "Text-to-Speech Conversion Successful"})
        except Exception as e:
            return jsonify({"error": str(e)})


text_to_speech_bp = Blueprint('text_to_speech', __name__)
text_to_speech_apis = TextToSpeechAPIs()


@text_to_speech_bp.route('/convert', methods=['POST'])
def convert_to_speech():
    print("Endpoint called")
    input_text = request.form.get('text')

    if not input_text:
        return jsonify({"error": "Text parameter is missing"}), 400

    return text_to_speech_apis.text_to_speech(input_text)
