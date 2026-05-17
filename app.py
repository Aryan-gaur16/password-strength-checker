from flask import Flask, request, jsonify
from checker import check_password_strength

# creates the flask app
app = Flask(__name__)

# This is the home route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Password Strength Checker API!"})

# main route to check password strength
@app.route('/check', methods=['POST'])
def check():
    # get the data sent to the api
    data = request.get_json()

    # This makes sure that a password was actually provided
    if not data or 'password' not in data:
        return jsonify({"error": "Please provide a password"}), 400

    # get the password and check its strength
    password = data['password']
    result = check_password_strength(password)

    return jsonify(result)

# health check route
@app.route('/health')
def health():
    return jsonify({"status": "App is running fine"})

# run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)