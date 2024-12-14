# d1gitalproxy

- This is a free and simple to use Discord webhook proxy, you can use this for your Roblox games or for other purposes.
Usage example:
```
import requests

webhook_url = "https://your-selfhosted-api.com/api/webhooks/1317507514232737792/nSM2QjLxFnzG9KHzbSE9m9uMbAoeNGoW4yN9vsQG0diVswnk2PKPLl1xpuT_R9kjk093"
bearer_token = "1281af29cadf2d18dd2d92a3584a5216" # Set this accordingly to your API password. Or remove the decorator from your API if you don't want to use so.

embed = {
    "title": "d1gitalmemories",
    "description": "Hello World!",
    "url": "https://leoo.lol",
    "color": 5814783, #HEX CODE
    "fields": [
        {"name": "Field 1", "value": "Value 1", "inline": True},
        {"name": "Field 2", "value": "Value 2", "inline": True}
    ],
    "footer": {"text": "d1gitalmemories"},
    "timestamp": "2024-10-26T00:00:00.000Z"  # ISO8601 timestamp
}

# Payload
payload = {
    "username": "d1gitalmemories",
    "avatar_url": "https://avatars.githubusercontent.com/u/155659333?v=4",  # Optional: Bot avatar URL
    "embeds": [embed]
}

headers = {
    "Authorization": f"Bearer {bearer_token}",
    "Content-Type": "application/json"
}

response = requests.post(webhook_url, json=payload, headers=headers)

if response.status_code == 204:
    print("Embed posted successfully!")
else:
    print(f"Failed to post embed: {response.status_code}")
    print(response.text)
```
