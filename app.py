from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

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


def save_users(users_data):
    with open(users_file, 'w') as file:
        json.dump(users_data, file)


@app.route('/api/users')
def users_json():
    loaded_users = load_users()
    return jsonify(loaded_users)


@app.route('/api/products')
def products_json():
    try:
        loaded_products = load_products()
        return jsonify(loaded_products)
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": "Internal Server Error"}), 500


@app.route('/api/posts')
def posts_json():
    loaded_posts = load_posts()
    return jsonify(loaded_posts)


@app.route('/api/register', methods=['POST'])
def register():
    try:
        new_user_data = request.get_json()
        users_data = load_users()
        users_data.append(new_user_data)
        save_users(users_data)
        return jsonify({"message": "User registered successfully"}), 200
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": "Internal Server Error"}), 500


@app.route('/api/recover-password', methods=['POST'])
def recover_password():
    try:
        user_email = request.json.get('email')
        return jsonify({"message": "Password recovery initiated. Check your email for instructions."}), 200
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": "Internal Server Error"}), 500

@app.route('/api/login', methods=['POST'])
def login():
    try:
        login_data = request.get_json()
        email = login_data.get('email')
        password = login_data.get('password')

        users_data = load_users()

        for user in users_data:
            if user.get('email') == email and user.get('password') == password:
                return jsonify({"message": "Login successful"}), 200
        
        return jsonify({"error": "Invalid email or password"}), 401
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": "Internal Server Error"}), 500
        
if __name__ == '__main__':
    app.run()
