#!/usr/bin/env python3

from pystalkd.Beanstalkd import Connection
import notification
import pickle
import base64

setup = {
	'connection': ('localhost', 11300),
	'tubes': {
		'use': 'python',	
		'ignore': ['default'],	
	}
}

c = Connection(*setup['connection'])

c.use(setup['tubes']['use'])
print("Using tube {}".format(c.using()))

notifications = []
notifications.append(notification.Notification("test1@example.com", "Hello"))

for notification in notifications:
    thing = pickle.dumps(notification)
    # beanstalk jobs only allows str objects
    body = base64.b64encode(thing)
    c.put(body.decode('ascii'))
