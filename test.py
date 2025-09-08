import requests
from flask import Flask, request

TOKEN = '7943851001:AAE7LY__KTM13YuwfbcldhUFU0PIzww_elI'
API_TELE = f"https://api.telegram.org/bot{TOKEN}"

app = Flask(__name__)

#Gửi message thường
def send_mes(chat_id,text,reply_markup=None):
    url = f"{TOKEN}/sendMessage"
    param = {
        'chat_id' : chat_id,
        'text': text
    }
    if reply_markup:
        param['reply_markup'] = reply_markup
    requests.post(url,json=param)
# Xử lý start
def start(chat_id):
    send_mes(chat_id=chat_id,text="Hello, I'm a bot for statistic issue of Shipping System")
# Xử lý help
def help(chat_id):
    send_mes(chat_id=chat_id,text="Hello, What do you need?")

# Xử lý callback từ button
def handle_callback_query(callback_query):
    url = f"{API_TELE}/editMessageText"
    query_id = callback_query['id']
    data = callback_query['data']
    message = callback_query['message']
    chat_id = callback_query["chat"]["id"]

     # Trả lời callback (bắt buộc)
    requests.post(f"{BASE_URL}/answerCallbackQuery", json={"callback_query_id": query_id})

    # Edit lại message
    text = f"You selected option: {data.split('_')[1]}"
    requests.post(url, 
    json={
        "chat_id": chat_id,
        "message_id": message["message_id"],
        "text": text
    })

# Endpoint nhận update từ Telegram (webhook)
# @app.route(f"/{TOKEN}", methods=["POST"])
# def webhook():
#     update = request.get_json()
#     print(update)
#     if "message" in update:
#         message = update["message"]
#         chat_id = message["chat"]["id"]

#         if "text" in message:
#             text = message["text"]
#             if text == "/start":
#                 handle_start(chat_id)
#             elif text == "/help":
#                 handle_help(chat_id)
#             else:
#                 send_message(chat_id, "I don't understand that command.")

#     elif "callback_query" in update:
#         handle_callback_query(update["callback_query"])

#     return "ok"

@app.route("/getMess",methods=["GET"])
def getMess(offset = None):
    url = f'{TOKEN}/getUpdates'
    param = {
        'offset' : offset,
        'timeout': 100
    }
    response = requests.get(url,params= param)
    print('Hello world')
    return response.json()

if __name__ == "__main__":
    # Chạy Flask server
    app.run(host="0.0.0.0", port=5000)