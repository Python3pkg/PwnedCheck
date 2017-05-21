__author__ = 'Casey Dunham'
__version__ = "0.1.2"


import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
import json


PWNED_API_URL = "https://haveibeenpwned.com/api/breachedaccount/%s"


class InvalidEmail(Exception):
    pass


def check(email):
    req = urllib.request.Request(PWNED_API_URL % urllib.parse.quote(email))
    try:
        resp = urllib.request.urlopen(req)
        return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        if e.code == 400:
            raise InvalidEmail("Email address does not appear to be a valid email")
        return []

