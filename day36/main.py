import requests
import json
import os
import smtplib
from datetime import datetime, timedelta

BASE_URL_stocks = "https://www.alphavantage.co"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

def raw_api(url, params):
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    return response.json()

def get_past_days() -> tuple:
    today = datetime.now().date()
    one_day = timedelta(days=1)

    yesterday = today - one_day
    day_before = yesterday - one_day

    return yesterday, day_before

def read_stock_data(json_data: dict, yesterday, day_before) -> tuple:
    one_day = timedelta(days=1)
    close_y: dict
    close_p: dict
    try:
        close_y = json_data[yesterday.strftime("%Y-%m-%d")]
    except KeyError:
        yesterday -= one_day
        close_y, close_p = read_stock_data(json_data, yesterday=yesterday, day_before=day_before)
    try:
        close_p = json_data[day_before.strftime("%Y-%m-%d")]
    except KeyError:
        day_before -= one_day
        close_y, close_p = read_stock_data(json_data, yesterday=yesterday, day_before=day_before)

    if close_p and close_y:
        return close_y, close_p

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def stock_movement():
    api_key = os.environ.get("P_API_KEY")
    url = "https://www.alphavantage.co/query"
    params = {
                "apikey": api_key,
                "function": "TIME_SERIES_DAILY",
                "symbol": STOCK,
                "outputsize": "compact",
                "datatype": "json"
              }
    j = raw_api(url, params=params)["Time Series (Daily)"]
    # print(json.dumps(j, indent=4))
    yday, pday = get_past_days()
    close_y, close_p = read_stock_data(j, yesterday=yday, day_before=pday)
    y = float(close_y["4. close"])
    p = float(close_p["4. close"])
    marginal_change = (y - p) / p
    percent = round(marginal_change * 100, 2)
    articles = []
    if abs(percent) > 5:
        articles = get_news(str(pday))
    return percent, articles

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def get_news(from_: str) -> list:
    api_key = os.environ.get("N_API_KEY")
    url = "https://newsapi.org/v2/everything"
    params = {
        "apiKey": api_key,
        "from": from_,
        "q": STOCK,
    }
    j = raw_api(url, params=params)
    articles = j["articles"][:3]
    return articles

## STEP 3: Use https://www.twilio.com - @tmomail.net
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
def send_sms(percent, article) -> bool:
    art = []
    for artic in article:
        temp_dict = {"title": artic["title"].lstrip(": "), "description": artic["description"]}
        art.append(temp_dict)
    print(art)
    message = f"{STOCK} price has changed by {percent}% \n"
    for news in art:
        message = message + f"{news['title']}\n    {news['description']} \n"
    try:
        print(message)
        return True
    except Exception:
        return False

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

def main():
    percent, articles = stock_movement()
    message = ""
    if percent and articles:
        message = send_sms(percent, articles)
    else:
        print(f"{STOCK} did not move very much today")
    if message:
        print("Success!")

if __name__ == "__main__":
    main()