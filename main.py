import os
from threading import Thread
import makePost
from random import randint

project_dir = str(randint(0, 99999999))
print(project_dir)
os.system(f"mkdir sites\\{project_dir}")
os.system(f"mkdir sites\\{project_dir}\\posts")

for i in range(3):
    Thread(target=makePost.makePost, args=("Статья", 6, 2, f"{os.getcwd()}\\sites\\{project_dir}\\")).start()

with open(f"{os.getcwd()}\\sites\\{project_dir}\\site.html", "w+") as siten:
    site = "<h1>СТАТЬИ СЕГОДНЯ</h1>\n"
    files = os.listdir(f"{os.getcwd()}\\sites\\{project_dir}\\posts")
    for file in files:
        site += f'<a href="{os.getcwd()}\\sites\\{project_dir}\\posts\\{file}">{file.replace(".html", "")}</a><br>\n'
    siten.write(site)

