import os

import cv2
import numpy as np


class ImagesHandler:
    def save_image(self, image_data, filename):
        image_path = os.path.join(filename)

        os.makedirs(os.path.dirname(image_path), exist_ok=True)
        image_np = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR)
        enhanced_image = self.enhance_color_and_brightness(image_np)

        cv2.imwrite(image_path, enhanced_image, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
        print(f"Image '{filename}' saved successfully at: {image_path}")
        return filename

    @staticmethod
    def enhance_color_and_brightness(image):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        hsv[:, :, 1] = np.clip(hsv[:, :, 1] * 1.2, 0, 255)  # Increase saturation
        hsv[:, :, 2] = np.clip(hsv[:, :, 2] * 1.3, 0, 255)  # Increase brightness

        enhanced_image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        return enhanced_image

    @staticmethod
    def get_image_urls():
        image_directory = "app/media/images"
        image_urls = []

        for filename in os.listdir(image_directory):
            if filename.lower().endswith(".png"):
                image_urls.append(f"http://localhost:5000/get-image/{filename}")

        return image_urls
