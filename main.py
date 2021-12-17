import json
import os
import sys
import time
from threading import Thread
import makePost
from random import randint

from balaboba import balaboba

'''
themes = ["IT", "APPLE",
          "Xiaomi", "Удифительные факты", "Гайды на все случаи жизни",
          "Охота и рыбалка", "ВКонтакте", "Игромания", "Google"]
themes_new = []
a = 0
for thm in themes:
    print(">>> " + thm)
    themes_new.append({"name":thm, "subthemes":[]})
    for i in range(25):
        sb = balaboba(thm, 2)
        print(sb)
        themes_new[a]["subthemes"].append(sb)
    a += 1
print(json.dumps(themes_new, ensure_ascii=False))

sys.exit(0)
'''

print("ZenGen by Zewsic")

project_dir = str(randint(0, 99999999))

print("ID проекта: "+ project_dir)

time.sleep(3)
os.system(f"mkdir sites\\{project_dir}")
os.system(f"mkdir sites\\{project_dir}\\posts")

with open(f"{os.getcwd()}\\themes.json", "r+") as jsooo: themes = json.loads(jsooo.read())

print("Генерация статей начата...")

with open(f"{os.getcwd()}\\sites\\{project_dir}\\site.html", "w+") as siten:
    site = "<h1>СРОЧНЫЕ НОВОСТИ</h1>\n"

    for i in range(25):
        postId = i
        cat = themes[randint(0, len(themes)-1)]
        name = cat["subthemes"][randint(0, len(cat["subthemes"])-1)]

        thr = Thread(target=makePost.makePost, args=(f"{name}", 6, 15, f"{os.getcwd()}\\sites\\{project_dir}\\", postId)).start()
        site += f'<a href="\\posts\\{postId}.html">{name}</a><br>\n'
    siten.write(site)

