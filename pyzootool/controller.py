"""
Central point for pyzootool's control
"""
import httplib2
from pyzootool import auth, items, users

class ZooControl():
    
    def __init__(self, apikey, username=None, password=None):
        self.apikey = apikey
        self.http = httplib2.Http()
        if username and password:
            ## TODO: Implement this
            self.auth = auth.ZooAuth(self.api_key, username, password)
        self.item = items.ZooItem(self.apikey, self.http)
        #self.user = users.ZooUser(self.apikey, self.http)