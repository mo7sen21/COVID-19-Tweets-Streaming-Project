Overview
This project streams and filters tweets related to COVID-19 symptoms, treatments, and pandemic-related keywords using Twitter's API (now X's API). The code collects tweets matching predefined filters (e.g., symptoms like "dry cough" or hashtags like #COVID19) and saves them to a JSON file while excluding retweets and replies.

Note: This code was designed for Twitter API v1.1 rules circa 2021. Since Twitter’s API has undergone significant changes (including migration to X and updates under Elon Musk’s leadership), some components may require adjustments to align with current documentation.

Prerequisites
Python 3.6+

Libraries: tweepy, pandas, numpy, matplotlib, seaborn, requests

Twitter Developer Account with API credentials:

API Key

API Secret Key

Bearer Token

Access Token

Access Secret

Setup
Install Dependencies:

bash
pip install tweepy pandas numpy matplotlib seaborn requests
Replace Credentials:
Update the placeholder credentials in the code:

python
api_key = 'your_api_key_here'
api_secret_key = 'your_api_secret_here'
bearer_token = 'your_bearer_token_here'
access_token = 'your_access_token_here'
access_secret = 'your_access_secret_here'
Convert to Python Script (Optional):
To run as a .py file instead of a Jupyter notebook:

bash
jupyter nbconvert --to script Copy_of_covid_tweets_tracing.ipynb
Adjust print statements and async logic if needed.

Usage
Configure Filters:
Modify keywords, keywords_2, and hashtags lists to adjust tracked terms.
Example:

python
keywords = ['I have high fever', 'I have dry cough', ...]  # Fix typo: "Dray" → "Dry"
Run the Stream:
Execute the notebook or script. The stream will:

Filter English tweets matching the keywords.

Skip retweets and replies.

Save raw tweet JSON data to stream_tweets_json_final.txt.

Stop after collecting 116,459 tweets (adjust limit_tweets as needed).

Monitor Output:
The script prints progress counters and final metrics (e.g., retweets excluded).

Key Features
Filtered Streaming: Uses Tweepy to track COVID-19 keywords and hashtags.

Data Exclusion: Ignores retweets and replies to focus on original content.

Rate Limit Handling: Built-in wait logic for API rate limits.

Limitations & Notes
Twitter API Changes:

Twitter’s API v2 introduced breaking changes (e.g., new authentication, endpoints).

The tweepy.Stream class may require updates for compatibility.

Review X's API documentation for migration guidance.

Typo Alerts:

Fix dray cough → dry cough in the keyword lists.

Rate Limits:
Free API tiers have low rate limits. Consider Academic Research access for larger datasets.

Possible Improvements
Migrate to Twitter API v2 for enhanced features and compliance.

Add data preprocessing steps (e.g., cleaning, sentiment analysis).

Use snscrape as a backup if API access is restricted.

Implement error logging and retries for robust streaming.

License
MIT License (replace with your preferred license).

Disclaimer: Replace all placeholder credentials and validate code against current API rules. Use responsibly in compliance with Twitter/X's terms of service.

