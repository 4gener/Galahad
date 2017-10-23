import requests
from bs4 import BeautifulSoup
import time
import json

building = input('Please input the building number:')

with open('config.json', encoding='utf-8') as chart:
    load = json.load(chart)
    buildingNo = load[building]

page = requests.get('http://www.iskyct.com/www/Uwash/shopsearch/shopdetail.jsp?SHOP_CD={}'.format(str(buildingNo)))

soup = BeautifulSoup(page.text, 'html.parser')

machines = soup('div', 'index_list2_con')

for machineType in machines:

    print(machineType('h2')[0].string)

    for machine in machineType('dl'):
        number = machine('b')[0].string
        status = machine.attrs['class'][0]

        print(number + "Machine", status)
        if status == 'free':
            free = True
            print('Lucky for you!')
        elif status == 'offline':
            pass
        else:
            ETF = machine.span.get_text().split('\n')[1]
            print('Estimated time of finish:', ETF)

    print()

print('Last checked time:', end=' ')
print(time.strftime("%H:%M:%S", time.localtime()))
