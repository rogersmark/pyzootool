"""
Custom exception classes for pyzootool
"""

class ZooError(Exception):
    
    def __init__(self, reason):
        self.reason = reason
        
    def __unicode__(self):
        return u'%s' % self.reason
        
    def __str__(self):
        return self.__unicode__()
        