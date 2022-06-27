import datetime as dt
from distutils.util import execute
from binance.client import Client
import time
import tkinter
import requests
import pandas as pd

root = tkinter.Tk()
root.title('TestBot')
root.geometry("700x1000")


input1 = tkinter.Label(root, text="API Key")
input1.pack()

el=tkinter.Entry(root, show="*")
el.pack()

input2 = tkinter.Label(root, text="API SECRET")
input2.pack()

el2=tkinter.Entry(root, show="*")
el2.pack()

input3 = tkinter.Label(root, text="Moving Average Fast (ex, 12)")
input3.pack()

el3=tkinter.Entry(root)
el3.pack()

input4 = tkinter.Label(root, text="Moving Average Slow (ex, 26)")
input4.pack()

el4=tkinter.Entry(root)
el4.pack()

input5 = tkinter.Label(root, text="Signal Line (ex, 9)")
input5.pack()

el5=tkinter.Entry(root)
el5.pack()

input6 = tkinter.Label(root, text="Symbol (ex, BTCUSDT)")
input6.pack()

el6=tkinter.Entry(root)
el6.pack()

input7 = tkinter.Label(root, text="Leverage (ex, 2)")
input7.pack()

el7=tkinter.Entry(root)
el7.pack()

input8 = tkinter.Label(root, text="Time Interval (ex, 5)")
input8.pack()

el8=tkinter.Entry(root)
el8.pack()

input9 = tkinter.Label(root, text="Order amount in USDT (ex, 100)(Leave empty if not used")
input9.pack()

el9=tkinter.Entry(root)
el9.pack()

input10 = tkinter.Label(root, text="Order amount in % (ex, 10)(Leave empty if not used")
input10.pack()

el10=tkinter.Entry(root)
el10.pack()

input11 = tkinter.Label(root, text="Loss Cut Rate % (ex, 10)")
input11.pack()

el11=tkinter.Entry(root)
el11.pack()


input12 = tkinter.Label(root, text="Order Entry Value(ex, 10)")
input12.pack()

el12=tkinter.Entry(root)
el12.pack()

input13 = tkinter.Label(root, text="Profit Take % (ex, 10)")
input13.pack()

el13=tkinter.Entry(root)
el13.pack()

input14 = tkinter.Label(root, text="Profit Take 1 in % (ex, 10)")
input14.pack()

el14=tkinter.Entry(root)
el14.pack()

input15 = tkinter.Label(root, text="Profit Take Stop 1 in % (ex, 10)")
input15.pack()

el15=tkinter.Entry(root)
el15.pack()

input16 = tkinter.Label(root, text="Profit Take 2 in % (ex, 10)")
input16.pack()

el16=tkinter.Entry(root)
el16.pack()

input17 = tkinter.Label(root, text="Profit Take Stop 2 in % (ex, 10)")
input17.pack()

el17=tkinter.Entry(root)
el17.pack()

orderlist=[]

now=dt.datetime.now

ptest1=0

def tick():
    try:
        if not doTick:
            return
        global ptest1
        global execute
        global roeslist

        api_key=str(el.get())
        api_secret=str(el2.get())
        short=int(el3.get())
        long=int(el4.get())
        signal=int(el5.get())
        symbol=str(el6.get())
        leverage=int(el7.get())
        timeinterval=str(el8.get())
        buyd=float(el12.get())

        client=Client(api_key=api_key, api_secret=api_secret, testnet=False)

        try:
            absOrderAmount=float(el9.get())
        except:
            absOrderAmount=0
        


























































































































root.mainloop()