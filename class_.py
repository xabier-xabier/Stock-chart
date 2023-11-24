import requests
from pprint import pprint
import matplotlib.pyplot as plt
from datetime import date
import numpy as np


class Stock():

    def check_code(company):
        if company=="IBM":
            code="IBM"
        elif company=="Apple":
            code="AAPL"
        elif company=="Amazon":
            code="AMZN"
        elif company=="Tesla":
            code="TSLA"
        elif company=="Microsoft":
            code="MSFT"
        elif company=="Alphabet":
            code="GOOGL"
        elif company=="Nvidia":
            code="NVDA"
        elif company=="Meta platforms":
            code="META"
        elif company=="Berkshire Hathaway":
            code="BRK-A"
        elif company=="Eli Lilly":
            code="LLY"
        elif company=="Visa":
            code="V"
        elif company=="United Health":
            code="UNH"
        elif company=="JP Morgan Chase":
            code="AMJ"
        elif company=="Walmart":
            code="WMT"
        elif company=="Exxon Mobil":
            code="XOM"
        elif company=="Broadcom":
            code="AVGO"
        elif company=="Mastercard":
            code="MA"
        else:
            code="JNJ"

        return code


    def daily(symbol):
        #I need to get my api key, this is a demo
        base_url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey="        #Enter your API
        #base_url="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"      #solo 25 llamadas al dia
        response=requests.get(base_url)
        resp_lan=response.json()
        return resp_lan
    
    def weekly(symbol):
        #I need to get my api key, this is a demo
        base_url=f"https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={symbol}&apikey="
        #base_url="https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=IBM&apikey=demo"      #solo 25 llamadas al dia
        response=requests.get(base_url)
        resp_lan=response.json()
        return resp_lan
    
    def monthly(symbol):
        #I need to get my api key, this is a demo
        base_url=f"https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={symbol}&apikey="
        #base_url="https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=IBM&apikey=demo"      #solo 25 llamadas al dia
        response=requests.get(base_url)
        resp_lan=response.json()
        return resp_lan
    
    def new_date(date,x):
        new_date=[]
        new_date.append(date)
        date_split=date.split("-")

        while x!=0:
            if int(date_split[1])>10:
                if int(date_split[2])>10:
                    date_num=int(date_split[2])-1
                    new_date1=str(date_split[0])+str("-")+str(date_split[1])+str("-")+str(date_num)
                    new_date.append(new_date1)
                    date=new_date1
                    date_split=date.split("-")
                    x-=1

                elif int(date_split[2])==1:
                    date_num=int(date_split[1])-1
                    new_date1=str(date_split[0])+str("-")+str(date_num)+str("-31")
                    new_date.append(new_date1)
                    date=new_date1
                    date_split=date.split("-")
                    x-=1

                elif int(date_split[2])<=10 and int(date_split[2])!=1:
                    date_num=int(date_split[2])-1
                    new_date1=str(date_split[0])+str("-")+str(date_split[1])+str("-0")+str(date_num)
                    new_date.append(new_date1)
                    date=new_date1
                    date_split=date.split("-")
                    x-=1

            elif int(date_split[1])==1:
                if int(date_split[2])>10:
                    date_num=int(date_split[2])-1
                    new_date1=str(date_split[0])+str("-")+str(date_split[1])+str("-")+str(date_num)
                    new_date.append(new_date1)
                    date=new_date1
                    date_split=date.split("-")
                    x-=1

                elif int(date_split[2])==1:
                    date_num=int(date_split[0])-1
                    new_date1=str(date_num)+str("-")+str("12")+str("-31")
                    new_date.append(new_date1)
                    date=new_date1
                    date_split=date.split("-")
                    x-=1

                elif int(date_split[2])<=10 and int(date_split[2])!=1:
                    date_num=int(date_split[2])-1
                    new_date1=str(date_split[0])+str("-")+str(date_split[1])+str("-0")+str(date_num)
                    new_date.append(new_date1)
                    date=new_date1
                    date_split=date.split("-")
                    x-=1

            elif int(date_split[1])<=10 and int(date_split[1])!=1:
                if int(date_split[2])>10:
                    date_num=int(date_split[2])-1
                    new_date1=str(date_split[0])+str("-")+str(date_split[1])+str("-")+str(date_num)
                    new_date.append(new_date1)
                    date=new_date1
                    date_split=date.split("-")
                    x-=1

                elif int(date_split[2])==1:
                    date_num=int(date_split[1])-1
                    new_date1=str(date_split[0])+str("-0")+str(date_num)+str("-31")
                    new_date.append(new_date1)
                    date=new_date1
                    date_split=date.split("-")
                    x-=1

                elif int(date_split[2])<=10 and int(date_split[2])!=1:
                    date_num=int(date_split[2])-1
                    new_date1=str(date_split[0])+str("-")+str(date_split[1])+str("-0")+str(date_num)
                    new_date.append(new_date1)
                    date=new_date1
                    date_split=date.split("-")
                    x-=1


        return new_date
    
    def check_date(resp_lan,new_date):
        open=[]
        close=[]
        high=[]
        low=[]
        volume=[]
        final_date=[]

        for i in new_date:
            try:
                
                #resp_lan["Time Series (Daily)"][i]
                open.append(float(resp_lan["Time Series (Daily)"][i]["1. open"]))
                high.append(float(resp_lan["Time Series (Daily)"][i]["2. high"]))
                low.append(float(resp_lan["Time Series (Daily)"][i]["3. low"]))
                close.append(float(resp_lan["Time Series (Daily)"][i]["4. close"]))
                volume.append(float(resp_lan["Time Series (Daily)"][i]["5. volume"]))
                final_date.append(i)
            
            except KeyError:
                pass

        open.reverse()
        high.reverse()
        low.reverse()
        close.reverse()
        volume.reverse()

        return open,close,high,low,volume,final_date
    
    def check_date_weekly(resp_lan,new_date):
        open=[]
        close=[]
        high=[]
        low=[]
        volume=[]
        final_date=[]

        for i in new_date:
            try:
                
                #resp_lan["Time Series (Daily)"][i]
                open.append(float(resp_lan["Weekly Time Series"][i]["1. open"]))
                high.append(float(resp_lan["Weekly Time Series"][i]["2. high"]))
                low.append(float(resp_lan["Weekly Time Series"][i]["3. low"]))
                close.append(float(resp_lan["Weekly Time Series"][i]["4. close"]))
                volume.append(float(resp_lan["Weekly Time Series"][i]["5. volume"]))
                final_date.append(i)
            
            except KeyError:
                pass

        open.reverse()
        high.reverse()
        low.reverse()
        close.reverse()
        volume.reverse()

        return open,close,high,low,volume,final_date
    
    def check_date_monthly(resp_lan,new_date):
        open=[]
        close=[]
        high=[]
        low=[]
        volume=[]
        final_date=[]

        for i in new_date:
            try:
                
                #resp_lan["Time Series (Daily)"][i]
                open.append(float(resp_lan["Monthly Time Series"][i]["1. open"]))
                high.append(float(resp_lan["Monthly Time Series"][i]["2. high"]))
                low.append(float(resp_lan["Monthly Time Series"][i]["3. low"]))
                close.append(float(resp_lan["Monthly Time Series"][i]["4. close"]))
                volume.append(float(resp_lan["Monthly Time Series"][i]["5. volume"]))
                final_date.append(i)
            
            except KeyError:
                pass

        open.reverse()
        high.reverse()
        low.reverse()
        close.reverse()
        volume.reverse()

        return open,close,high,low,volume,final_date
    
    def plot_graph1(open,close,high,low, new_date,ma,company):
        width = 0.15 
        N=0
        color=[]
        t=[]
        dif=[]
        new_date.reverse()
        for i in open:
            N+=1

        ind = np.arange(N)  
        for i in range(0,N,1):
            t.append(new_date[i])     #Esto es para las T1, T2, poder nombrarlos
            dif_=high[i]-low[i]
            dif.append(dif_)
            if i==0:
                color.append("green")

            else:
                if close[i]>close[i-1]:
                    color.append("green")
                    #color[i]="green"
                else:
                    color.append("red")
                    #color[i]="red"

        fig, ax = plt.subplots()

        ax.bar(t,dif, width, bottom=low, color=color)

        ax.set_ylabel('Stock value $')
        ax.set_title(f"Stock chart of {company}")
        ax.legend(title='Stock value $')

        plt.plot(t, ma, color="lightgrey")

        plt.show()

        return t
    

    def plot_volume(t,volume,ma ,company):
        width=0.4
        fig, ax = plt.subplots()

        ax.bar(t,volume, width, color="blue")

        ax.set_ylabel('Volume')
        ax.set_title(f'Volume in time {company}')
        ax.legend(title='Volume $')

        plt.plot(t, ma, color="orange")
        plt.show()


    def MA_calculus(close):

        MA=[]
        sum=0
        n=0
        for i in close:
            sum+=i
            n+=1
            calculus=(sum/n)
            MA.append(calculus)

        return MA
    
    def plot_all(open,close,high,low, new_date,ma,volume,ma_v,company):
        width = 0.15 
        N=0
        color=[]
        t=[]
        dif=[]
        for i in open:
            N+=1

        ind = np.arange(N)  
        for i in range(0,N,1):
            t.append(new_date[i])     #Esto es para las T1, T2, poder nombrarlos
            dif_=high[i]-low[i]
            dif.append(dif_)
            if i==0:
                color.append("green")

            else:
                if close[i]>close[i-1]:
                    color.append("green")
                    #color[i]="green"
                else:
                    color.append("red")
                    #color[i]="red"

        fig, ax = plt.subplots(2)

        ax[0].bar(t,dif, width, bottom=low, color=color)

        ax[0].set_ylabel('Stock value $')
        ax[0].set_title(f'Stock value of {company}')
        ax[0].legend(title='Stock value')
        ax[0].plot(t,ma, color="lightgrey")
        #plt.plot(t, ma)

        ax[1].bar(t,volume, width, color="blue")

        ax[1].set_ylabel('Volume $')
        ax[1].set_title('Volume in time')
        ax[1].legend(title='Volume $')
        ax[1].plot(t,ma_v, color="orange")
        #plt.plot(t, ma_v)

        plt.show()

class Time():

    def current_date():
        today=date.today()
        return today