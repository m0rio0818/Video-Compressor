import json

def makeRequest_JsonFile(filepath, method, custom, res_type, params=None):
    d = {
        "filepath" : filepath,
        "method" : method,
        "custom" : custom,
        "res_type" : res_type,
        "params" : params,
    }
    
    with open("../json/request.json", "w") as f:
        json.dump(d, f, indent=2)
    return