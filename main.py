import json

import requests


def read_api_key():
    with open("D:/pyproj/api_key_pilot.txt", "r") as file:
        for line in file:
            api_key = line
    return api_key


def ping_sms_single(api_key):
    # url_balance = "https://smspilot.ru/api.php?balance=rur&apikey=" + api_key  # ссылка на запрос баланса кошелька
    url_ping = "https://smspilot.ru/api.php?send=HLRVIP&to=79087964781&callback=https%3A%2F%2Fexample.com%2Fhlr-status.php&apikey=XYZ&format=v"
    # пример ссылки на запрос HLRVIP
    # https://smspilot.ru/api.php?send=HLRVIP&to=79087964781&callback=https%3A%2F%2Fexample.com%2Fhlr-status.php&apikey=XYZ&format=v
    # print(url)
    r = requests.get(url_ping)
    j = json.loads(r.text)
    print(j)


def ping_sms_paсkage(api_key, nubmers):
    url = "https://smspilot.ru/api2.php"
    param = {'api_key': api_key, "text": "HLRVIP"}

    list_of_numb = []
    for number in numbers:
        numb_dict = {'to': number}
        list_of_numb.append(numb_dict) # Как вставить словарь в список???
    param['send'] = list_of_numb
    print(param)
    return param




if __name__ == '__main__':
    api_key = read_api_key()
    numbers = ["79686073656", "79647976061", "79533525333"]
    # ping_sms_single(api_key) # call def with single nubm checking
    ping_sms_paсkage(api_key, numbers)

