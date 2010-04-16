import json
import urllib

from pyzootool import ROOT_URL

class ZooUserResult():
    
    def __init__(self, json_data):
        """
        Takes a SINGLE json data object. Do not pass an array in
        """
        self.parse_results(json_data)
        
    def parse_results(self, json_data):
        """
        Maps out the json data fields to variables
        """
        self.username = json_data['username']
        self.website = json_data['website']
        self.avatar = json_data['avatar']
        self.profile = json_data['profile']
        
class ZooUser():
    """
    TODO:
        This whole class
    """
    
    def __init__(self, apikey, http):
        """
        Arguments: 
            apikey - ZooTool apikey
            http - httplib2 http connection
        """
        self.apikey = apikey
        self.http = http
        
    def get_userinfo(self, username):
        """
        Argument:
            username - name of user you wish to get info on
            
        Returns:
            result - ZooUserResult
        
        Takes in a username, calls ZooTool API and gets json data
        """
        values = {'username': username, 'apikey': self.apikey}
        url = "%s/api/users/info/?%s" % (ROOT_URL, urllib.urlencode(values))
        resp, content = self.http.request(url)
        json_data = json.loads(content)
        result = ZooUserResult(json_data)
        
    def get_user_friends(self, username):
        """
        Argument:
            username - name of user you wish to get info on
            
        Returns:
            zoo_results - Array of ZooUserResult
        
        Takes in a username, calls ZooTool API and gets json data
        """
        values = {'username': username, 'apikey': self.apikey}
        url = "%s/api/users/friends/?%s" % (ROOT_URL, urllib.urlencode(values))
        resp, content = self.http.request(url)
        json_data = json.loads(content)
        zoo_results = []
        for item in json_data:
            result = ZooUserResult(item)
            zoo_results.append(result)
        if zoo_results:
            return zoo_results
        else:
            raise AttributeError("No Results Found")
        
    def get_user_followers(self, username):
        """
        Argument:
            username - name of user you wish to get info on

        Returns:
            zoo_results - Array of ZooUserResult

        Takes in a username, calls ZooTool API and gets json data
        """
        values = {'username': username, 'apikey': self.apikey}
        url = "%s/api/users/followers/?%s" % (ROOT_URL, urllib.urlencode(values))
        resp, content = self.http.request(url)
        json_data = json.loads(content)
        zoo_results = []
        for item in json_data:
            result = ZooUserResult(item)
            zoo_results.append(result)
        return zoo_results