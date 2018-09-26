# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
import time
from bs4 import BeautifulSoup

MP = "https://us.battle.net/forums/en/overwatch/"
GD = "https://us.battle.net/forums/en/overwatch/22813879/"
GDPG = "https://us.battle.net/forums/en/overwatch/22813879/?page="
TH = "/forums/en/overwatch/topic/"
DM = "https://us.battle.net"

SLEEP_INTERVAL=.5

#GD seems to be capped at 9999 but has launch day threads
#launch day? May 24, 2016 

#threads in each subforum may link to each other, be careful of dupes
    
def getThreads(page_url): #returns list now
    r = requests.get(page_url)
    
    soup = BeautifulSoup(r.content, features="html5lib")
    
    threadlinks = {}
    for link in soup.find_all('a'):
        l=link.get('href')
        if l is not None and (l[:len(TH)]) == TH:
            threadlinks[l] = DM+l[: len(TH) + 11 ]
            #print (l[ len(TH) : len(TH) + 11 ])
    
    retval = []
    for l in threadlinks.values():
        retval.append(l)         
            
    return (retval)
    
if __name__ == "__main__":
    
    f = open("urls", "w")
    
    urllists = []
    for pagenum in range(1,10000):
        urllists.append(getThreads(GDPG+str(pagenum))) 
        time.sleep(SLEEP_INTERVAL)
        break # remove when ready to run on the entire GD 
    
    
    for urllist in urllists:
        for urls in urllist:
            f.write(urls)
            
    f.close()