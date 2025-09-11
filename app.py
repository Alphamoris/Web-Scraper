

from flask import Flask, render_template, jsonify
from scraper import TwitterScraper
import json
from bson import json_util
import config
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
scraper = TwitterScraper()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape_trends():
    try:
        logger.info("Starting scraping process...")
        
        # Get a proxy from ProxyMesh
        proxy = f"http://{config.PROXYMESH_USERNAME}:{config.PROXYMESH_PASSWORD}@{config.PROXYMESH_HOST}"
        
        # Run the scraper
        result = scraper.get_trending_topics(proxy)
        
        if not result:
            logger.error("Scraper returned no results")
            return jsonify({"error": "Failed to scrape trends"}), 500
        
        # Convert MongoDB document to JSON
        json_result = json.loads(json_util.dumps(result))
        logger.info("Successfully retrieved trends")
        return json_result
        
    except Exception as e:
        logger.error(f"Error in /scrape endpoint: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Verify MongoDB connection on startup
    try:
        scraper.client.server_info()
        logger.info("Successfully connected to MongoDB")
    except Exception as e:
        logger.error(f"Failed to connect to MongoDB: {str(e)}")
        
    app.run(debug=True)
