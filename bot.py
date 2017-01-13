from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('hb8oE3kH7ys+kpqrUcKCEeAii6gvsAmf4hKTJzffNe6VEkcptKpdczTKs7BHuxlkN3JbH8731E1D7/h/4Lu2L5gjKrTTW9kpwGTcZd7w+tpw/RPQEWWILrhfePT0s2nUe2M+O50e1NOPVUpNAF3emwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('4fa72238672c25a970d378eb364ac3af')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))