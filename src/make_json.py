import json

def makeJsonFile(filepath, method, custom, params=None):
    d = {
        "filepath" : filepath,
        "method" : method,
        "custom" : custom,
        "params" : params,
    }
    
    with open("../json/request.json", "w") as f:
        json.dump(d, f)
    return
