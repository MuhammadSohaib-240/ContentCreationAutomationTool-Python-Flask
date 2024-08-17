import os


class FileManager:
    @staticmethod
    def delete_all_files_in_directory(directory):
        try:
            for file_name in os.listdir(directory):
                file_path = os.path.join(directory, file_name)
                if os.path.isfile(file_path):
                    os.remove(file_path)
            print(f"All files in {directory} deleted successfully.")
        except Exception as e:
            print(f"Error deleting files in {directory}: {e}")

    @staticmethod
    def delete_all_video_files():
        FileManager.delete_all_files_in_directory("app/media/videos")

    @staticmethod
    def delete_all_audio_files():
        FileManager.delete_all_files_in_directory("app/media/audios")

    @staticmethod
    def delete_all_image_files():
        FileManager.delete_all_files_in_directory("app/media/images")

    @staticmethod
    def delete_all_edited_files():
        FileManager.delete_all_files_in_directory("app/media/edited")
