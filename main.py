import functions_framework
from flask import jsonify
from snippet.notify_ms_team import create_adaptive_card, send_adaptive_card_to_ms_teams


@functions_framework.http
def send_ms_teams_notification(request):

    request_json = request.get_json(silent=True)

    if not request_json:
        return "ไม่พบข้อมูล JSON ใน request", 400

    webhook = request_json.get("webhook")
    message_title = request_json.get("message_title")
    message_body = request_json.get("message_body")

    adabtive_card = create_adaptive_card(
        header_text=message_title, message_body=message_body
    )
    send_adaptive_card_to_ms_teams(webhook, adabtive_card)
