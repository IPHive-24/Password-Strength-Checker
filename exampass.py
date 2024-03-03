from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import string

app = Flask(__name__, template_folder='templates')
CORS(app)

def check_password_strength(password):
    score=0
    length = len(password)

    if length > 20:
        return -1, None  # Password is too long

    def check_password_strength(password):
      length = len(password)

    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    score = 0
    combinations = None

    if has_lower and has_upper and has_digit and has_special:
        score = 4
        combinations = 'Uppercase, lowercase, numbers, and special characters'
    elif has_lower and has_upper and has_special:
        score = 3
        combinations = 'Uppercase, lowercase, and special characters '
    elif has_special:
        score = 2
        combinations = 'only special'
    elif has_upper and has_digit:
        score = 2
        combinations = 'Uppercase, numbers'   
    elif has_lower and has_upper:
        score = 1
        combinations = 'Lowercase, uppercase'     
    elif has_lower or has_upper or has_digit:
        score = 0
        combinations = 'Uppercase or lowercase or digits'
    elif length < 8:
        score = 0
        combinations = 'Less than 8 characters'
    else:
        score = -2
        combinations = 'Less than 8 characters'

    return score, combinations


@app.route('/')
def index():
    return render_template('password1.html')

@app.route('/check_password_strength', methods=['POST'])
def check_password_strength_route():
    data = request.json
    password = data.get('password')
    score, combinations = check_password_strength(password)
    return jsonify({'score': score, 'combinations': combinations})

if __name__ == '__main__':
    app.run(debug=True)
