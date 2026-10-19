from flask import Flask, request, jsonify

app = Flask(__name__)

# Fake database (Users aur unke secret notes)
users_db = {
    "1": {"name": "Alice", "secret_note": "Alice ka khufiya note"},
    "2": {"name": "Bob", "secret_note": "Bob ka khufiya note"}
}

# VULNERABLE ENDPOINT
@app.route('/api/get_note', methods=['GET'])
def get_note():
    user_id = request.args.get('id') # User URL mein ?id=1 dalega
    
    if user_id in users_db:
        # VULNERABILITY: Yeh check nahi kar raha ke logged-in user kaun hai!
        return jsonify({"status": "success", "data": users_db[user_id]})
    else:
        return jsonify({"status": "error", "message": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)