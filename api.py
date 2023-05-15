import requests

access_token = "your_token"

headers = {
    "Authorization": "JWT " + "your_token"
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



