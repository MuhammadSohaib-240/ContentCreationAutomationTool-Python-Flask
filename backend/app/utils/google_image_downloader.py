import os
import time
import requests
import base64
from selenium import webdriver
from selenium.webdriver.common.by import By

class GoogleImageDownloader:
    def __init__(self):
        self.driver = None

    def __enter__(self):
        self._initialize_driver()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.quit()

    def _initialize_driver(self):
        options = webdriver.FirefoxOptions()
        options.headless = True
        self.driver = webdriver.Firefox(options=options)

    def download_images(self, search_terms, num_images=1, save_directory="images"):
        with self:
            for term_index, term in enumerate(search_terms):
                # Search for the term on Google Images
                self.search_images(term)

                # Get image URLs
                image_urls = self.get_image_urls(num_images)

                # Download and save images
                self.download_and_save_images(term, image_urls, save_directory, term_index)

    def search_images(self, term):
        # Add "1920 x 1080" and "hd" to the search query
        search_url = f"https://www.google.com/search?q={term}&tbm=isch"
        self.driver.get(search_url)
        time.sleep(2)  # Allow time for the images to load

    def get_image_urls(self, num_images):
        image_elements = self.driver.find_elements(By.CSS_SELECTOR, "img.rg_i")

        image_urls = []
        for i in range(min(num_images, len(image_elements))):
            try:
                image_url = image_elements[i].get_attribute("src")
                if image_url:
                    image_urls.append(image_url)
            except Exception as e:
                print(f"Error fetching image URL: {e}")

        return image_urls

    def download_and_save_images(self, term, image_urls, save_directory, term_index):
        term_directory = os.path.join(save_directory, f"sentence_{term_index}")
        os.makedirs(term_directory, exist_ok=True)

        for i, image_url in enumerate(image_urls):
            try:
                if image_url.startswith("data:image"):
                    # Handle base64-encoded images
                    data = image_url.split(',')[1]
                    img_data = base64.b64decode(data)

                    file_extension = "jpg"  # You can adjust the file extension based on the actual format
                    filename = f"sentence_{term_index}.{file_extension}"

                    # Updated path to save images inside the specified directory
                    with open(os.path.join(term_directory, filename), 'wb') as file:
                        file.write(img_data)
                else:
                    # Handle regular image URLs
                    response = requests.get(image_url, stream=True)
                    response.raise_for_status()

                    file_extension = response.headers.get('content-type').split('/')[-1]
                    filename = f"sentence_{term_index}.{file_extension}"

                    # Updated path to save images inside the specified directory
                    with open(os.path.join(term_directory, filename), 'wb') as file:
                        for chunk in response.iter_content(chunk_size=128):
                            file.write(chunk)

                    print(f"Downloaded: {filename}")
            except Exception as e:
                print(f"Error downloading image: {e}")

    def quit(self):
        self.driver.quit()
