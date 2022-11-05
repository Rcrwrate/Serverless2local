from Controler.Plugin import Manager
import json

@Manager.registerEvent("/debug")
def debug(msg):
    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(msg)
    }
    