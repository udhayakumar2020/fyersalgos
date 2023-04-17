print("you can!!")
import login as login
from datetime import datetime
import time
import os
import time
import json
from niftystocks import ns
import math

import pyttsx3
true = True 
# WHOLE WROMG ITS JUST BACKTESTING WE NEED TO CHANGE AS A LIVE PRICE TO TRADE IN LICE AND CURRENT PRICe
# =>After 10:15 no trade is a best 
# => buffer of 0.01 is a best to cut some entries 
loss=0
profit=0
symbolsinlongprofit=[]
symbolsinlongloss=[]
symbolsinshortloss=[]
symbolsinshortprofit=[]
high=[]
trades = 0



# print(login.fyers.get_profile())
print("LOGGED-IN")
# {'s': 'ok', 'code': 200, 'message': '', 'netPositions': [{'symbol': 'MCX:SILVERMIC23APRFUT', 'id': 'MCX:SILVERMIC23APRFUT-BO', 'buyAvg': 70047, 'buyQty': 2, 'buyVal': 140094, 'sellAvg': 69990, 'sellQty': 2, 'sellVal': 139980, 'netAvg': 0, 'netQty': 0, 'side': 0, 'qty': 0, 'productType': 'BO', 'realized_profit': -114, 'crossCurrency': '', 'qtyMulti_com': 1, 'segment': '20', 'ltp': 70915, 'fyToken': '1120230428245470', 'exchange': '11', 'unrealized_profit': 0, 'dayBuyQty': 2, 'cfBuyQty': 0, 'daySellQty': 2, 'cfSellQty': 0, 'rbiRefRate': 1, 'pl': -114, 'slNo': 0, 'avgPrice': 0}, {'symbol': 'NSE:COALINDIA-EQ', 'id': 'NSE:COALINDIA-EQ-BO', 'buyAvg': 212.3, 'buyQty': 105, 'buyVal': 22291.5, 'sellAvg': 211.55, 'sellQty': 105, 'sellVal': 22212.75, 'netAvg': 0, 'netQty': 0, 'side': 0, 'qty': 0, 'productType': 'BO', 'realized_profit': -78.75, 'crossCurrency': '', 'qtyMulti_com': 1, 'segment': '10', 'ltp': 208.45, 'fyToken': '101000000020374', 'exchange': '10', 'unrealized_profit': 0, 'dayBuyQty': 105, 'cfBuyQty': 0, 'daySellQty': 105, 'cfSellQty': 0, 'rbiRefRate': 1, 'pl': -78.75, 'slNo': 0, 'avgPrice': 0}, {'symbol': 'NSE:BANKNIFTY23MAR39700CE', 'id': 'NSE:BANKNIFTY23MAR39700CE-BO', 'buyAvg': 389, 'buyQty': 50, 'buyVal': 19450, 'sellAvg': 378.075, 'sellQty': 50, 'sellVal': 18903.75, 'netAvg': 0, 'netQty': 0, 'side': 0, 'qty': 0, 'productType': 'BO', 'realized_profit': -546.2500000000006, 'crossCurrency': '', 'qtyMulti_com': 1, 'segment': '11', 'ltp': 191.85, 'fyToken': '101123032952616', 'exchange': '10', 'unrealized_profit': 0, 'dayBuyQty': 50, 'cfBuyQty': 0, 'daySellQty': 50, 'cfSellQty': 0, 'rbiRefRate': 1, 'pl': -546.2500000000006, 'slNo': 0, 'avgPrice': 0}, {'symbol': 'NSE:NIFTY23MAR17000CE', 'id': 'NSE:NIFTY23MAR17000CE-BO', 'buyAvg': 155.825, 'buyQty': 200, 'buyVal': 31165, 'sellAvg': 148.8625, 'sellQty': 200, 'sellVal': 29772.5, 'netAvg': 0, 'netQty': 0, 'side': 0, 'qty': 0, 'productType': 'BO', 'realized_profit': -1392.4999999999955, 'crossCurrency': '', 'qtyMulti_com': 1, 'segment': '11', 'ltp': 83, 'fyToken': '101123032957270', 'exchange': '10', 'unrealized_profit': 0, 'dayBuyQty': 200, 'cfBuyQty': 0, 'daySellQty': 200, 'cfSellQty': 0, 'rbiRefRate': 1, 'pl': -1392.4999999999955, 'slNo': 0, 'avgPrice': 0}, {'symbol': 'NSE:NIFTY23MAR17000PE', 'id': 'NSE:NIFTY23MAR17000PE-BO', 'buyAvg': 100.55, 'buyQty': 50, 'buyVal': 5027.5, 'sellAvg': 90.4, 'sellQty': 50, 'sellVal': 4520, 'netAvg': 0, 'netQty': 0, 'side': 0, 'qty': 0, 'productType': 'BO', 'realized_profit': -507.49999999999955, 'crossCurrency': '', 'qtyMulti_com': 1, 'segment': '11', 'ltp': 144, 'fyToken': '101123032957271', 'exchange': '10', 'unrealized_profit': 0, 'dayBuyQty': 50, 'cfBuyQty': 0, 'daySellQty': 50, 'cfSellQty': 0, 'rbiRefRate': 1, 'pl': -507.49999999999955, 'slNo': 0, 'avgPrice': 0}, {'symbol': 'MCX:CRUDEOILM23APRFUT', 'id': 'MCX:CRUDEOILM23APRFUT-BO', 'buyAvg': 5658, 'buyQty': 2, 'buyVal': 113160, 'sellAvg': 5715, 'sellQty': 2, 'sellVal': 114300, 'netAvg': 0, 'netQty': 0, 'side': 0, 'qty': 0, 'productType': 'BO', 'realized_profit': 1140, 'crossCurrency': '', 'qtyMulti_com': 10, 'segment': '20', 'ltp': 5670, 'fyToken': '1120230419253938', 'exchange': '11', 'unrealized_profit': 0, 'dayBuyQty': 2, 'cfBuyQty': 0, 'daySellQty': 2, 'cfSellQty': 0, 'rbiRefRate': 1, 'pl': 1140, 'slNo': 0, 'avgPrice': 0}, {'symbol': 'NSE:APOLLOHOSP-EQ', 'id': 'NSE:APOLLOHOSP-EQ-BO', 'buyAvg': 4315, 'buyQty': 5, 'buyVal': 21575, 'sellAvg': 4302.38, 'sellQty': 5, 'sellVal': 21511.9, 'netAvg': 0, 'netQty': 0, 'side': 0, 'qty': 0, 'productType': 'BO', 'realized_profit': -63.099999999999454, 'crossCurrency': '', 'qtyMulti_com': 1, 'segment': '10', 'ltp': 4283.35, 'fyToken': '1010000000157', 'exchange': '10', 'unrealized_profit': 0, 'dayBuyQty': 5, 'cfBuyQty': 0, 'daySellQty': 5, 'cfSellQty': 0, 'rbiRefRate': 1, 'pl': -63.099999999999454, 'slNo': 0, 'avgPrice': 0}, {'symbol': 'NSE:NIFTY23MAR17100PE', 'id': 'NSE:NIFTY23MAR17100PE-BO', 'buyAvg': 133.26666666666665, 'buyQty': 150, 'buyVal': 19990, 'sellAvg': 124.4, 'sellQty': 150, 'sellVal': 18660, 'netAvg': 0, 'netQty': 0, 'side': 0, 'qty': 0, 'productType': 'BO', 'realized_profit': -1329.9999999999968, 'crossCurrency': '', 'qtyMulti_com': 1, 'segment': '11', 'ltp': 208.6, 'fyToken': '101123032953341', 'exchange': '10', 'unrealized_profit': 0, 'dayBuyQty': 150, 'cfBuyQty': 0, 'daySellQty': 150, 'cfSellQty': 0, 'rbiRefRate': 1, 'pl': -1329.9999999999968, 'slNo': 0, 'avgPrice': 0}, {'symbol': 'NSE:BANKNIFTY23MAR39700PE', 'id': 'NSE:BANKNIFTY23MAR39700PE-BO', 'buyAvg': 400, 'buyQty': 25, 'buyVal': 10000, 'sellAvg': 387, 'sellQty': 25, 'sellVal': 9675, 'netAvg': 0, 'netQty': 0, 'side': 0, 'qty': 0, 'productType': 'BO', 'realized_profit': -325, 'crossCurrency': '', 'qtyMulti_com': 1, 'segment': '11', 'ltp': 510.7, 'fyToken': '101123032952617', 'exchange': '10', 'unrealized_profit': 0, 'dayBuyQty': 25, 'cfBuyQty': 0, 'daySellQty': 25, 'cfSellQty': 0, 'rbiRefRate': 1, 'pl': -325, 'slNo': 0, 'avgPrice': 0}], 'overall': {'count_open': 0, 'count_total': 9, 'pl_realized': -3217.0999999999917, 'pl_total': -3217.0999999999917, 'pl_unrealized': 0}}     
# PS C:\algoTrading> 
# get Current price


