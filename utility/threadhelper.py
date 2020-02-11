import threading
from utility.logger import logger


class ThreadHelper(threading.Thread):
    def __init__(self, name, action):
        threading.Thread.__init__(self)
        # self.threadID = threadID
        self.name = name
        self.action = action

    def run(self):
        logger.info("Starting {0}".format(self.name))
        self.action()
        logger.info("Exiting {0}".format(self.name))

