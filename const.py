discount_codes = {
    "SAVE10": 10,
    "WELCOME20": 20,
    "STUDENT15": 15,
    "NEWUSER25": 25
}

creds = [
    {"ID": "24AIML043", "Password": "8888"},
    {"ID": "24AIML046", "Password": "4444"}
]
        

product = [
    {"ProductID": 101, "ProductName": "Smartphone XYZ", "Category": "Electronics", "Price": 299.99},
    {"ProductID": 102, "ProductName": "Laptop ABC", "Category": "Electronics", "Price": 899.99},
    {"ProductID": 103, "ProductName": "Wireless Headphones", "Category": "Electronics", "Price": 59.99},
    {"ProductID": 104, "ProductName": "LED TV 50-inch", "Category": "Electronics", "Price": 499.99},
    {"ProductID": 105, "ProductName": "Bluetooth Speaker", "Category": "Electronics", "Price": 79.99},
    {"ProductID": 106, "ProductName": "Smartwatch", "Category": "Electronics", "Price": 129.99},
    {"ProductID": 107, "ProductName": "Gaming Mouse", "Category": "Electronics", "Price": 39.99},
    {"ProductID": 108, "ProductName": "Mechanical Keyboard", "Category": "Electronics", "Price": 69.99},
    {"ProductID": 109, "ProductName": "Portable Power Bank", "Category": "Electronics", "Price": 19.99},
    {"ProductID": 110, "ProductName": "Wireless Charger", "Category": "Electronics", "Price": 25.99},
    
    {"ProductID": 201, "ProductName": "Running Shoes", "Category": "Fashion", "Price": 69.99},
    {"ProductID": 202, "ProductName": "Jeans for Men", "Category": "Fashion", "Price": 49.99},
    {"ProductID": 203, "ProductName": "Leather Wallet", "Category": "Fashion", "Price": 29.99},
    {"ProductID": 204, "ProductName": "Sunglasses", "Category": "Fashion", "Price": 19.99},
    {"ProductID": 205, "ProductName": "Cotton T-shirt", "Category": "Fashion", "Price": 14.99},
    {"ProductID": 206, "ProductName": "Watch for Women", "Category": "Fashion", "Price": 119.99},
    {"ProductID": 207, "ProductName": "Chinos for Men", "Category": "Fashion", "Price": 39.99},
    {"ProductID": 208, "ProductName": "Sneakers for Women", "Category": "Fashion", "Price": 89.99},
    {"ProductID": 209, "ProductName": "Formal Shirt", "Category": "Fashion", "Price": 34.99},
    {"ProductID": 210, "ProductName": "Jacket for Winter", "Category": "Fashion", "Price": 99.99},
    
    {"ProductID": 301, "ProductName": "Stainless Steel Water Bottle", "Category": "Home & Kitchen", "Price": 22.99},
    {"ProductID": 302, "ProductName": "Air Fryer", "Category": "Home & Kitchen", "Price": 149.99},
    {"ProductID": 303, "ProductName": "Coffee Maker", "Category": "Home & Kitchen", "Price": 89.99},
    {"ProductID": 304, "ProductName": "Smart Thermostat", "Category": "Home & Kitchen", "Price": 129.99},
    {"ProductID": 305, "ProductName": "Electric Kettle", "Category": "Home & Kitchen", "Price": 34.99},
    {"ProductID": 306, "ProductName": "Cookware Set", "Category": "Home & Kitchen", "Price": 159.99},
    {"ProductID": 307, "ProductName": "Blender", "Category": "Home & Kitchen", "Price": 49.99},
    {"ProductID": 308, "ProductName": "Robot Vacuum", "Category": "Home & Kitchen", "Price": 249.99},
    {"ProductID": 309, "ProductName": "Toaster", "Category": "Home & Kitchen", "Price": 29.99},
    {"ProductID": 310, "ProductName": "Waffle Maker", "Category": "Home & Kitchen", "Price": 39.99},
    
    {"ProductID": 401, "ProductName": "Novel: The Great Adventure", "Category": "Books", "Price": 15.99},
    {"ProductID": 402, "ProductName": "Cookbook: Healthy Eating", "Category": "Books", "Price": 19.99},
    {"ProductID": 403, "ProductName": "Children's Book: Adventure Time", "Category": "Books", "Price": 8.99},
    {"ProductID": 404, "ProductName": "Science Fiction: Mars Exploration", "Category": "Books", "Price": 12.99},
    {"ProductID": 405, "ProductName": "Fantasy Novel: Dragon's Quest", "Category": "Books", "Price": 16.99},
    {"ProductID": 406, "ProductName": "Biography: Life of a Legend", "Category": "Books", "Price": 18.99},
    {"ProductID": 407, "ProductName": "Self-Help: Mindfulness", "Category": "Books", "Price": 9.99},
    {"ProductID": 408, "ProductName": "Mystery Novel: The Secret Code", "Category": "Books", "Price": 14.99},
    {"ProductID": 409, "ProductName": "History Book: Ancient Civilizations", "Category": "Books", "Price": 21.99},
    {"ProductID": 410, "ProductName": "Travel Guide: Europe Adventure", "Category": "Books", "Price": 24.99},
    
    {"ProductID": 501, "ProductName": "Yoga Mat", "Category": "Sports & Outdoors", "Price": 19.99},
    {"ProductID": 502, "ProductName": "Dumbbells Set", "Category": "Sports & Outdoors", "Price": 39.99},
    {"ProductID": 503, "ProductName": "Tennis Racket", "Category": "Sports & Outdoors", "Price": 49.99},
    {"ProductID": 504, "ProductName": "Camping Tent", "Category": "Sports & Outdoors", "Price": 129.99},
    {"ProductID": 505, "ProductName": "Fishing Rod", "Category": "Sports & Outdoors", "Price": 24.99},
    {"ProductID": 506, "ProductName": "Bicycle Helmet", "Category": "Sports & Outdoors", "Price": 19.99},
    {"ProductID": 507, "ProductName": "Baseball Gloves", "Category": "Sports & Outdoors", "Price": 39.99},
    {"ProductID": 508, "ProductName": "Golf Club Set", "Category": "Sports & Outdoors", "Price": 499.99},
    {"ProductID": 509, "ProductName": "Running Shorts", "Category": "Sports & Outdoors", "Price": 14.99},
    {"ProductID": 510, "ProductName": "Swimming Goggles", "Category": "Sports & Outdoors", "Price": 9.99},
    
    {"ProductID": 601, "ProductName": "Pet Bed", "Category": "Pets", "Price": 49.99},
    {"ProductID": 602, "ProductName": "Cat Litter Box", "Category": "Pets", "Price": 19.99},
    {"ProductID": 603, "ProductName": "Dog Leash", "Category": "Pets", "Price": 14.99},
    {"ProductID": 604, "ProductName": "Bird Cage", "Category": "Pets", "Price": 59.99},
    {"ProductID": 605, "ProductName": "Dog Food", "Category": "Pets", "Price": 34.99},
    {"ProductID": 606, "ProductName": "Cat Food", "Category": "Pets", "Price": 24.99},
    {"ProductID": 607, "ProductName": "Pet Toy Set", "Category": "Pets", "Price": 19.99},
    {"ProductID": 608, "ProductName": "Dog Collar", "Category": "Pets", "Price": 9.99},
    {"ProductID": 609, "ProductName": "Pet Water Fountain", "Category": "Pets", "Price": 39.99},
    {"ProductID": 610, "ProductName": "Pet Shampoo", "Category": "Pets", "Price": 12.99}
]
        
        