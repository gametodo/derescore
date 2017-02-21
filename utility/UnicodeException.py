# -*- coding: utf-8 -*-

from __future__ import unicode_literals

class UnicodeException(Exception):

    def __init__(self, message):

        if isinstance(message, unicode):
            super(UnicodeException, self).__init__(message.encode('utf-8'))
            self.message = message

        elif isinstance(message, str):
            super(UnicodeException, self).__init__(message)
            self.message = message.decode('utf-8')

        else:
            raise TypeError

    def __unicode__(self):

        return self.message
