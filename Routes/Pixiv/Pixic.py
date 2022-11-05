import requests
import json
import logging
LOG = logging.getLogger("Pixic")
LOG.setLevel(logging.INFO)
T = logging.StreamHandler()
LOG.addHandler(T)

header = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "dnt": "1",
    "origin": "https://m.pixivic.com",
    # "referer": "https://m.pixivic.com/",
    "sec-ch-ua": '''" Not A;Brand";v="99", "Chromium";v="101", "Microsoft Edge";v="101"''',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "Android",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39"
}
# BASEAPI = "https://api.huisq.site"
BASEAPI = "https://api.phantom-sea-limited.ltd/Pixic"


class Pixivic():
    def __init__(self):
        self.session = requests.session()
        self.session.trust_env = False
        self.session.keep_alive = False
        try:
            with open("/mnt/au.log", "r", encoding="utf-8") as f:
                r = f.readlines()[0]
            self.header = header.copy()
            self.header["authorization"] = r
        except Exception:
            self.header = header.copy()
            self.header["authorization"] = ""
            LOG.info("Pixic初始化失败")

    def refresh_AU(self):
        url = BASEAPI + "/verificationCode"
        del self.header["authorization"]
        r = self.session.get(url, headers=self.header).json()
        imageBase64 = r["data"]["imageBase64"]
        vid = r["data"]["vid"]
        from Verification import VC
        vc = VC()
        code = vc.get_code(imageBase64)
        url = BASEAPI + f"/users/token?vid={vid}&value={code}"
        data = {
            "password": "12345678",
            "username": "蓬莱寺西琳"
        }
        r = self.session.post(url, json=data, headers=self.header)
        LOG.info(r.headers)
        LOG.info(r.text)
        try:
            self.header["authorization"] = r.headers["authorization"]
            with open("/mnt/au.log", "w", encoding="utf-8") as fn:
                fn.write(r.headers["authorization"])
        except Exception:
            raise Exception("无法登录")
        return None

    def search(self, word, page):
        url = BASEAPI + \
            "/illustrations?page={}&keyword={}&pageSize=30".format(page, word)
        r = self.session.get(url, headers=self.header)
        LOG.info(r.text)
        r = json.loads(r.text)
        if r["message"] in ["登录身份信息过期","token无效"]:
            raise Exception("登录身份信息过期")
        i = 0
        while i < len(r["data"]):
            # print(r["data"][i]["type"])
            if r["data"][i]["type"] == "ad_image":
                del r["data"][i]
            i += 1
        return r

    def auto_search(self, word, page):
        i = 1
        l = []
        while i <= int(page):
            try:
                l += self.search(word, i)["data"]
            except Exception as err:
                if err.args[0] == "登录身份信息过期":
                    try:
                        self.refresh_AU()
                        l += self.search(word, i)["data"]
                    except Exception:
                        return l
                else:
                    return l
            i += 1
        return l


if __name__ == "__main__":
    p = Pixivic()
    # p.refresh_AU()
    # p.search("bba",1)
    r = p.auto_search("bba","5")
    print(len(r))
    print(r)