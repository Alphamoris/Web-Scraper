from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import uuid
import time
from pymongo import MongoClient
import config
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TwitterScraper:
    def __init__(self):
        self.client = MongoClient(config.MONGO_URI)
        self.db = self.client[config.DB_NAME]
        self.collection = self.db[config.COLLECTION_NAME]
        
    def setup_driver(self, proxy=None):
        chrome_options = webdriver.ChromeOptions()
        if proxy:
            chrome_options.add_argument(f'--proxy-server={proxy}')
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        try:
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            return driver
        except Exception as e:
            logger.error(f"Failed to setup driver: {str(e)}")
            raise
    
    def login_to_twitter(self, driver):
        try:
            logger.info("Attempting to login to Twitter...")
            driver.get('https://twitter.com/i/flow/login')
            
            # Wait for username field and enter username
            username_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="username"]'))
            )
            username_input.clear()
            username_input.send_keys(config.TWITTER_USERNAME)
            time.sleep(1)
            
            # Click next button
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@role='button']//span[text()='Next']"))
            )
            next_button.click()
            time.sleep(2)
            
            # Wait for password field and enter password
            password_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="password"]'))
            )
            password_input.clear()
            password_input.send_keys(config.TWITTER_PASSWORD)
            time.sleep(1)
            
            # Click login button
            login_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@role='button']//span[text()='Log in']"))
            )
            login_button.click()
            
            # Wait for login to complete
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="primaryColumn"]'))
            )
            logger.info("Successfully logged in to Twitter")
            return True
            
        except Exception as e:
            logger.error(f"Login failed: {str(e)}")
            return False
    
    def get_trending_topics(self, proxy=None):
        driver = None
        try:
            logger.info("Starting trend scraping process...")
            driver = self.setup_driver(proxy)
            
            if not self.login_to_twitter(driver):
                raise Exception("Failed to login to Twitter")
            
            # Navigate to Twitter Explore/Trending page
            logger.info("Navigating to trending page...")
            driver.get('https://twitter.com/explore/tabs/trending')
            time.sleep(5)  # Wait for page to load completely
            
            # Wait for trending section and get trends
            trends_container = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Timeline: Trending now"])'))
            )
            
            # Get all trend elements
            trends = trends_container.find_elements(By.CSS_SELECTOR, '[data-testid="trend"]')
            
            # Extract top 5 trends
            trending_topics = []
            for trend in trends[:5]:
                try:
                    trend_name = trend.find_element(By.CSS_SELECTOR, '[data-testid="trendName"]').text
                    trending_topics.append(trend_name.strip())
                except Exception as e:
                    logger.warning(f"Failed to extract trend: {str(e)}")
                    continue
            
            if not trending_topics:
                raise Exception("No trends found")
            
            # Store in MongoDB
            record = {
                "_id": str(uuid.uuid4()),
                "timestamp": datetime.now(),
                "ip_address": proxy if proxy else "direct",
                "trend1": trending_topics[0] if len(trending_topics) > 0 else "",
                "trend2": trending_topics[1] if len(trending_topics) > 1 else "",
                "trend3": trending_topics[2] if len(trending_topics) > 2 else "",
                "trend4": trending_topics[3] if len(trending_topics) > 3 else "",
                "trend5": trending_topics[4] if len(trending_topics) > 4 else ""
            }
            
            self.collection.insert_one(record)
            logger.info("Successfully scraped and stored trends")
            return record
            
        except Exception as e:
            logger.error(f"Error scraping trends: {str(e)}")
            return None
        finally:
            if driver:
                driver.quit()
    
    def get_latest_record(self):
        try:
            return self.collection.find_one(sort=[("timestamp", -1)])
        except Exception as e:
            logger.error(f"Error fetching latest record: {str(e)}")
            return None
