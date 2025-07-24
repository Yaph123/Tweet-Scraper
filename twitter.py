import requests
import pandas as pd
import sqlalchemy as db

BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAJzp3AEAAAAAiTjeVoyZlkHkbjG%2F4iK3Vc%2FVFCg%3DNYzTRMmyUVv3Vq7xoczmE45VLeZD01Vitn4lQvBsDrgQETtm3j'

# Step 1: Get Elon Musk's User ID
username = "elonmusk"
url_user_lookup = f"https://api.twitter.com/2/users/by/username/{username}"
headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
}

response = requests.get(url_user_lookup, headers=headers)

if response.status_code != 200:
    print("Failed to fetch user ID:", response.status_code)
    print(response.text)
    exit()

user_id = response.json()["data"]["id"]
print(f"User ID for {username}: {user_id}")

# Step 2: Get Elon Musk's recent tweets
url_user_tweets = f"https://api.twitter.com/2/users/{user_id}/tweets"
params = {
    "max_results": 5,  # You can increase up to 100 if needed
    "tweet.fields": "created_at,text"
}

response = requests.get(url_user_tweets, headers=headers, params=params)

if response.status_code == 200:
    tweets = response.json().get("data", [])
    if not tweets:
        print("No tweets found.")
        exit()
    print(f"\nRecent tweets from @{username}:")
    for tweet in tweets:
        print(f"- {tweet['created_at']}: {tweet['text']}")
else:
    print("Failed to fetch tweets:", response.status_code)
    print(response.text)
    exit()

# Step 3: Convert tweets list of dicts into DataFrame
df = pd.DataFrame(tweets)

# Step 4: Create SQLite engine and save DataFrame to SQL table
engine = db.create_engine('sqlite:///tweets_database.db')
df.to_sql('elon_tweets', con=engine, if_exists='replace', index=False)

# Step 5: Query the database and print results to confirm
with engine.connect() as connection:
    query_result = connection.execute(db.text("SELECT * FROM elon_tweets;")).fetchall()
    print("\nTweets loaded from the database:")
    print(pd.DataFrame(query_result, columns=df.columns))
