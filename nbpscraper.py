import requests
from bs4 import BeautifulSoup
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

url = "https://stooq.pl/t/?i=510"

indexes = ["nz50","dax","ndx","spx"]
ids = ["c2","m1"]

while True:
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    indeksy_tabela = soup.select("table.fth1").pop(0)

    prices = {}
    percents = {}

    for curr in indexes:
        prices[curr] = []
        percents[curr] = []
        for idc in ids:
            if idc == "c2":
                try:
                    prices[curr].append(indeksy_tabela.find(id='aq_^'+curr+'_'+idc).text)
                except AttributeError:
                    prices[curr].append("nan")
            else: 
                try:
                    percents[curr].append(indeksy_tabela.find(id='aq_^'+curr+'_'+idc).text)
                except AttributeError:
                    percents[curr].append("nan")

    #for key,value in prices.items():
        #print(value)
    time.sleep(0.1)

    if len(prices) == 2 and len(percents) ==2:
        break
print(prices)

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def charts(i):

    ax1.clear()

    for key,value in prices.items():
        series = list(map(float,value))
        ax1.plot(range(len(series)), series)
        

ani = animation.FuncAnimation(fig, charts, interval=1000)
plt.show()
