import requests
from bs4 import BeautifulSoup
import time
import pync

while (True):

    page = requests.get('http://www.iskyct.com/www/Uwash/shopsearch/shopdetail.jsp?SHOP_CD=617')

    soup = BeautifulSoup(page.text, 'html.parser')

    machines = soup('dl')

    free = False

    for machine in machines[-3:]:
        number = machine('b')[0].string
        status = machine.attrs['class'][0]

        print(number + "Machine", status)
        if status == 'free':
            free = True
            print('Lucky for you! Go get the damn machine!')
        else:
            ETF = machine.span.get_text().split('\n')[1]
            print('Estimated time of finish:', ETF)

    print('Last checked time:', end=' ')
    print(time.strftime("%H:%M:%S", time.localtime()))

    if free:
        pync.Notifier.notify('GOOOOOOOOO!')
        print('\a')
        exit(0)

    time.sleep(15)
