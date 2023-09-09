import requests

print(requests.get("https://api.yelp.com/v3/businesses/north-india-restaurant-san-francisco/reviews").text)