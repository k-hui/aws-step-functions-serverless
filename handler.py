import json


def hello(event, context):
    body = {
        "message": "Hello",
        "input": event,
    }

    return {"code": 200, "body": json.dumps(body)}


def world(event, context):
    body = {
        "message": "World",
        "input": event,
    }

    return {"code": 200, "body": json.dumps(body)}
