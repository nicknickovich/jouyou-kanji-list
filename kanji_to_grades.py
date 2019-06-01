from kanji import kanji_list
import pprint

grade_1 = []
grade_2 = []
grade_3 = []
grade_4 = []
grade_5 = []
grade_6 = []
grade_s = []
grades = [grade_1, grade_2, grade_3, grade_4, grade_5, grade_6]

kanji_all = []

for kanji in kanji_list:
    try:
        g = int(kanji["Grade"])
        grades[g-1].append(kanji["New"])
    except:
        grade_s.append(kanji["New"])

for kanji in kanji_list:
    kanji_all.append(kanji["New"][0])


f = open("kanji_grades.py", encoding="utf-8", mode="w")
for i in range(1, 7):
    f.write("grade_" + str(i) + " = " + pprint.pformat(grades[i-1]) + "\n")
f.write("grade_s" + pprint.pformat(grade_s))
f.close()