import requests

TOKEN_API = "7943851001:AAE7LY__KTM13YuwfbcldhUFU0PIzww_elI"



def setwebhook_tele():
    API_TELE = f"https://api.telegram.org/bot{TOKEN_API}/setwebhook"
    params = {
        # Có thể thay đổi bất cứ lúc nào 
        "url": "https://d58e43739f59.ngrok-free.app/webhook"
    }

    response = requests.post(API_TELE,params=params)
    print(response.json())
def deletewebhook():
    API_DELETE = f"https://api.telegram.org/bot{TOKEN_API}/deleteWebhook"
    params = {
        "drop_pending_updates":True
    }
    response = requests.post(API_DELETE,params=params)
    print(response.json())
def getInfowebhook():
    url = f"https://api.telegram.org/bot{TOKEN_API}/getWebhookInfo"
    response = requests.get(url=url)
    print(response.json())

if __name__ == "__main__":
    deletewebhook()
    setwebhook_tele()
    getInfowebhook()

