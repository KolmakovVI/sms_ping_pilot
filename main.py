def read_api_key():
    with open("C:/pyproj/api_key_pilot.txt", "r") as file:
        for line in file:
            api_key = line
    return api_key


def ping_sms(api_key):
    pass



if __name__ == '__main__':
    api_key = read_api_key()

    ping_sms(api_key)

