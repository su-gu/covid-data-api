from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests 
from bs4 import BeautifulSoup 


@csrf_exempt
def getStateWiseReport():
    URL = "https://www.mohfw.gov.in/"
    r = requests.get(URL) 
    
    soup = BeautifulSoup(r.content, 'lxml')
    mydivs = soup.find_all("div", {"class": "table-responsive"})
    states = BeautifulSoup(str(mydivs[-1]), 'lxml')
    states = states.find_all("tr")
    stateWiseData = {}
    for state in range(1,33):
        stateName=str(states[state].find_all("td")[1])[(str(states[state].find_all("td")[1]).index('>'))+1:-5]
        confirmed=str(states[state].find_all("td")[2])[(str(states[state].find_all("td")[2]).index('>'))+1:-5]
        cured=str(states[state].find_all("td")[3])[(str(states[state].find_all("td")[3]).index('>'))+1:-5]
        death=str(states[state].find_all("td")[4])[(str(states[state].find_all("td")[4]).index('>'))+1:-5]
        stateWiseData[state]={"State":stateName,"confirmed":confirmed,"cured":cured,"death":death}
    return stateWiseData
