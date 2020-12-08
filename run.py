import requests
from datetime import datetime as dt
import time

def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    massage = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = massage)
    return r.status_code


if __name__ == '__main__':
    message = '[LINE Notify] Hello World' # 要傳送的訊息內容
    token = 'U6T7zu3vFz40C3uVOVKrtdpoHpMBXCmKhmHrs9Q1cif' # 權杖值

    # lineNotifyMessage(token, message)
    while True:
        if dt.now().minute%5==0:
            lineNotifyMessage(token,'hello')
