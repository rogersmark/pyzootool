Introduction
=====================

pyzootool wraps the API of http://www.zootool.com. It's currently still very early in development, and not quite everything works.

Install
=====================

You can either just grab the head here from Github, or you can pip or easy_install the package as well as it's now on pypi.

What Works 
=====================

- Grabbing items by uid
- Grabbing items by popularity
- Grabbing items by username
- Getting information on a user
- Getting list of followers that a user has
- Getting list of friends that a user has
- Adding items to zootool

What Doesn't Work
=====================

- Features nobody told me they wanted :) (Auth issues now fixed)

Examples
=====================

Here's a few examples of what you can do with this tool::

	from pyzootool import controller
	zoocontrol = controller.ZooControl(apikey=YOUR_API_KEY)
	
	## User information
	followers = zoocontrol.user.get_user_followers('username')
	friends = zoocontrol.user.get_user_friends('username')
	userinfo = zoocontrol.user.get_userinfo('username')
	
	## Items
	popular_items = zoocontrol.item.get_popular('week')
	user_items = zoocontrol.item.get_items_by_user('username')
	item = zoocontrol.item.get_item('uid')
	
Here's use of authentication::

	from pyzootool import controller
	zoocontrol = controller.ZooControl(apikey=YOUR_API_KEY, username=USER, password=PASS)
	result = zoocontrol.item.add_item(url="http://www.google.com", title="A cool new search engine!")
	
