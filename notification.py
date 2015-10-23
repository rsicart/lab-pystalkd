#!/usr/bin/env/python3

from datetime import datetime

class Notification:
    def __init__(self, address, msg):
        self.address = address
        self.msg = msg
        self.date = datetime.now()

    def __str__(self):
        return "{} :: {} :: {}".format(self.address, self.msg, self.date)
