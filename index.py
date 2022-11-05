from Controler.Plugin import Manager
from Lib.log import Log
import re

Manager.register("Routes.Pixiv.index")


def main(message):
    l = Log("Router", log_level=40).Log()
    for i in Manager.Plugin:
        # if i in message["path"]:
        if check(i,message["path"]):
            func = Manager.Plugin[i]
            return func(message)
            # try:
            #     return func(message)
            # except Exception as err:
            #     l.error(f"[Router][ERROR]\t\t{func}\t\t{err.args}")
            #     return {
            #         "isBase64Encoded": False,
            #         "statusCode": 500,
            #         "headers": {"Content-Type": "text/html"},
            #         "body": "SERVER ERROR"
            #     }
    return {
        "isBase64Encoded": False,
        "statusCode": 404,
        "headers": {"Content-Type": "text/html"},
        "body": "NO API ROUTES HERE"
    }


def check(path1, path2):
    try:
        re.search(f"^{path1}", path2).group(0)
    except Exception:
        return False
    else:
        return True
