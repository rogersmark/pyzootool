from unittest import TestCase

from pyzootool import users, items, controller

class ZooTest(TestCase):
    
    def setUp(self):
        self.user_info = {
            "username":"f4nt",
            "website":'null',
            "avatar":"http:\/\/blank.com/f4nt_l.jpg?1271429353",
            "profile":"http:\/\/zootool.com\/user\/f4nt\/"
        }
        self.item_info = {
            "uid":"wol",
            "title":"4Chan gets charitable",
            "url":"http:\/\/i.imgur.com\/kdYBh.jpg",
            "added":"1271422494",
            "type":"image",
            "views":"0",
            "likes":"1",
            "permalink":"http:\/\/zootool.com\/watch\/wol\/",
            "tinyurl":"http:\/\/zoo.tl\/wol",
            "thumbnail":"http:\/\/c0382052.cdn.cloudfiles.rackspacecloud.com\/wol_s.jpg?1271422495",
            "tags":["none"],
            "description":"None"
        }
        
        self.item_array = [
            {
                "uid":"wol",
                "title":"4Chan gets charitable",
                "url":"http:\/\/i.imgur.com\/kdYBh.jpg",
                "added":"1271422494",
                "type":"image",
                "views":"0",
                "likes":"1",
                "permalink":"http:\/\/zootool.com\/watch\/wol\/",
                "tinyurl":"http:\/\/zoo.tl\/wol",
                "thumbnail":"http:\/\/c0382052.cdn.cloudfiles.rackspacecloud.com\/wol_s.jpg?1271422495",
                "tags":["none"],
                "description":"None"
            },
            {
                "uid":"r4v6",
                "title":"f4nt's pyzootool at master - GitHub",
                "url":"http:\/\/github.com\/f4nt\/pyzootool",
                "added":"1271381736",
                "type":"page",
                "views":"6",
                "likes":"2",
                "permalink":"http:\/\/zootool.com\/watch\/r4v6\/",
                "tinyurl":"http:\/\/zoo.tl\/r4v6",
                "thumbnail":"http:\/\/c0397571.cdn.cloudfiles.rackspacecloud.com\/r4v6_s.jpg?1271502861",
                "tags":["zootool","python"],
                "description":""
            }
        ]
        
    def test_user_parse(self):
        result = users.ZooUserResult(self.user_info)
        self.assertEqual(self.user_info['username'], result.username)
        
    def test_item_parse(self):
        item = items.ZooItemResult(self.item_info)
        self.assertEqual(self.item_info['uid'], item.uid)
        
    def test_array_item_parse(self):
        result_list = []
        for item in self.item_array:
            result = items.ZooItemResult(item)
            result_list.append(result)
        self.assertEqual(len(self.item_array), len(result_list))