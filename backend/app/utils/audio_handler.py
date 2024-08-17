import os


class AudioHandler:
    @staticmethod
    def get_audio_urls():
        audio_directory = "app/media/audios"
        audio_urls = []

        # Get all filenames in the audio directory
        audio_files = [filename for filename in os.listdir(audio_directory) if filename.endswith(".mp3")]

        # Skip the first audio clip
        audio_files_to_skip = audio_files[1:]

        # Create URLs for the remaining audio clips
        for filename in audio_files_to_skip:
            audio_urls.append(f"http://localhost:5000/get-audio/{filename}")

        return audio_urls
