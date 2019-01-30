from app.application import app
from flask import jsonify

USERS = {}
GET = 'GET'

# The angled brackets tell Flask to capture anything after the slash into a
# variable named username.
@app.route("/user/<username>", methods=[GET])
def access_users(username):
    if request.method == GET:
        user_details = USERS.get(username)
        if user_details:
            return jsonify(user_details)
        else:
            return Response(status=404)
