from session import SESSION
import re

def Ranking():
    se = SESSION()
    r = se.get(, False)
    li = re.findall(r'<a href=\"/artworks/([\s\S]+?)\"class=',r)
    return len(li)

if __name__ == "__main__":
    print(Ranking())