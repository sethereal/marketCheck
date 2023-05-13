import requests

access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzaWQiOiIzRUhSYjRhMVpKS01YdlZZTlcyeW1WUWdCUGd4UVNKYyIsImNzcmZfdG9rZW4iOiJjMWVhY2YxMWM3YzhjMjRjZGFjNjY5OGU4NGY4OGY4Mzk3NjgwNzYwIiwiZXhwIjoxNjg2MjY3Nzg5LCJpYXQiOjE2ODEwODM3ODksImlzcyI6Imp3dCIsImF1ZCI6Imp3dCIsImF1dGhfdHlwZSI6ImNvb2tpZSIsInNlY3VyZSI6ZmFsc2UsImp3dF9pZGVudGl0eSI6Inc4MWJjYjVWVDdFWjYyVHljaTBKbENMeExySUNlbTZzIiwibG9naW5fdWEiOiJiJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwOS4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzExMS4wJyIsImxvZ2luX2lwIjoiYic2OC4yMzAuMjE2Ljk1JyJ9.cZTm9wzoepyS4clDUMj7iuFP80ECGgjRzpRVxR6-1-Y"

headers = {
    "Authorization": "JWT " + "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzaWQiOiIzRUhSYjRhMVpKS01YdlZZTlcyeW1WUWdCUGd4UVNKYyIsImNzcmZfdG9rZW4iOiJjMWVhY2YxMWM3YzhjMjRjZGFjNjY5OGU4NGY4OGY4Mzk3NjgwNzYwIiwiZXhwIjoxNjg2MjY3Nzg5LCJpYXQiOjE2ODEwODM3ODksImlzcyI6Imp3dCIsImF1ZCI6Imp3dCIsImF1dGhfdHlwZSI6ImNvb2tpZSIsInNlY3VyZSI6ZmFsc2UsImp3dF9pZGVudGl0eSI6Inc4MWJjYjVWVDdFWjYyVHljaTBKbENMeExySUNlbTZzIiwibG9naW5fdWEiOiJiJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwOS4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzExMS4wJyIsImxvZ2luX2lwIjoiYic2OC4yMzAuMjE2Ljk1JyJ9.cZTm9wzoepyS4clDUMj7iuFP80ECGgjRzpRVxR6-1-Y"
}

response = requests.get("https://api.warframe.market/v1/items", headers=headers)

def testFunc():
    if response.ok:
        items = response.json()
        print(f"Successfully retrieved {len(items)} items.")
    else:
        print("Failed to retrieve items.")

def apiRequest(item_name):
    response = requests.get(f"https://api.warframe.market/v1/items/{item_name}/orders", headers=headers)
    if response.ok:
        orders = response.json()["payload"]["orders"]
        return orders
    else:
        print("Failed to retrieve orders.")
        return None



