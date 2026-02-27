from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder='.')
CORS(app)

products = [
    # Fruits
    {"id": 1,  "name": "Bananas",      "category": "Fruits",     "price": 120,  "rating": 4.5, "image": "https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?w=300&q=80"},
    {"id": 2,  "name": "Apples",       "category": "Fruits",     "price": 350,  "rating": 4.7, "image": "https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?w=300&q=80"},
    {"id": 3,  "name": "Mangoes",      "category": "Fruits",     "price": 280,  "rating": 4.9, "image": "https://images.unsplash.com/photo-1553279768-865429fa0078?w=300&q=80"},
    {"id": 4,  "name": "Oranges",      "category": "Fruits",     "price": 200,  "rating": 4.4, "image": "https://images.unsplash.com/photo-1611080626919-7cf5a9dbab12?w=300&q=80"},
    {"id": 5,  "name": "Watermelon",   "category": "Fruits",     "price": 150,  "rating": 4.6, "image": "https://images.unsplash.com/photo-1563114773-84221bd62daa?w=300&q=80"},
    {"id": 6,  "name": "Grapes",       "category": "Fruits",     "price": 320,  "rating": 4.3, "image": "https://images.unsplash.com/photo-1537640538966-79f369143f8f?w=300&q=80"},
    # Vegetables
    {"id": 7,  "name": "Tomatoes",     "category": "Vegetables", "price": 80,   "rating": 4.2, "image": "https://images.unsplash.com/photo-1546094096-0df4bcaaa337?w=300&q=80"},
    {"id": 8,  "name": "Potatoes",     "category": "Vegetables", "price": 40,   "rating": 4.0, "image": "https://images.unsplash.com/photo-1518977676601-b53f82aba655?w=300&q=80"},
    {"id": 9,  "name": "Onions",       "category": "Vegetables", "price": 60,   "rating": 3.9, "image": "https://images.unsplash.com/photo-1508747703725-719777637510?w=300&q=80"},
    {"id": 10, "name": "Spinach",      "category": "Vegetables", "price": 50,   "rating": 4.3, "image": "https://images.unsplash.com/photo-1576045057995-568f588f82fb?w=300&q=80"},
    {"id": 11, "name": "Carrots",      "category": "Vegetables", "price": 70,   "rating": 4.4, "image": "https://images.unsplash.com/photo-1598170845058-32b9d6a5da37?w=300&q=80"},
    {"id": 12, "name": "Capsicum",     "category": "Vegetables", "price": 90,   "rating": 4.1, "image": "https://images.unsplash.com/photo-1614806687007-2215083f4b4b?w=300&q=80"},
    # Dairy
    {"id": 13, "name": "Fresh Milk",   "category": "Dairy",      "price": 90,   "rating": 4.5, "image": "https://images.unsplash.com/photo-1563636619-e9143da7973b?w=300&q=80"},
    {"id": 14, "name": "Eggs (12pcs)", "category": "Dairy",      "price": 240,  "rating": 4.7, "image": "https://images.unsplash.com/photo-1582722872445-44dc5f7e3c8f?w=300&q=80"},
    {"id": 15, "name": "Yogurt",       "category": "Dairy",      "price": 120,  "rating": 4.3, "image": "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=300&q=80"},
    {"id": 16, "name": "Butter",       "category": "Dairy",      "price": 180,  "rating": 4.2, "image": "https://images.unsplash.com/photo-1589985270826-4b7bb135bc9d?w=300&q=80"},
    # Bakery
    {"id": 17, "name": "Bread Loaf",   "category": "Bakery",     "price": 80,   "rating": 4.1, "image": "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=300&q=80"},
    {"id": 18, "name": "Croissant",    "category": "Bakery",     "price": 60,   "rating": 4.5, "image": "https://images.unsplash.com/photo-1555507036-ab1f4038808a?w=300&q=80"},
    # Meat
    {"id": 19, "name": "Chicken 1kg",  "category": "Meat",       "price": 750,  "rating": 4.6, "image": "https://images.unsplash.com/photo-1604503468506-a8da13d82791?w=300&q=80"},
    {"id": 20, "name": "Mutton 1kg",   "category": "Meat",       "price": 1400, "rating": 4.4, "image": "https://images.unsplash.com/photo-1529692236671-f1f6cf9683ba?w=300&q=80"},
]

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/about')
def about():
    return send_from_directory('.', 'about.html')

@app.route('/api/products')
def get_products():
    return jsonify(products)

@app.route('/api/products/<category>')
def get_by_category(category):
    filtered = [p for p in products if p['category'].lower() == category.lower()]
    return jsonify(filtered)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
