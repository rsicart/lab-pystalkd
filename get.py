#!/usr/bin/env python3

from pystalkd.Beanstalkd import Connection
import notification
import pickle
import base64

setup = {
		'connection': ('localhost', 11300),
		'tubes': {
			'watch': ['python'],	
			'ignore': ['default'],	
		}
}

c = Connection(*setup['connection'])

for tube in setup['tubes']['watch']:
	c.watch(tube)

print("Watching tubes {}".format(c.watching()))


for tube in setup['tubes']['ignore']:
	c.ignore(tube)

print("Ignoring tubes {}".format(c.watching()))

#for action, tubes in setup['tubes'].items():
#	for tube in tubes:
#		getattr(c, action)(tube)


job = c.reserve()

body = job.body.encode('ascii')
# beanstalk jobs only allows str objects
thing = base64.b64decode(body)
notification = pickle.loads(thing)

print(notification)

job.delete()
