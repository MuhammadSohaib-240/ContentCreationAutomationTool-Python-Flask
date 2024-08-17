import os
from flask import Blueprint, request, jsonify

from app.utils.audio_handler import AudioHandler
from app.utils.audio_processor import AudioProcessor
from app.utils.file_manager import FileManager
from app.utils.images_handler import ImagesHandler
from app.utils.video_concatenator import VideoConcatenator
from app.utils.video_processor import VideoProcessor


class RecordCreateAPIs:
    def __init__(self):
        self.audio_handler = AudioHandler()
        self.image_handler = ImagesHandler()
        self.audio_processor = AudioProcessor()
        self.video_concatenator = VideoConcatenator()
        self.file_manager = FileManager()

        self.ffmpeg_path = r'C:\ffmpeg\bin\ffmpeg.exe'
        self.media_directory = os.path.join("app", "media")
        self.audio_directory = os.path.join(self.media_directory, "audios")
        self.images_directory = os.path.join(self.media_directory, "images")
        self.video_directory = os.path.join(self.media_directory, "videos")
        self.output_directory = os.path.join(self.media_directory, "edited")

    def get_audio_files(self):
        try:
            audio_urls = self.audio_handler.get_audio_urls()
            return jsonify({"audioUrls": audio_urls}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def get_image_files(self):
        try:
            image_urls = self.image_handler.get_image_urls()
            return jsonify({"imageUrls": image_urls}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def save_image(self, image_data, filename):
        try:
            filename = self.image_handler.save_image(image_data, filename)
            print(f"Image saved successfully at: {filename}")
            return f"Image '{filename}' saved successfully", 200
        except Exception as e:
            print(f"Error processing image: {str(e)}")
            return "Error processing image", 500

    def create_videos(self):
        try:
            print("Service is called")
            VideoProcessor.create_videos(
                self.audio_directory,
                self.images_directory,
                self.video_directory,
                self.ffmpeg_path
            )

            VideoConcatenator.concatenate_videos(
                self.video_directory,
                self.output_directory,
                "edited_video.mp4",
                self.ffmpeg_path
            )

            return jsonify({"message": f"Video edited successfully"})
        except Exception as e:
            return jsonify({"error": str(e)})

    def delete_all_files(self):
        try:
            self.file_manager.delete_all_audio_files()
            self.file_manager.delete_all_image_files()
            self.file_manager.delete_all_video_files()
            self.file_manager.delete_all_edited_files()

            return jsonify({"message ": f"Files deleted successfully"})
        except Exception as e:
            return jsonify({"message ": f"{e}"})

    def delete_images(self):
        try:
            self.file_manager.delete_all_image_files()
            return jsonify({"message ": f"Files deleted successfully"})
        except Exception as e:
            return jsonify({"message ": f"{e}"})

    def delete_videos(self):
        try:
            self.file_manager.delete_all_video_files()
            return jsonify({"message ": f"Files deleted successfully"})
        except Exception as e:
            return jsonify({"message ": f"{e}"})

    def delete_audios(self):
        try:
            self.file_manager.delete_all_audio_files()
            return jsonify({"message ": f"Files deleted successfully"})
        except Exception as e:
            return jsonify({"message ": f"{e}"})


record_create_bp = Blueprint('record_create', __name__)
record_create_apis = RecordCreateAPIs()


@record_create_bp.route("/get-audio-files", methods=['GET'])
def get_audio_files():
    return record_create_apis.get_audio_files()


@record_create_bp.route("/get-image-files", methods=['GET'])
def get_image_files():
    return record_create_apis.get_image_files()


@record_create_bp.route("/edit-video", methods=['POST'])
def edit_video():
    return record_create_apis.create_videos()


@record_create_bp.route("/delete-all-files", methods=['DELETE'])
def delete_all_files():
    return record_create_apis.delete_all_files()


@record_create_bp.route("/delete-images", methods=['DELETE'])
def delete_images():
    return record_create_apis.delete_images()


@record_create_bp.route("/delete-videos", methods=['DELETE'])
def delete_videos():
    return record_create_apis.delete_videos()


@record_create_bp.route("/delete-audios", methods=['DELETE'])
def delete_audios():
    return record_create_apis.delete_audios()


@record_create_bp.route("/add-image", methods=['POST'])
def add_image():
    try:
        image = request.files['image']
        audio_index = request.form['audioIndex']
        image_data = image.read()

        filename = os.path.join("app", "media", "images", f"sentence{audio_index}.png")
        saved_filename = record_create_apis.save_image(image_data, filename)

        return saved_filename
    except Exception as e:
        print(f"Error processing image: {str(e)}")
        return "Error processing image", 500
