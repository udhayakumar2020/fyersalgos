#Imports
from datetime import datetime
import json
import os
from fyers_api import accessToken
from fyers_api import fyersModel



# Variables for login 
app_id = "176EKUCLSL-100"
app_secret= "I9T6F7X8WQ"
redirect_url= "https://trade.fyers.in/api-login/redirect-uri/index.html"


def get_access_token():
    if not os.path.exists('access_token.txt'):
    # if(True):
        session=accessToken.SessionModel(client_id=app_id,secret_key=app_secret,redirect_uri=redirect_url, response_type="code", grant_type="authorization_code")
        response =session.generate_authcode()
        print("Login URL:",response)
        
        auth_code =input("enterAuthCode") 
        session.set_token(auth_code)
        access_token = session.generate_token()["access_token"]
        
        with open('access_token.txt','w') as f:
            f.write(access_token)
    
    else:
        with open('access_token.txt','r') as f:
            access_token = f.read()
        
    return access_token

fyers = fyersModel.FyersModel(client_id=app_id, token=get_access_token(),log_path="")
print('login success')