# symbols = ["MCX:SILVERMIC23APRFUT"]
symbols = ["MCX:CRUDEOILM23APRFUT"]


def data_handling(symbol):
    date = datetime.today().strftime('%Y-%m-%d')
    hist_data = {"symbol":symbol,"resolution":"60","date_format":1,"range_from":date,"range_to":date,"cont_flag":"1"}
    srp = login.fyers.history(hist_data)
    # print(srp)
    hl_data = srp["candles"][0]
    high = hl_data[2] 
    low = hl_data[3]
    # print("High:",high,"  ","Low:",low)
    return high, low
    
def calculate_long_position_size(price):
    available_capital = get_available_funds() / 4
    quantity = 1
    risk_per_unit = price * 0.003
    max_capital_risk = available_capital * 0.003
    quantity = max_capital_risk / risk_per_unit

    return round(quantity)

def calculate_short_position_size(price):
    available_capital = get_available_funds() / 3
    quantity = 1
    risk_per_unit = price * 0.003
    max_capital_risk = available_capital * 0.003
    quantity = max_capital_risk / risk_per_unit

    return math.floor(quantity)
    
def get_available_funds():
    try:
        return login.fyers.funds()['fund_limit'][-1]['equityAmount']

    except:
        return 70000

# print(funds())
# {'symbol': 'MCX:CRUDEOILM23APRFUT', 'id': 'MCX:CRUDEOILM23APRFUT-BO', 'buyAvg': 5658, 'buyQty': 2, 'buyVal': 113160, 'sellAvg': 5715, 'sellQty': 2, 'sellVal': 114300, 'netAvg': 0, 'netQty': 0, 'side': 0, 'qty': 0, 'productType': 'BO', 'realized_profit': 1140, 'crossCurrency': '', 'qtyMulti_com': 10, 'segment': '20', 'ltp': 5642, 'fyToken': '1120230419253938', 'exchange': '11', 'unrealized_profit': 0, 'dayBuyQty': 2, 'cfBuyQty': 0, 'daySellQty': 2, 'cfSellQty': 0, 'rbiRefRate': 1, 'pl': 1140, 'slNo': 0, 'avgPrice': 0}
def positions():
    # {'count_open': 0, 'count_total': 8, 'pl_realized': 618.7500000000007, 'pl_total': 618.7500000000007, 'pl_unrealized': 0} 
