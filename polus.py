
# https://github.com/anpang54/polus.py
# (c) 2026 Anpang, MIT license


# IMPORTS

import urllib.request
import json


# CONSTANTS

_version = "0.1.0"

_url = "https://polus.wiki/w/rest.php/v1"

_headers = {
    "User-Agent": f"polus.py/{_version}"
}


# MAKING REQUESTS

def _http_get(url, parse_json=False):
    request = urllib.request.Request(url, headers=_headers)
    with urllib.request.urlopen(request) as response:
        raw_data = response.read().decode("utf-8")
        if parse_json:
            return json.loads(raw_data)
        return raw_data


# CLASSES

class PolusException(Exception):
    pass

class Article:

    def __init__(self, id):
        self.id = id

    def __str__(self):
        if not hasattr(self, "id"):
            raise PolusException("Article doesn't have an ID.") 
        return f"<Article {self.id}>"
    
    def read_raw(self):
        if not hasattr(self, "id"):
            raise PolusException("Article doesn't have an ID.") 
        return _http_get(f"{_url}/page/{self.id}", True)["source"]
