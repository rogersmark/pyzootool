"""
Central point for pyzootool's control
"""
import httplib2
import hashlib

from pyzootool import items, users

class ZooControl():
    
    def __init__(self, apikey, username=None, password=None):
        self.apikey = apikey
        self.http = httplib2.Http()
        if username and password:
            hash = hashlib.sha1(password)
            self.http.add_credentials(username, hash.hexdigest())
            
        self.item = items.ZooItem(self.apikey, self.http)
        self.user = users.ZooUser(self.apikey, self.http)