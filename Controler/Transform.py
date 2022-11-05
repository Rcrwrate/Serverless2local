class Transform():
    @staticmethod
    def input(request, url):
        o = {
            'headerParameters': {},
            "headers": {},
            'httpMethod': 'GET',
            'isBase64Encoded': False,
            'path': '/API',
            'pathParameters': {},
            'queryString': {},
            'queryStringParameters': {},
            'requestContext': {
                'httpMethod': 'ANY',
                'identity': {},
                'path': '/API',
                'serviceId': 'LOCAL',
                'sourceIp': '0.0.0.0',
                'stage': 'release'
            }
        }
        for i in request.headers:
            o["headers"][i[0]] = i[1]
        args = request.args.to_dict()
        for i in args:
            if args[i] == '':
                o["queryString"][i] = True
            else:
                o["queryString"][i] = args[i]
        o["path"] = "/" + url
        o["requestContext"]["path"] = "/" + url
        o["httpMethod"] = request.method
        return o

    @staticmethod
    def out(msg):
        '''
        {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"Content-Type": "text/html"},
        "body": ""
        }
        '''
        if msg["isBase64Encoded"]:
            import base64
            from Flask import make_response
            # return "data:image/jpeg;base64," + msg["body"], msg["statusCode"], msg["headers"]
            # response = make_response(base64.decodebytes(msg["body"]))
            # response.headers = msg["headers"]
            # response.status_code = msg["statusCode"]
            # return response 
            return base64.decode(msg["body"]), msg["statusCode"], msg["headers"]
        else:
            return msg["body"], msg["statusCode"], msg["headers"]
