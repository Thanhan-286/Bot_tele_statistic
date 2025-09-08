import requests
from flask import Flask, request,render_template_string,jsonify
# from pyngrok import ngrok,conf
import json

app = Flask(__name__)

@app.route("/webhook",methods=["POST","GET"])
def send_mess():
    # print("Hello my boy")
    if request.method == "GET":
        return "Webhook is running!"
    else:
        data = request.get_json()
        print(data)
        data_json = json.dumps(data,indent=4,ensure_ascii=False) 
        html = """
            <html>
                <head><title>Hiển thị dữ liệu</title></head>
                <body>
                    <h1>Dữ liệu nhận được</h1>
                    <pre>{{ data|safe }}</pre>
                </body>
            </html>
        """
        return render_template_string(html,data=data_json)

if __name__ == "__main__":
    # Mở tunnel cho cổng 5000
    # public_url = ngrok.connect(5000)
    # print(public_url)

    app.run(debug=True,port=5000)