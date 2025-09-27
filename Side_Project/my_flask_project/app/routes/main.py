from flask import Blueprint, request, jsonify, render_template
import os
main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    os.system('cls')
    return render_template('index.html')

# API GET
@main.route('/get_test', methods=['GET'])
def hello():
    os.system('cls')
    return jsonify({
        "message": "POST API is Active",
        "status": "OK"
    })

# API POST
@main.route('/post_test', methods=['POST'])
def submit():
    os.system('cls')
    data = request.get_json()
    name = data.get('name', 'Không rõ')
    return jsonify({
        "message": f"Chào {name}, POST API is Active",
        "status": "OK"
    })
