# 🌟 Twitter Trends Scraper

A powerful and elegant solution for real-time Twitter trends monitoring with proxy support and MongoDB integration.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.15.2-green)
![MongoDB](https://img.shields.io/badge/MongoDB-Latest-brightgreen)
![Flask](https://img.shields.io/badge/Flask-3.0.0-lightgrey)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🚀 Features

- 🔍 **Real-time Trend Scraping**: Automatically fetches top 5 trending topics from Twitter
- 🔄 **Proxy Integration**: Uses ProxyMesh for IP rotation and anonymity
- 💾 **MongoDB Storage**: Persistent storage with unique IDs for each scraping session
- 🌐 **Web Interface**: Clean and responsive UI for viewing trends
- 📊 **JSON Export**: Easy data export in JSON format
- 🛡️ **Error Handling**: Robust error handling and logging
- 🔒 **Security**: Environment-based configuration for sensitive data

## 🛠️ Technology Stack

- **Backend**: Python, Flask
- **Web Automation**: Selenium WebDriver
- **Database**: MongoDB
- **Frontend**: HTML5, CSS3, JavaScript
- **Proxy Service**: ProxyMesh
- **Package Management**: pip

## 📋 Prerequisites

Before running the application, ensure you have:

- Python 3.8 or higher
- MongoDB installed and running
- A Twitter account
- ProxyMesh account credentials
- Chrome browser installed

## ⚡ Quick Start

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/twitter-trends-scraper.git
   cd twitter-trends-scraper
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env with your credentials
   nano .env
   ```

4. **Set Up Environment Variables**
   ```env
   # MongoDB Configuration
   MONGO_URI=mongodb://localhost:27017/

   # Twitter Credentials
   TWITTER_USERNAME=your_twitter_username
   TWITTER_PASSWORD=your_twitter_password

   # ProxyMesh Configuration
   PROXYMESH_USERNAME=your_proxymesh_username
   PROXYMESH_PASSWORD=your_proxymesh_password
   ```

5. **Run the Application**
   ```bash
   python app.py
   ```

6. **Access the Web Interface**
   - Open your browser and navigate to `http://localhost:5000`
   - Click the "Run Script" button to start scraping trends

## 🎯 Usage

1. **Web Interface**
   - Navigate to the homepage
   - Click "Run Script" to fetch current trends
   - View trends, IP address used, and JSON data
   - Refresh for new trends

2. **MongoDB Data**
   ```javascript
   // Example document structure
   {
     "_id": "unique_uuid",
     "timestamp": ISODate("2024-12-25T17:08:30.123Z"),
     "ip_address": "xxx.xxx.xxx.xxx",
     "trend1": "First Trending Topic",
     "trend2": "Second Trending Topic",
     "trend3": "Third Trending Topic",
     "trend4": "Fourth Trending Topic",
     "trend5": "Fifth Trending Topic"
   }
   ```

## 🔧 Configuration Options

### Selenium Options
- Headless mode (enabled by default)
- Custom Chrome options
- Proxy configuration
- Anti-detection measures

### MongoDB Settings
- Custom database name
- Collection configuration
- Index optimization

### Proxy Settings
- ProxyMesh endpoint selection
- IP rotation strategy
- Connection timeout settings

## 📝 Logging

The application includes comprehensive logging:
- Scraping process details
- MongoDB operations
- Error tracking
- Performance metrics

Logs are available in the console and can be configured for file output.

## 🛡️ Security Features

- Environment-based credential management
- Secure proxy handling
- MongoDB authentication
- Error message sanitization
- Cross-Origin Resource Sharing (CORS) protection

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Twitter for providing trending topics
- ProxyMesh for proxy services
- MongoDB for database solutions
- Selenium for web automation
- Flask for web framework

## 📞 Support

For support, please:
- Open an issue in the GitHub repository
- Contact the maintainers
- Check the documentation

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/twitter-trends-scraper&type=Date)](https://star-history.com/#yourusername/twitter-trends-scraper&Date)

---
Made with ❤️ by [Your Name]
#   W e b - S c r a p e r  
 