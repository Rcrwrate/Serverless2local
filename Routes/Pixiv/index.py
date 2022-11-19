# -*- coding: utf8 -*-
import json
from .method import METHOD
from Controler.Plugin import Manager


def get_qs(qs, key):
    try:
        id = qs[key]
    except KeyError:
        return False
    else:
        return id


def main_handler(event, context):
    try:
        return main(event, context)
    except Exception as err:
        r = {"error": "坏了，后台出错了，错误序列号{}\n错误原因{}".format(
            event["headers"]["x-api-requestid"], err.args)}
        return {
            "isBase64Encoded": False,
            "statusCode": 500,
            "headers": {"Content-Type": "text/json"},
            "body": json.dumps(r)
        }

@Manager.registerEvent("/PIXIV")
def main(event):
    path = event["path"]
    query = event["queryString"]
    if path == "/PIXIV/illust":
        pid = get_qs(query, "pid")
        thumb = get_qs(query, "thumbnails")
        met = METHOD()
        r = met.get_by_pid(pid)
        if thumb:
            base = r["body"]["urls"]["original"]
            return {
                "isBase64Encoded": False,
                "statusCode": 302,
                "headers": {"Location": base},
                "body": base
            }
        else:
            return {
                "isBase64Encoded": False,
                "statusCode": 200,
                "headers": {"Content-Type": "text/json"},
                "body": json.dumps(r)
            }
    elif path == "/PIXIV/tag":
        tag = get_qs(query, "tag")
        met = METHOD()
        r = met.get_tag_popular(tag)
        if get_qs(query, "random"):
            r = met.random_list(r)
        return {
            "isBase64Encoded": False,
            "statusCode": 200,
            "headers": {"Content-Type": "text/json"},
            "body": json.dumps(r)
        }
    elif path == "/PIXIV/title":
        met = METHOD()
        fin = met.official_index()
        if get_qs(query, "random"):
            fin = met.random_list(
                fin["pixivBackgroundSlideshow.illusts"]["landscape"])
        return {
            "isBase64Encoded": False,
            "statusCode": 200,
            "headers": {"Content-Type": "text/json"},
            "body": json.dumps(fin)
        }
    elif path == "/PIXIV/search":
        from .more_session import fast_2_get
        word = get_qs(query, "word").split("+")
        level = get_qs(query, "level")
        if level:
            level = int(level)
        else:
            level = 0
        met = METHOD()
        word = met.translate_list(word)
        r = met.normal_search(level, word)
        if len(r["body"]["illustManga"]["data"]) == 0:
            r = met.normal_search(level, word, s_mode="s_tc")
        if len(r["body"]["illustManga"]["data"]) == 0:
            fin = {"error": "没有搜索到结果喵"}
        else:
            fin = fast_2_get(r["body"]["illustManga"]["data"])
        return{
            "isBase64Encoded": False,
            "statusCode": 200,
            "headers": {"Content-Type": "text/json"},
            "body": json.dumps(fin)
        }
    elif path == "/PIXIV/random/thumbnails":
        met = METHOD()
        fin = met.random_ranking()
        base = fin["body"]["urls"]["original"].replace("i.pixiv.re","piv.sirin.top")
        return {
            "isBase64Encoded": False,
            "statusCode": 302,
            "headers": {"Location": base},
            "body": base
        }
    elif path == "/PIXIV/random":
        met = METHOD()
        fin = met.random_ranking()
        return {
            "isBase64Encoded": False,
            "statusCode": 200,
            "headers": {"Content-Type": "text/json"},
            "body": json.dumps(fin)
        }
    elif path == "/PIXIV/ranking":
        top = get_qs(query, "top")
        mode = get_qs(query, "mode")
        Date = get_qs(query, "date")
        met = METHOD()
        if mode in ["weekly", "monthly"]:
            fin = met.ranking(type=mode, date=Date, TOP=top)
        else:
            fin = met.ranking(date=Date, TOP=top)
        return {
            "isBase64Encoded": False,
            "statusCode": 200,
            "headers": {"Content-Type": "text/json"},
            "body": json.dumps(fin)
        }
    elif path == "/PIXIV/pixic":
        word = get_qs(query, "word").split("+")
        page = get_qs(query, "page")
        met = METHOD()
        if len(word) == 1:
            transed = met.translate(word[0])
            if transed != False and page == False:
                word = transed
                page = 3
            elif transed != False and page != False:
                word = transed
            elif page == False:
                page = 2
                word = word[0]
        else:
            word = met.translate_list(word)
            page = 1
        from .Pixic import Pixivic
        pixic = Pixivic()
        fin = pixic.auto_search(word=word, page=page)
        if get_qs(query, "random"):
            from .more_session import fast_2_get
            fin = fast_2_get(fin)
        return {
            "isBase64Encoded": False,
            "statusCode": 200,
            "headers": {"Content-Type": "text/json"},
            "body": json.dumps(fin)
        }
    elif path == "/PIXIV/test":
        met = METHOD()
        word = get_qs(query, "word").split("+")
        return {
            "isBase64Encoded": False,
            "statusCode": 200,
            "headers": {"Content-Type": "text/json"},
            "body": met.translate_list(word)
        }
    elif path == "/PIXIV/login":
        from .Pixic import Pixivic
        pixic = Pixivic()
        pixic.refresh_AU()
        return {
            "isBase64Encoded": False,
            "statusCode": 200,
            "headers": {"Content-Type": "text/json"},
            "body": "{}"
        }
    elif path == "/PIXIV/mirror":
        return {
            "isBase64Encoded": False,
            "statusCode": 200,
            "headers": {"Content-Type": "text/json"},
            "body": json.dumps({"0": "i.pixiv.re", "1": "p.kirin.workers.dev", "2": "proxy.pixivel.moe", "3": "pximg.obfs.dev", "4": "pximg.moonchan.xyz"})
        }
    elif path == "/PIXIV/setu":
        from .callback import SETU
        return {
            "isBase64Encoded": False,
            "statusCode": 200,
            "headers": {"Content-Type": "text/html"},
            "body": SETU()
        }
    elif path == "/PIXIV/au/w":
        with open("/mnt/au.log", "w", encoding="utf-8") as f:
            f.write("eyJhbGciOiJIUzUxMiJ9.eyJwZXJtaXNzaW9uTGV2ZWwiOjIsInJlZnJlc2hDb3VudCI6MiwiaXNDaGVja1Bob25lIjowLCJ1c2VySWQiOjEzODEzNywiaWF0IjoxNjUyODQ1MzYwLCJleHAiOjE2NTMzNjM3NjB9.Bclf5qS4fH8gW_lzaOGePxwevocxbH_RWqTTFzajdZunfV0dvKOgv73F2S7QjWv7Q6ZbPjZg0L5O0ws88VloJA")
        return {
            "isBase64Encoded": False,
            "statusCode": 200,
            "headers": {"Content-Type": "text/json"},
            "body": "OK"
        }
    elif path == "/PIXIV/au/r":
        with open("/mnt/au.log", "r", encoding="utf-8") as f:
            r = f.readlines()[0]
        return {
            "isBase64Encoded": False,
            "statusCode": 200,
            "headers": {"Content-Type": "text/json"},
            "body": r
        }
    else:
        return {
            "isBase64Encoded": False,
            "statusCode": 403,
            "headers": {"Content-Type": "text/json"},
            "body": "{'error':'403 forbidden'}"
        }
