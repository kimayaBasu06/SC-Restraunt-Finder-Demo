# import pandas as pd

# # Define the data for the Santa Cruz Bites blog
# # NOTE: The latitude and longitude coordinates are approximations for demonstration purposes.

# RESTAURANTS_DATA = [
#     {
#         "id": 1,
#         "name": "Betty's Burgers",
#         "category": "Casual Dining",
#         "description": "Famous for their massive, juicy burgers and extensive beer selection. A local favorite right near the boardwalk.",
#         "lat": 36.9691,
#         "lon": -122.0177,
#         "best_times": "Lunch or dinner, especially after a day at the beach. Open until 9 PM.",
#         "cost": "$$",
#         "image_url": "https://images.unsplash.com/photo-1627918451121-a1cc0a53b5e4?q=80&w=2942&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
#         "tags": ["burgers", "beach", "american"],
#         "similar": [2, 5],
#     },
#     {
#         "id": 2,
#         "name": "West End Tap & Kitchen",
#         "category": "New American",
#         "description": "Upscale pub fare with a focus on local, seasonal ingredients and a great atmosphere for a sophisticated evening.",
#         "lat": 37.0003,
#         "lon": -122.0620,
#         "best_times": "Dinner, especially weekend evenings. Great for happy hour.",
#         "cost": "$$$",
#         "image_url": "https://images.unsplash.com/photo-1549488349-e380e927c62d?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
#         "tags": ["tapas", "craft beer", "cocktails"],
#         "similar": [1, 3],
#     },
#     {
#         "id": 3,
#         "name": "Companion Bakeshop",
#         "category": "Cafe/Bakery",
#         "description": "Artisan bakery known for its incredible sourdough, pastries, and coffee. Perfect for a morning treat.",
#         "lat": 36.9839,
#         "lon": -122.0468,
#         "best_times": "Early mornings on weekdays for the freshest bread. Lunch for a light sandwich.",
#         "cost": "$",
#         "image_url": "https://images.unsplash.com/photo-1583091910627-2292f3922650?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
#         "tags": ["coffee", "pastries", "breakfast"],
#         "similar": [4],
#     },
#     {
#         "id": 4,
#         "name": "Taqueria Vallarta",
#         "category": "Mexican Food",
#         "description": "The quintessential Santa Cruz taco experience. Famous for its 'super' burritos and extensive salsa bar.",
#         "lat": 36.9740,
#         "lon": -122.0298,
#         "best_times": "Lunch rush (quick service) or a late-night bite.",
#         "cost": "$",
#         "image_url": "https://images.unsplash.com/photo-1511910849309-0dffb8785141?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
#         "tags": ["mexican", "tacos", "cheap"],
#         "similar": [1, 5],
#     },
#     {
#         "id": 5,
#         "name": "Oswald Restaurant",
#         "category": "Fine Dining",
#         "description": "A refined downtown dining experience offering a seasonal menu with high-quality, inventive dishes and a great wine list.",
#         "lat": 36.9745,
#         "lon": -122.0292,
#         "best_times": "Dinner reservation required. Great for special occasions.",
#         "cost": "$$$$",
#         "image_url": "https://images.unsplash.com/photo-1517248135460-449e791c10d7?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
#         "tags": ["fine dining", "wine", "upscale"],
#         "similar": [2],
#     }
# ]

# # Convert the data list to a pandas DataFrame for easy searching and manipulation
# df_restaurants = pd.DataFrame(RESTAURANTS_DATA)
# # Set the name as the index for quick lookups
# df_restaurants.set_index('name', inplace=True)