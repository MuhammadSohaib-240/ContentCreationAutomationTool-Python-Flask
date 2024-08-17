import os
import subprocess
from glob import glob


class VideoConcatenator:
    @staticmethod
    def concatenate_videos(video_directory, output_directory, output_filename, ffmpeg_path):
        # List all video files in the directory
        video_files = sorted(glob(os.path.join(video_directory, "*.mp4")))

        if not video_files:
            print("No video files found for concatenation.")
            return

        # Create a temporary text file with the list of input files
        temp_file_path = os.path.join(video_directory, "input_list.txt")
        with open(temp_file_path, 'w') as temp_file:
            for file in video_files:
                # Make the path relative to video_directory
                relative_path = os.path.relpath(file, video_directory)
                temp_file.write(f"file '{relative_path}'\n")

        # Construct the video concatenation command with a fixed resolution (e.g., 1920x1080)
        output_path = os.path.join(output_directory, output_filename)
        video_concatenation_command = [
            ffmpeg_path,
            '-f', 'concat',
            '-safe', '0',
            '-i', f'{temp_file_path}',
            '-vf', 'scale=1920:1080',  # Set the desired resolution (e.g., 1920x1080)
            '-c:v', 'libx264',
            '-pix_fmt', 'yuv420p',
            '-c:a', 'aac',
            '-strict', 'experimental',
            output_path
        ]

        subprocess.run(video_concatenation_command)

        # Remove the temporary input file
        os.remove(temp_file_path)

        return output_path
