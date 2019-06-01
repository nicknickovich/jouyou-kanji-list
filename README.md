# jouyou-kanji-list
List of all jouyou kanji with readings and meanings from jisho.org

Files in this repository:
1. wikikanji.html - html table from https://en.wikipedia.org/wiki/List_of_j%C5%8Dy%C5%8D_kanji
2. kanji.py - parsed table from the wiki page organized in a list of dictionaries. Really ugly, not usable for readings, but usable for number of strokes, grades, main radical, etc.
3. pars.py - script used for parsing wikipedia page.
4. kanji_all.py - a list of all jouyou kanji (only kanji).
5. kanji_grades.py - joyou kanji organized by grade.
6. kanji_to_grades.py - script used to make kanji_grades.py.
**7. readings_jisho.py - all jouyou kanji with readings and meanings from jisho.org**
**8. readings_jisho.json - the same file in json format**
9. from_jisho.py - script used to make files readings_jisho.py and readings_jisho.json
**10. readings_jisho.xlsx - jouyou kanji with readings and meanings in a form of excel table**
11. readings_jisho_to_ex.py - script used to make readings_jisho.xlsx
