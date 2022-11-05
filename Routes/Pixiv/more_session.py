import threading
from Lib.Network import Network as SESSION
import json
import random

header = {
    "Host": "www.pixiv.net",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 Edg/96.0.1054.53",
}


class SEThread(threading.Thread):
    def __init__(self, pid):
        super(SEThread, self).__init__()  # 重构run函数必须要写
        self.fin = ""
        self.pid = pid

    def run(self):
        self.session = SESSION({
            "www.pixiv.net": {
                "ip": "210.140.92.187"
            }})
        url = "https://www.pixiv.net/ajax/illust/{}".format(str(self.pid))
        r = self.session.get(url, headers=header)
        r = r.text.replace("i.pximg.net", "i.pixiv.re")
        r = json.loads(r)
        bookmarkCount = r["body"]["bookmarkCount"]
        viewCount = r["body"]["viewCount"]
        if bookmarkCount >= 5000 or viewCount >= 10000 or bookmarkCount/viewCount >= 0.22:
            self.fin = r
        else:
            self.fin = False


def fast_2_get(li: list):
    try:
        while True:
            i = random.choice(li)
            li.remove(i)
            i2 = random.choice(li)
            li.remove(i2)
            se = SEThread(i["id"])
            se2 = SEThread(i2["id"])
            se.start()
            se2.start()
            while True:
                if se.fin != "":
                    break
                if se2.fin != "":
                    break
            if se.fin:
                return se.fin
            if se2.fin:
                return se2.fin
    except Exception:
        return {"error":"没有满足要求的涩图喵"}


if __name__ == "__main__":
    from method import METHOD
    met = METHOD()
    fin = met.normal_search(1000, "八雲紫")
    li = fin["body"]["illustManga"]["data"]
    print(fast_2_get(li))
