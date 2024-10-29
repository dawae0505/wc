from flask import Flask, request, abort
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# Replace with your LINE Bot's channel secret and access token
LINE_CHANNEL_SECRET = 'e90484a9aee263155e90c975d4b5e327'
LINE_CHANNEL_ACCESS_TOKEN = 'VLbmxh7077c9a73/INENK2y70KsX1OiymZ2N3SpqOhWL8ZJLpMuYjkP6tLC+AE0MOQRmbAjg3/8fvj/5KJHKmOhcbgSXnndX27mxHM6YIUp+6Z1iiDhJEl/8zVAoHkh1W+1QggqCswYbRP1U4pUAgQdB04t89/1O/w1cDnyilFU='

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(LINE_CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # Process each event
    for event in events:
        if isinstance(event, MessageEvent) and isinstance(event.message, TextMessage):
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=event.message.text)
            )

    return 'OK'

if __name__ == "__main__":
    app.run(port=8000)