import os

def apikey(*args, **kwargs):
    key = args[0]
    if key != os.environ['API_KEY']:
        return
    return {'authorization': 'successful'}