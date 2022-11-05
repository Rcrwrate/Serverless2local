# -*- coding: UTF-8 -*-
from session import SESSION


class METHOD():
    def __init__(self):
        self.session = SESSION()

    def get_by_pid(self, pid):
        url = "https://www.pixiv.net/ajax/illust/{}".format(str(pid))
        r = self.session.get(url)
        return r

    def geturls_by_pid(self, pid):
        url = "https://www.pixiv.net/ajax/illust/{}/pages".format(str(pid))
        r = self.session.get(url)
        return r

    def get_tag_popular(self, tag):
        url = "https://www.pixiv.net/ajax/search/top/{}?lang=zh".format(tag)
        r = self.session.get(url)
        fin = r["body"]["popular"]["permanent"] + \
            r["body"]["popular"]["recent"]
        if len(fin) == 0:
            return ["error", r["body"]["relatedTags"]]
        return fin

    def random_list(self, list):
        import random
        if "error" in list:
            fin = "你或许想搜的是"
            for i in list[1]:
                fin = fin + i + "  "
            return {"error": fin}
        i = random.choice(list)
        try:
            id = i["id"]
        except KeyError:
            id = i["illust_id"]
        r = self.geturls_by_pid(id)
        fin = random.choice(r["body"])
        fin["id"] = id
        return fin

    def official_index(self):
        import re
        import json
        r = self.session.get("https://www.pixiv.net/", False)
        fin = re.findall(r"class=\"json-data\" value=\'([\s\S]+?)\'>", r)[0]
        fin = json.loads(fin)
        return fin

    def normal_search(self, level: int, word: str, s_mode="s_tag"):
        if level == 0:
            search = word
        else:
            search = "{}users入り {}".format(level, word)
        url = "https://www.pixiv.net/ajax/search/artworks/{0}?word={0}&order=date_d&mode=all&p=1&s_mode={1}&type=illust_and_ugoira&lang=zh".format(
            search, s_mode)
        r = self.session.get(url)
        r["body"]["illustManga"]["data"] = self.Filtering_NO_COMIC(r["body"]["illustManga"]["data"])
        return r

    def old_ranking(self, type="daily", TOP=False):
        import re
        r = self.session.get("https://www.pixiv.net/ranking.php", False)
        li = re.findall(r'<a href=\"/artworks/([\s\S]+?)\"class=', r)
        if TOP:
            return self.get_by_pid(li[int(TOP)*2-1])
        else:
            return li

    def ranking(self, type="daily", date=False, TOP=False):
        if date:
            url = "https://www.pixiv.net/ranking.php?mode={}&date={}&p=1&format=json".format(
                type, date)
        else:
            url = "https://www.pixiv.net/ranking.php?mode={}&p=1&format=json".format(
                type)
        r = self.session.get(url)
        r["contents"] = self.Filtering_NO_COMIC(r["contents"])
        if TOP:
            PID = r["contents"][int(TOP)-1]["illust_id"]
            return self.get_by_pid(PID)
        return r

    def translate(self,word):
        url = "https://www.pixiv.net/rpc/cps.php?keyword={}&lang=zh".format(word)
        r = self.session.get(url)
        for i in r["candidates"]:
            if i["type"] == "tag_translation":
                if i["tag_translation"] == word:
                    return i["tag_name"]
        return False

    @staticmethod
    def Filtering_NO_COMIC(L:list):
        '''输入必须是列表'''
        O = []
        BAN = ["漫画","漫画素材工房"]
        for i in L:
            if [item for item in i["tags"] if item not in BAN] == i["tags"]:
                O.append(i)
        return O
    
    def random_ranking(self):
        import time
        import random
        TIME = list(time.localtime())[0:3]
        if TIME[2] == 1:
            DATA = str(random.randint(2016,TIME[0])) + str(random.randint(1,TIME[1])).zfill(2) + str(1).zfill(2)
        else:
            DATA = str(random.randint(2016,TIME[0])) + str(random.randint(1,TIME[1])).zfill(2) + str(random.randint(1,TIME[2]-1)).zfill(2)
        fin = self.ranking(date=DATA)
        id = random.choice(fin["contents"])["illust_id"]
        return self.get_by_pid(id)

    # def get_origian_img(self, pid_json: dict):
    #     url = pid_json["body"]["urls"]["original"]
    #     r = self.session.get_base(url)
    #     return r


if __name__ == "__main__":
    met = METHOD()
    
    print(met.random_ranking())
