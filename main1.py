from flask import Flask, request, jsonify
import requests
from waitress import serve

app = Flask(__name__)

def authenticate(f):
    def wrapper(*args, **kwargs):
        auth_token = request.headers.get('Authorization')
        expected_token = "1281af29cadf2d18dd2d92a3584a5216" # Set this to whatever you'd like if you want to make it private.

        if not auth_token or auth_token != f'Bearer {expected_token}':
            return jsonify({'error': 'Unauthorized'}), 401

        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper

@app.route('/api/webhooks/<webhookId>/<webhookToken>', methods=['POST'])
@authenticate # Remove this if you don't want a protected route.
def post_to_discord(webhookId, webhookToken):
    data = request.get_json()
    message = data.get('message')
    embeds = data.get('embeds')
    avatar_url = data.get('avatar_url') 

    if not message and (not embeds or not isinstance(embeds, list) or len(embeds) == 0):
        return jsonify({'error': 'Missing "message" or "embeds" in request body'}), 400

    discord_webhook_url = f'https://discord.com/api/webhooks/{webhookId}/{webhookToken}'

    try:
        payload = {
            'content': message or '',
            'embeds': embeds or [],
        }
        if avatar_url:
            payload['avatar_url'] = avatar_url 

        response = requests.post(discord_webhook_url, json=payload)

        if not response.ok:
            print('Error posting to Discord:', response.status_code, response.text)
            return jsonify({'error': 'Failed to post to Discord'}), 500

        return jsonify({'success': True, 'message': 'Posted to Discord successfully!'}), 200
    except Exception as e:
        print('Error posting to Discord:', e)
        return jsonify({'error': 'Failed to post to Discord'}), 500

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=21392)
