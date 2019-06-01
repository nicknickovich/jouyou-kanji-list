"""
Parse html page (only kanji table part)
https://en.wikipedia.org/wiki/List_of_j%C5%8Dy%C5%8D_kanji
and organize it in a list of dictionaries
"""

import bs4,pprint

f1 = open("wikikanji.html", encoding="utf-8")
soup = bs4.BeautifulSoup(f1.read(), "html5lib")
elems = soup.select("tr td")
l_elems = len(elems)

kanjiData = []
count = 0

for i in range(0, l_elems, 9):
    kanjiData.append({})
    kanjiData[count].update({"#": elems[i].getText(),
                             "New": elems[i+1].getText()[0],
                             "Old": elems[i+2].getText(),
                             "Radical": elems[i+3].getText(),
                             "Strokes": elems[i+4].getText(),
                             "Grade": elems[i+5].getText(),
                             "Year added": elems[i+6].getText(),
                             "Meaning": elems[i+7].getText(),
                             "Reading": elems[i+8].getText().replace("\n", "")})
    count += 1

f2 = open("kanji.py", encoding="utf-8", mode="w")
f2.write("kanji_list = " + pprint.pformat(kanjiData))
f2.close()