#    print(login.fyers.positions()['netPositions'])
    
    MTM = int(login.fyers.positions()['overall']['pl_total'])
    engine = pyttsx3.init()

    # Get a list of available voices
    voices = engine.getProperty('voices')

    # Set the desired voice
    engine.setProperty('voice', voices[0].id)  # Index 1 is for the second voice in the list

    # Convert text to speech
    text =MTM
    engine.say(text)

    # Run the speech engine and wait for the text to be spoken
    engine.runAndWait()

positions()

def place_orders(symbol,h,l):
   
    df = {"symbols":symbol}
    var = login.fyers.quotes(df)["d"]
    ltp = var[0]["v"]['lp']
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Get a list of available voices
    voices = engine.getProperty('voices')

    # Set the desired voice
    engine.setProperty('voice', voices[0].id)  # Index 1 is for the second voice in the list

    # Convert text to speech
    text = ltp - 6028
    engine.say(text)

    # Run the speech engine and wait for the text to be spoken
    engine.runAndWait()
    
    LSL=round(h*.003)
    SSL=round(l*.003)
    LTR=round(h*.006)
    STR=round(l*.006)
    longWithBuffer=math.ceil(0.001 * h) + h
    shortWithBuffer= l - round(0.001 * l)  
    print(f"LTP:{ltp} Low:{l} High:{h} longwithbuff{longWithBuffer} shortbuff{shortWithBuffer}")

    global trades
    


    if (ltp >= longWithBuffer)  and (trades < 5):
        trades += 1
        # symbols.remove(symbol)                   
        print(f'LONG:{symbol} Signal@: {h} Signal with buffer:{shortWithBuffer} Entry@:{ltp} qty:{calculate_long_position_size(ltp)}')
        # data = {"symbol":symbol,"qty":calculate_long_position_size(ltp),"type":2,"side":1,"productType":"BO",
        # "limitPrice":0,"stopPrice":0,"validity":"DAY","disclosedQty":0,"offlineOrder":"False",  "stopLoss":LSL,"takeProfit":LTR}
        # response = login.fyers.place_order(data)
        # print(response)
        
    elif (ltp <= shortWithBuffer) and (trades < 5):
        trades += 1
        # symbols.remove(symbol)

        print(f'sorted:{symbol} Signal@: {l} Signal with buffer:{shortWithBuffer} Entry@:{ltp} qty:{calculate_short_position_size(ltp)}')
        # data = {"symbol":symbol,"qty":calculate_short_position_size(ltp),"type":2,"side":-1,"productType":"BO",
        # "limitPrice":0,"stopPrice":0,"validity":"DAY","disclosedQty":0,"offlineOrder":"False",  "stopLoss":SSL,"takeProfit":STR}
        
        # response = login.fyers.place_order(data)
        
        # print(response)
        
    
    else:
        pass


    
    
    ltp = var[0]
    
   
        
        
        
        
        
        
