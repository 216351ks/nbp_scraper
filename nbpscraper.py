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
                    prices[curr].append("N/A")
            else: 
                try:
                    percents[curr].append(indeksy_tabela.find(id='aq_^'+curr+'_'+idc).text)
                except AttributeError:
                    percents[curr].append("N/A")

    #for key,value in prices.items():
        #print(value)
    time.sleep(5)

    if len(prices) == 15: 
        break
    elif len(percents) ==15: 
        break 

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animation(i):

    xs= []
    ys= []

    for key,value in prices.items():
        ys.append(float(" ".join(value)))

    for _ in ys: 
        x = 1
        xs.append(x)
        x+=1

    ax1.clear()
    ax1.plot(xs,ys)

ani = animation.FuncAnimation(fig, animation, interval=1000)
plt.show()
