
import functions_framework 
import json
import requests
from flask import jsonify
from snippet.notify_ms_team import create_adaptive_card, send_adaptive_card_to_ms_teams

@functions_framework.http   
def send_ms_teams_notification(request):
    request_json = request.get_json(silent=True)
    if request_json and 'message' in request_json:
        message = request_json['message']
    else:
        return jsonify({'error': 'No message provided'}), 400
    if request_json and 'webhook_url' in request_json:
        webhook_url = request_json['webhook_url']
    else:
        return jsonify({'error': 'No webhook url provided'}), 400
    if request_json and 'title' in request_json:
        title = request_json['title']
    else:
        return jsonify({'error': 'No title provided'}), 400

