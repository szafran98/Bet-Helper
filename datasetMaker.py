from bs4 import BeautifulSoup
import time
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import sqlite3

urlList = ["https://www.livescore.in/pl/anglia/premier-league/tabela/", "https://www.livescore.in/pl/anglia/championship/tabela/", "https://www.livescore.in/pl/belgia/jupiler-league/tabela/", "https://www.livescore.in/pl/francja/ligue-1/tabela/", "https://www.livescore.in/pl/hiszpania/laliga/tabela/", "https://www.livescore.in/pl/holandia/eredivisie/tabela/", "https://www.livescore.in/pl/niemcy/bundesliga/tabela/"]
listaZup = []
bazaLinkow = []
driver = webdriver.Chrome(ChromeDriverManager().install())
for url in urlList:
    driver.get(url)
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    listaDruzyn = soup.find_all("span", {"class" : "team_name_span"})
    for team in listaDruzyn:
        link = team.a['onclick']
        wycietyLink = re.findall(r"'.+?'",link)
        wycietyLink = str(wycietyLink[0])
        bazaLinkow.append(wycietyLink[1:-1] + "wyniki/")

ostatnieSpotkania = {}
driver = webdriver.Chrome(ChromeDriverManager().install())
for link in bazaLinkow:
    driver.get("https://www.livescore.in" + link)
    time.sleep(1)
    soupTeam = BeautifulSoup(driver.page_source, "html.parser")
    spotkaniaDruzyny = soupTeam.find_all("div", {"class" : "event__match"})
    teamName = soupTeam.find("div", {"class" : "teamHeader__name"}).text
    temp = []
    for spotkanie in spotkaniaDruzyny:
        druzyny = spotkanie.find_all("div", {"class": "event__participant"})
        gospodarz = druzyny[0].text
        gosc = druzyny[1].text
        if gospodarz == teamName.strip():
            temp.append(spotkanie.find_all("span")[0].text)
        else:
            temp.append(spotkanie.find_all("span")[1].text)
    ostatnieSpotkania.update( {teamName.strip() : temp} )

conn=sqlite3.connect("teams.db")
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS teams (id INTEGER PRIMARY KEY, name text, goals text)")
conn.commit()

id = 0
for key in ostatnieSpotkania:
    cur.execute("INSERT INTO teams VALUES (?, ?,?)",[id, str(key), str(ostatnieSpotkania[key])])
    id += 1

conn.commit()
conn.close()