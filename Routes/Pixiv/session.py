# -*- coding: UTF-8 -*-
import requests
import logging
import json
# import base64

requests.packages.urllib3.disable_warnings()

LOG = logging.getLogger("PIXIV")
LOG.setLevel(logging.ERROR)
T = logging.StreamHandler()
LOG.addHandler(T)

header = {
    "Host": "www.pixiv.net",
    "referer": "https://www.pixiv.net/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 Edg/96.0.1054.53",
}


class SESSION():
    def __init__(self):
        self.session = requests.Session()
        self.session.trust_env = False
        self.session.keep_alive = False

    def get(self, url, JSON=True):
        r = self.session.get(url, headers=header, verify=False)
        LOG.info("GET:\t" + r.url + "\n\t" + r.text)
        fin = r.text.replace("i.pximg.net", "i.pixiv.re")
        if JSON:
            return json.loads(fin)
        else:
            return fin

    # def get_base(self, url):
    #     headers = header.copy()
    #     headers["Host"] = "i.pximg.net"
    #     headers["referer"] = "https://www.pixiv.net"
    #     r = self.session.get(url, headers=headers, verify=False)
    #     LOG.info("GET:\t" + r.url + "\n\t")
    #     return r.text


if __name__ == "__main__":
    s = SESSION()
    # s.get("https://www.pixiv.net/ajax/search/artworks/%E6%98%8E%E6%97%A5%E6%96%B9%E8%88%9F?word=%E6%98%8E%E6%97%A5%E6%96%B9%E8%88%9F&order=date_d&mode=all&p=1&s_mode=s_tag_full&type=all&wlt=3000&hlt=3000&lang=zh")
    print(s.get_base(
        "https://i.pximg.net/img-original/img/2022/04/20/06/08/27/97749485_p0.jpg"))
