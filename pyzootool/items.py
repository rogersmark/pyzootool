import json
import urllib

from pyzootool import ROOT_URL

class ZooResult():
    
    def __init__(self, json_data):
        self.parse_results(json_data)
        
    def parse_results(self, json_data):
        print json_data
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
        self.apikey = apikey
        self.http = http
        
        
    def get_item(self, item_id):
        values = {'uid': item_id, 'apikey': self.apikey}
        url = "%s/api/items/info/?%s" % (
            ROOT_URL, urllib.urlencode(values)
        )
        resp, content = self.http.request(url)
        json_data = json.loads(content)
        result = ZooResult(item)
        return zoo_results
        
    def get_popular(self, pop_type):
        values = {'type': pop_type, 'apikey': self.apikey }
        url = "%s/api/items/popular/?%s" % (
            ROOT_URL, urllib.urlencode(values)
        )
        resp, content = self.http.request(url)
        json_data = json.loads(content)
        zoo_results = []
        for item in json_data:
            result = ZooResult(item)
            zoo_results.append(result)
        return zoo_results