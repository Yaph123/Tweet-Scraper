import requests

def get_latest_story():
    # Step 1: Get the list of new story IDs
    url = "https://hacker-news.firebaseio.com/v0/newstories.json"
    response = requests.get(url)
    story_ids = response.json()

    # Step 2: Loop through the IDs and find the first actual 'story'
    for story_id in story_ids:
        item_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        item_response = requests.get(item_url)
        item = item_response.json()

        # Check if item is a 'story'
        if item and item.get('type') == 'story':
            title = item.get('title', 'No Title')
            author = item.get('by', 'Unknown')
            link = item.get('url', f"https://news.ycombinator.com/item?id={story_id}")

            # Print the story details
            print("📰 Title:", title)
            print("✍️ Author:", author)
            print("🔗 Link:", link)
            break

# Run the function
get_latest_story()
