
# https://github.com/anpang54/astronomy.py
# (c) 2026 Anpang, MIT license


# IMPORTS

import urllib.request
import json


# CONSTANTS

_version = "0.0.1a"

_url = "https://astronomy.wiki/w/rest.php/v1"

_headers = {
    "User-Agent": f"astronomy.py/{_version}"
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

class AstronomyWikiException(Exception):
    pass

class Article:

    def __init__(self, id):
        self.id = id

    def __str__(self):
        if not hasattr(self, "id"):
            raise AstronomyWikiException("Article doesn't have an ID.") 
        return f"<Article {self.id}>"
    
    def read_raw(self):
        if not hasattr(self, "id"):
            raise AstronomyWikiException("Article doesn't have an ID.") 
        return _http_get(f"{_url}/page/{self.id}", True)["source"]