# response = login.fyers.gainers()
# print(response)
        
        
        
        
    
start = "09:44:00"    
end = "21:00:00"
now = datetime.strftime(datetime.now(),"%H:%M:%S")

# Check is it need to run a code in range of 9:40 - 3:30
run = True if ((now>start) & (now<end)) else False

# next line i aded back test
# run = True 


if run==False and now<start:
    x = True
    while x:
        # funds()
        print("Waiting for market to open")
        time.sleep(30)
        now = datetime.strftime(datetime.now(),"%H:%M:%S")
        x = True if now<start else False
    run = True
    

while run:
    print("\nCurrent time","   ",now)
    # for i in symbols:
    #     print("\n"+i)
    #     h,l= data_handling(i)
    #     place_orders(i,h,l)
    # print("after delete",symbols)
    time.sleep(10)
    positions()
    now = datetime.strftime(datetime.now(),"%H:%M:%S")
    run = True if ((now>start) & (now<end)) else False




if now>end:
    print("\nMarket Closed!")





# Initialize the text-to-speech engine
# engine = pyttsx3.init()

# # Get a list of available voices
# voices = engine.getProperty('voices')

# # Set the desired voice
# engine.setProperty('voice', voices[1].id)  # Index 1 is for the second voice in the list

# # Convert text to speech
# text = "ithu tamil pesuma yenna doubt ah irruke udhaya"
# engine.say(text)

# # Run the speech engine and wait for the text to be spoken
# engine.runAndWait()