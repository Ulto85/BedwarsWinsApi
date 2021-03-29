import requests
from bs4 import BeautifulSoup
class MinceCraft():
    def __init__(self):
        pass
    def get_solo_wins(self,player):
        url = 'https://plancke.io/hypixel/player/stats/'+player+'#BedWars'
        page = requests.get(url)
        supper = BeautifulSoup(page.content,'html.parser')
        try:
            n = supper.find_all('table')[1].find_all('tr')[2].find_all('td')[6].get_text()
        except:
            n = supper.find_all('table')[2].find_all('tr')[2].find_all('td')[6].get_text()
        return n
minecraft = MinceCraft()
