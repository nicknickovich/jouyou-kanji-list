# kanji_all is a list of all jouyou kanji
from kanji_all import kanji_list
import requests, bs4, pprint, json

kanji_w_readings = {}
l = len(kanji_list)
count = 0
while count < l:
    item = kanji_list[count]
    url = "https://jisho.org/search/" + item + "%20%23kanji"
    print("Downloading page # %s..." % count)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html5lib") # you need to install html5lib
                                                   # or change it to html.parser

    # this gives a list of html elements of this class:
    s = soup.select("dd.kanji-details__main-readings-list")
    try:
        # in jisho kun reading goes first
        # sometimes there is no on or kun reading
        # more often then not there is no kun reading
        on_yomi = s[1].select("a")
        kun_yomi = s[0].select("a")
    except:
        on_yomi = s[0].select("a")
        kun_yomi = []
    
    meanings = soup.select("div.kanji-details__main-meanings")
    meanings_list = meanings[0].string.strip().split(", ")

    # sometimes for kokuji there is no on reading
    if "(kokuji)" in meanings_list and on_yomi == s[0].select("a"):
        kun_yomi = on_yomi
        on_yomi = []
    
    # creating nested dictionaries
    kanji_w_readings.update({item: {}})
    kanji_w_readings[item].update({"kun": []})
    kanji_w_readings[item].update({"on": []})
    kanji_w_readings[item].update({"meanings": []})

    for kun in kun_yomi:
        kanji_w_readings[item]["kun"].append(kun.string)
    for on in on_yomi:
        kanji_w_readings[item]["on"].append(on.string)
    for meaning in meanings_list:
        kanji_w_readings[item]["meanings"].append(meaning)
    
    count += 1

# write in a .py file to import to python scripts
f = open("readings_jisho.py", mode="w", encoding="utf-8")
f.write("kanji_dict = " + pprint.pformat(kanji_w_readings))
f.close()

# write in a .json file
f = open("readings_jisho.json", encoding="utf-8", mode="w")
json.dump(kanji_w_readings, f, indent=2, ensure_ascii=False, separators=(", ", ": "))
f.close()

print("Done.")