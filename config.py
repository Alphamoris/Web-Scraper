import os
from dotenv import load_dotenv

load_dotenv()

# MongoDB Configuration
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
DB_NAME = 'twitter_trends'
COLLECTION_NAME = 'trends'

# Twitter Credentials
TWITTER_USERNAME = os.getenv('TWITTER_USERNAME')
TWITTER_PASSWORD = os.getenv('TWITTER_PASSWORD')

# ProxyMesh Configuration
PROXYMESH_USERNAME = os.getenv('PROXYMESH_USERNAME')
PROXYMESH_PASSWORD = os.getenv('PROXYMESH_PASSWORD')
PROXYMESH_HOST = 'us-wa.proxymesh.com:31280'  # Example proxy endpoint
