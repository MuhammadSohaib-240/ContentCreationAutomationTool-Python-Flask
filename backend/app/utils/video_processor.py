import os
import subprocess


class VideoProcessor:
    @staticmethod
    def create_videos(audio_directory, images_directory, output_directory, ffmpeg_path):
        try:
            print("Video Processor create video method called")

            for i in range(4):
                audio_path = os.path.join(audio_directory, f"sentence{i + 1}.mp3")
                image_path = os.path.join(images_directory, f"sentence{i + 1}.png")
                output_path = os.path.join(output_directory, f"sentence{i + 1}.mp4")

                custom_command = (
                    f"{ffmpeg_path} -loop 1 -i {image_path} -i {audio_path} "
                    "-c:v libx264 -tune stillimage -c:a aac -b:a 192k "
                    '-vf "scale=\'iw-mod(iw,2)\':\'ih-mod(ih,2)\',format=yuv420p" '
                    f"-shortest -movflags +faststart {output_path}"
                )

                subprocess.call(custom_command, shell=True)
        except Exception as e:
            print("Error:", e)
