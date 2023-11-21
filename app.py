from flask import Flask, render_template, request, redirect, url_for, jsonify
import json

app = Flask(__name__)

users = []
products = []
posts = []

users_file = 'usuarios.txt'
products_file = 'produtos.txt'
posts_file = 'posts.txt'


def load_users():
    try:
        with open(users_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def load_products():
    try:
        with open(products_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def load_posts():
    try:
        with open(posts_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_users():
    with open(users_file, 'w') as file:
        json.dump(users, file)

def save_products():
    with open(products_file, 'w') as file:
        json.dump(products, file)

def save_posts():
    with open(posts_file, 'w') as file:
        json.dump(posts, file)

@app.route('/api/users')
def users_json():
    users = load_users()
    return jsonify(users)

@app.route('/api/products')
def products_json():
    products = load_products()
    return jsonify(products)

@app.route('/api/posts')
def posts_json():
    posts = load_posts()
    return jsonify(posts)

if __name__ == '__main__':
    app.run()
