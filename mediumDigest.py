
"""
Created on  Feb 5 2018

@author: Chime Njoku
"""

# mediumDigest.py - Opens random articles in a particular medium category


import requests, webbrowser, bs4,random




def main():
    topic = input("TOPICS:   popular   technology   self   culture   web-development...\nWhat topic on medium are you interested in? " )
    num_articles = int(input("How many articles do want to read?(1-10) "))
    if (topic and (num_articles > 0)) :
        print('Running...') # display text while downloading the medium page
        
        res = requests.get('https://medium.com/topic/' + topic)
        res.raise_for_status()
        
        soup = bs4.BeautifulSoup(res.text,"html.parser")
        linkElems = soup.select('div.u-flex0.u-sizeFullWidth a')
        
        numOpen=random.sample(linkElems,num_articles)
        for i in range(num_articles):  
            webbrowser.open(numOpen[i].get('href'))
    elif not topic:
        # User enters empty string for topic
        print("Error: Enter a topic!")
    else:
        # User enters less than 1 for number of articles. 
        print("Error: Minimum number of articles is 1!")   
         
if __name__ == "__main__":
    main()
    
