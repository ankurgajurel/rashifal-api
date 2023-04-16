import requests
import json
from flask import Flask

url = "http://127.0.0.1:9991/"

daily_rashi_path = "/daily/singha"
monthly_rashi_path = "/monthly/singha"
yearly_rashi_path = "/yearly/singha"


def generate_rashifal(url, operation):
    if operation == "daily":
        url = url + daily_rashi_path
        ref = 'daily_rashifal_singha'
    elif operation == "monthly":
        url = url + monthly_rashi_path
        ref = 'daily_rashifal_singha'
    elif operation == "yearly":
        url = url + yearly_rashi_path
        ref = 'daily_rashifal_singha'
    else:
        return "Invalid operation"
    response = requests.request("GET", url)
    data = json.loads(response.text)[ref]
    print(data)
    return data

daily = generate_rashifal(url, "daily")
monthly = generate_rashifal(url, "monthly")
yearly = generate_rashifal(url, "yearly")



app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<div style=\"font-size: 200%;overflow:hidden;\"> Daily: {}<br> <br> <br> MONTHLY: {} <br> <br><br> YEARLY: {}<br><br><br> check more at: <a href=\"https:\/\/github.com\/ankurgajurel\/rashifal-api\">https://github.com/ankurgajurel/rashifal-api</a></div>".format(daily,monthly,yearly)

if __name__ == "__main__":
    app.run(debug=True, port=9881)