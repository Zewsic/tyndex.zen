from random import randint
from balaboba import balaboba

def makePost(text=str(randint(1, 4999999)), style=randint(0, 12), count=1, project_dir="", postId=0):
    with open(project_dir + f"posts\\{postId}.html", "w+") as fil:
        fil.write(balaboba(text, style, count))
    print(str(postId) + " - READY!")
