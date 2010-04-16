import json
import urllib

from pyzootool import ROOT_URL

class ZooItemResult():
    
    def __init__(self, json_data):
        """
        Takes a SINGLE json object. Do *not* pass arrays of json data in.
        """
        self.parse_results(json_data)
        
    def parse_results(self, json_data):
        """
        Maps out the json data fields to variables
        """
        self.uid = json_data['uid']
        self.title = json_data['title']
        self.url = json_data['url']
        self.type = json_data['type']
        self.views = json_data['views']
        self.likes = json_data['likes']
        self.permalink = json_data['permalink']
        self.tinyurl = json_data['tinyurl']
        self.thumbnail = json_data['thumbnail']

class ZooItem():
    
    def __init__(self, apikey, http):
        """
        Arguments: 
            apikey - ZooTool apikey
            http - httplib2 http connection
        """
        self.apikey = apikey
        self.http = http
        
    def get_item(self, item_id):
        """
        Argument:
            item_id - unique identifier of item
            
        Returns:
            result - ZooItemResult
            
        Takes in a uid, calls to the ZooTool api to get the JSON objects.
        Returns a parsed json result in the form of a ZooItemResult object.
        """
        values = {'uid': item_id, 'apikey': self.apikey}
        url = "%s/api/items/info/?%s" % (
            ROOT_URL, urllib.urlencode(values)
        )
        resp, content = self.http.request(url)
        json_data = json.loads(content)
        result = ZooItemResult(item)
        return result
        
    def get_popular(self, pop_type):
        """
        Argument:
            pop_type - Valid options are 'week', 'year', 'all', 'today'
            
        Returns:
            zoo_results - ZooItemResult
            
        Takes in the popular sorting option. Returns an array of ZooItemResults
        """
        values = {'type': pop_type, 'apikey': self.apikey }
        url = "%s/api/items/popular/?%s" % (
            ROOT_URL, urllib.urlencode(values)
        )
        resp, content = self.http.request(url)
        json_data = json.loads(content)
        zoo_results = []
        for item in json_data:
            result = ZooItemResult(item)
            zoo_results.append(result)
        return zoo_results
        
    def get_items_by_user(self, username):
        """
        Arguement:
            username - user we should grab items from
            
        Returns:
            zoo_results - Array of ZooItemResults
            
        Takes in a username, calls ZooTool API and receives JSON data. Kicks
        back an array of ZooItemResults
        """
        values = {'username': username, 'apikey': self.apikey}
        url = "%s/api/users/items/?%s" % (
            ROOT_URL, urllib.urlencode(values)
        )
        resp, content = self.http.request(url)
        json_data = json.loads(content)
        zoo_results = []
        for item in json_data:
            result = ZooItemResult(item)
            zoo_results.append(result)
        return zoo_results
        
    def add_item(self, url, title, tags=None, description=None, referer=None,
        public=None):
        """
        Arguments:
            url - Required. URL to object to be added
            title - Required. Title of object
            tags - Optional. Comma delimited string of tags
            description - Optional.
            referer - Optional
            public - Optional. Must equal 'y' or 'n'
            
        Returns:
            result - ZooItemResult
        """
        values = {
            'url': url,
            'title': title,
            'tags': tags,
            'description': description,
            'referer': referer,
            'public': public,
            'apikey': self.apikey
        }
        url = "%s/api/add/?%s" % (
            ROOT_URL, urllib.urlencode(values)
        )
        resp, content = self.http.request(url)
        json_data = json.loads(content)
        result = ZooItemResult(json_data['item'])
        return result