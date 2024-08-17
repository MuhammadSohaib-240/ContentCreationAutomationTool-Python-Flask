from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from app.ml_models.articles_categorizer import ArticleCategorizer


class ArticleScraper:
    def __init__(self):
        self.hollywood_url = "https://www.hollywoodreporter.com/c/movies/"
        self.business_url = "https://www.hollywoodreporter.com/c/business/"
        self.realstate_url = "https://www.hollywoodreporter.com/c/lifestyle/real-estate/"
        self.shopping_url = "https://www.hollywoodreporter.com/c/lifestyle/shopping/"
        self.style_url = "https://www.hollywoodreporter.com/c/lifestyle/style/"
        self.article_categorizer = ArticleCategorizer()
        self.updates = {}
        self.global_index = 0
        self.page_number = 1

    def _initialize_driver(self):
        options = webdriver.FirefoxOptions()
        options.headless = True
        return webdriver.Firefox(options=options)

    def hollywood_updates(self, driver):
        driver.get(self.hollywood_url)
        self._get_updates(driver)

    def business_updates(self, driver):
        driver.get(self.business_url)
        self._get_updates(driver)

    def realstate_updates(self, driver):
        driver.get(self.realstate_url)
        self._get_updates(driver)

    def shopping_updates(self, driver):
        driver.get(self.shopping_url)
        self._get_updates(driver)

    def style_updates(self, driver):
        driver.get(self.style_url)
        self._get_updates(driver)

    def _get_updates(self, driver):
        section = driver.find_element(By.CLASS_NAME, "latest-stories-news-river")
        h3_titles = section.find_elements(By.XPATH, ".//h3[@id='title-of-a-story']")

        for h3_title in h3_titles:
            try:
                self.global_index += 1
                a_element = h3_title.find_element(By.XPATH, ".//a")
                title = a_element.text
                href = a_element.get_attribute("href")
                category = self.article_categorizer.categorize(title)
                self.updates[self.global_index] = {
                    "index": self.global_index,
                    "title": title,
                    "url": href,
                    "category": category
                }

            except NoSuchElementException:
                print(f"{self.global_index}. No <a> element found within the h3")

    def fetch_latest_updates(self):
        try:
            driver = self._initialize_driver()
            self.hollywood_updates(driver)
            self.realstate_updates(driver)
            self.shopping_updates(driver)

            if not self.updates:  # Check if the dictionary is empty
                return []

            return self.updates
        except Exception as e:
            # Handle exceptions if needed
            print(f"Error fetching updates: {e}")
            return []
        finally:
            # Cleanup logic (e.g., calling driver.quit())
            driver.quit()

    def get_current_updates(self):
        if not self.updates:
            return []

        return self.updates

    def fetch_article(self, article_index):
        try:
            self.driver = self._initialize_driver()  # Initialize the driver

            # Fetch the dictionary for the given index
            article_info = self.updates.get(article_index)

            if article_info:
                # Access the "url" field from the dictionary
                article_url = article_info.get("url")

                if article_url:
                    # Call fetch_paragraphs and return the result
                    return self.fetch_paragraphs(article_url)
                else:
                    return "URL not found in the article information."
            else:
                return f"Article information not found for index {article_index}."
        except Exception as e:
            # Handle exceptions if needed
            print(f"Error fetching article: {e}")
            return []
        finally:
            # Ensure that the driver is quit in all cases
            if self.driver:
                self.driver.quit()

    def fetch_paragraphs(self, article_url):
        self.driver.get(article_url)

        # Locate the article tag
        article_tag = self.driver.find_element(By.TAG_NAME, "article")

        # Locate the div with class names "a-content a-content--left-space"
        content_div = article_tag.find_element(By.CLASS_NAME, "a-content.a-content--left-space")

        # Locate all the <p> tags inside the div
        paragraphs = content_div.find_elements(By.TAG_NAME, "p")

        # Return a list of cleaned paragraph texts
        return [self.clean_paragraph_text(paragraph) for paragraph in paragraphs]

    def clean_paragraph_text(self, paragraph):
        # Use WebElement's getText() method to get visible text, excluding child elements
        return paragraph.text
