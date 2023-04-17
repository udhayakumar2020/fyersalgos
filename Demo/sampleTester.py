# import math

# def buffer_price(equity_price):
#     buffer = 0.001  # 0.1% buffer
#     buffer_price = equity_price * (1 + buffer)
#     buffer_price_rounded = round(buffer_price + 0.0005, 3)
#     buffer_price_rounded = buffer_price_rounded - equity_price
#     buffer_price_divisible = round(buffer_price_rounded * 20) / 20
#     return buffer_price_divisible

# # def buffer_price(equity_price):
# #     buffer = 0.001  # 0.1% buffer
# #     buffer_price = equity_price * (1 + buffer)
# #     buffer_price_rounded = math.ceil(buffer_price * 20) / 20
# #     return buffer_price_rounded


# # def buffer_price(equity_price):
# #     buffer = 0.001  # 0.1% buffer
# #     buffer_price = equity_price * (1 + buffer)
# #     print(buffer_price)
# #     buffer_price_rounded = math.ceil(buffer_price * 20) / 20 
# #     buffer_price_rounded = buffer_price_rounded - equity_price
# #     return buffer_price_rounded

# price = 109004.8767 # current equity price
# buffered_price = buffer_price(price)
# print("Current Price:", price)
# print("Buffered Price:", buffered_price)

# import winsound
# duration = 1000  # milliseconds
# freq = 100  # Hz
# winsound.Beep(freq, duration)


# def beep():
#     print('\a')
# import winsound
# winsound.Beep(600, 1000)


import winsound
# winsound.MessageBeep()

# import subprocess
# subprocess.call(['speech-dispatcher'])        #start speech dispatcher
# subprocess.call(['spd-say', '"your process has finished"'])


# import sys
# print('\a')
# sys.stdout.flush()

# import time
# time.sleep(10)   #Set the time
# for x in range(60):  
#     time.sleep(1)
#     print('\a')
    

# import winsound
# import playsound    
# text2speech = gTTS("Your course "   " is downloaded to " ". Check it fast.")
# text2speech.save("temp.mp3")
# winsound.Beep(2500, 1000)
# playsound("temp.mp3")


# import subprocess

# subprocess.call(['D:\greensoft\TTPlayer\TTPlayer.exe', "E:\stridevampaclip.mp3"])

# import os
# os.system('C:/Users/Udhaya/Downloads/Adada-Vaa.mp3')


import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the rate of speech
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)

# Set the volume
volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)

variabless='RELIANCE'
# Convert text to speech
text = "Sonna purunjuku nalaiku pathukalam kumare "+variabless +"with price 2018.45 SL with 2029.95 "
engine.say(text)

# Run the speech engine and wait for the text to be spoken
engine.runAndWait()


import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Get a list of available voices
voices = engine.getProperty('voices')

# Set the desired voice
engine.setProperty('voice', voices[1].id)  # Index 1 is for the second voice in the list

# Convert text to speech
text = "ithu tamil pesuma yenna doubt ah irruke udhaya"
engine.say(text)

# Run the speech engine and wait for the text to be spoken
engine.runAndWait()




# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# # Load the price data
# prices = pd.read_csv('equity_prices.csv')

# # Define the box size
# box_size = 0.02

# # Calculate the highs and lows of the Darvas Boxes
# highs = prices['High'].rolling(window=int(box_size*len(prices)), min_periods=1).max()
# lows = prices['Low'].rolling(window=int(box_size*len(prices)), min_periods=1).min()

# # Identify the upper and lower bounds of the boxes
# upper_bounds = highs.shift(1)
# lower_bounds = lows.shift(1)

# # Detect box breakouts
# long_signals = prices['Close'] > upper_bounds
# short_signals = prices['Close'] < lower_bounds

# # Plot the prices and the boxes
# plt.plot(prices['Close'], label='Price')
# plt.plot(upper_bounds, label='Upper Bound')
# plt.plot(lower_bounds, label='Lower Bound')
# plt.legend()
# plt.show()

# # Print the signals
# print('Long Signals:')
# print(long_signals[long_signals == True])
# print('Short Signals:')
# print(short_signals[short_signals == True])
# In this code, we use a rolling window to calculate the highs and lows of the Darvas Boxes based on the box size parameter. We then use these highs and lows to determine the upper and lower bounds of the boxes, and finally, we identify long and short signals based on whether the price has broken out above the upper bound or below the lower bound. The signals are then printed for further analysis.

# Note that this is just a sample code and there are many ways to modify and optimize this algorithm based on your trading goals and preferences. Also, remember to thoroughly test your algorithm before using it in live trading.