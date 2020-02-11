""" This is a Singleton metaclass. All classes affected by this metaclass 
have the property that only one instance is created for each set of arguments 
passed to the class constructor."""


class Singleton(type):

    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(cls, bases, dict)
        cls._instanceDict = {}

    def __call__(cls, *args, **kwargs):
        argdict = {'args': args}
        argdict.update(kwargs)
        argset = frozenset(argdict)
        if argset not in cls._instanceDict:
            cls._instanceDict[argset] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instanceDict[argset]


# class Singleton(type):
#     def __init__(cls, name, bases, dic):
#         super(Singleton, cls).__init__(name, bases, dic)
#         cls.instance = None

#     def __call__(cls, *args, **kwargs):
#         if cls.instance is None:
#             print("Creating NEW Singleton instance")

#             cls.instance = super(Singleton, cls).__call__(*args, **kwargs)

#         return cls.instance


# class Singleton(type):
# """ This is a Singleton metaclass. All classes affected by this metaclass 
# have the property that only one instance is created for each set of arguments 
# passed to the class constructor."""

#     def __init__(cls, name, bases, dict):
#         super(Singleton, cls).__init__(cls, bases, dict)
#         cls._instanceDict = {}

#     def __call__(cls, *args, **kwargs):
#         argdict = {'args': args}
#         argdict.update(kwargs)
#         argset = frozenset(argdict)
#         if argset not in cls._instanceDict:
#             cls._instanceDict[argset] = super(Singleton, cls).__call__(*args, **kwargs)
#         return cls._instanceDict[argset]

# class Connection(object):
# """ Simulate a connection that sends messages to a host. 
# Note that each host passed to the constructor will 
# instantiate this class only once."""
#     __metaclass__ = Singleton

#     def __init__(self, host = 'none'):
#         self.host = host
        
#     def send(self, msg):
#         print "Sent to {host}: {msg}".format(host = self.host, msg = msg)

# conn1 = Connection(host = 'myhost')
# conn2 = Connection(host = 'home')
# conn3 = Connection(host = 'home')

# assert(id(conn3) == id(conn2))
# assert(id(conn1) != id(conn2))