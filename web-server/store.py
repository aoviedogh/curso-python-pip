import requests

def get_categories():
  r = requests.get("https://api.escuelajs.co/api/v1/categories")
  print("status_code:", r.status_code)
  print("text:", r.text)
  print("type:", type(r.text))

  categories = r.json()

  for category in categories:
    print("Category:", category["name"])
