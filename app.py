import os

from flask import Flask, request, jsonify, render_template, redirect, url_for,send_file
from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import SyncGrant
from werkzeug.utils import secure_filename

app = Flask(__name__)
fake = Faker()


@app.route('/')
def index():
    return render_template('index.html')

# Add your Twilio credentials
@app.route('/token')
def generate_token():
    TWILIO_ACCOUNT_SID='AC2285b8a0a1311e0ff5bddc6c56f577a5'
    TWILIO_SYNC_SERVICE_SID='ISdb4e352375546ace1cb0201238f78474'
    TWILIO_API_KEY='SKe04a3118249920c5972c741483daa45c'
    TWILIO_API_SECRET='7FrRKsjnclqmrzoeMJQj52Vvv0h7DIeb'

    username = request.args.get('username', fake.user_name())

    # create access token with credentials
    token = AccessToken(TWILIO_ACCOUNT_SID, TWILIO_API_KEY, TWILIO_API_SECRET, identity=username)
    # create a Sync grant and add to token
    sync_grant_access = SyncGrant(TWILIO_SYNC_SERVICE_SID)
    token.add_grant(sync_grant_access)
    return jsonify(identity=username, token=token.to_jwt().decode())

# Write the code here
@app.route('/', methods=['POST'])
def download_text():
    content=request.form['text']
    with open('Darsh.txt', 'w') as a:
        a.write(content)
    x='Darsh.txt'
    return send_file(x, as_attachment=True)

if __name__ == "__main__":
    app.run(host='localhost', port='5001', debug=True)
