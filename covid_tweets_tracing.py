"""
COVID-19 Tweets Streamer (2021 Twitter API v1.1 Implementation)
Created: Oct 2021 | Last Updated: [Your Update Date]
Converted to .py file with compatibility warnings

WARNING: Twitter API changed significantly since Elon Musk's acquisition (now X.com).
This code uses deprecated v1.1 endpoints - may require substantial updates for current API.
"""

# --------------------------
# Section 1: Imports
# --------------------------
import tweepy  # WARNING: Requires tweepy v3.x. Newer v4.x uses different API methods
import json
import datetime

# --------------------------
# Section 2: API Credentials
# --------------------------
# OUTDATED AUTH METHOD: Modern X API prefers OAuth2 with bearer tokens
api_key = '*************************'
api_secret_key = '*************************'
bearer_token = '*************************'
access_token = '*************************'
access_secret = '*************************'

# --------------------------
# Section 3: Authentication
# --------------------------
# DEPRECATED: Twitter API v2 uses tweepy.Client() instead
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)  # Rate limit handling changed in v2

# --------------------------
# Section 4: Filter Parameters
# --------------------------
# NOTE: 'dray' is likely a typo - preserved for historical accuracy
keywords = [
    'I have high fever', 'I have Dray cough',  # TYPO WARNING: 'Dray' should be 'Dry'
    'I have sore throat', 'I have diarrhea',
    'I have difficulty breathing', 'I suffer from loss of taste',
    'I got covid', 'I got covid19'
]

keywords_2 = [
    'pandemic', 'fever', 'dray cough',  # TYPO PRESERVED
    'coronavirus', 'covid19', 'quarantine'
]

# MODERN ALTERNATIVE: Current Twitter API uses rule-based filtering with different syntax
hashtags = ['#COVID19', '#corona_virus', '#Quarantine']

# --------------------------
# Section 5: Stream Listener
# --------------------------
# DEPRECATED CLASS: Twitter API v2 uses StreamClient instead of StreamListener
class StreamListener(tweepy.StreamListener):
    def __init__(self, limit_tweets):
        super().__init__()
        self.counter = 0
        self.out_counter = 0
        self.limit_tweets = limit_tweets

    def on_data(self, data):
        try:
            data_json = json.loads(data)
            # MODERN NOTE: Current API returns different JSON structure
            if data_json.get('in_reply_to_status_id') or data_json.get('text', '').startswith('RT'):
                self.out_counter += 1
            else:
                with open('stream_tweets_json_final.txt', 'a') as f:
                    json.dump(data_json, f)
                    f.write('\n')
                    self.counter += 1
                    print(f"Collected {self.counter} tweets")
                    
                if self.counter >= self.limit_tweets:
                    print(f"Reached target of {self.limit_tweets} tweets at {datetime.datetime.now()}")
                    return False
        except Exception as e:
            print(f"Error: {str(e)}")
            return True

    def on_error(self, status_code):
        # OBSOLETE: Modern API uses different error codes and handling
        if status_code == 420:
            return False
        print(f"Encountered error code: {status_code}")
        return True

# --------------------------
# Section 6: Stream Initialization
# --------------------------
if __name__ == "__main__":
    # WARNING: Modern API requires different initialization
    print("Starting legacy Twitter API v1.1 stream...")
    stream_listener = StreamListener(limit_tweets=1000)  # Reduced for testing
    
    # DEPRECATED: New API uses tweepy.StreamClient(bearer_token=...)
    stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
    
    try:
        # OBSOLETE PARAMETER: Modern filtering uses add_rules() system
        stream.filter(
            track=keywords + keywords_2 + hashtags,
            languages=["en"],
            is_async=False  # WARNING: Async handling changed in modern APIs
        )
    except KeyboardInterrupt:
        print("Stream stopped manually")
    finally:
        print(f"Total collected tweets: {stream_listener.counter}")
        print(f"Excluded retweets/replies: {stream_listener.out_counter}")

# --------------------------
# Compatibility Notes
# --------------------------
"""
CRITICAL UPDATES NEEDED FOR 2023+:
1. Migrate to Twitter API v2 with tweepy v4+ or twitter-api-client
2. Use OAuth2 bearer token authentication
3. Implement new rule-based filtering system
4. Adapt to new Twitter data structure and rate limits
5. Replace deprecated StreamListener with StreamClient
6. Handle new error codes and compliance requirements
"""

# Consider using Twitter's modern filtered stream endpoint:
# https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream