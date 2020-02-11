import os
import time
import logging

# LOAD_TIME = time.strftime("%b-%d-%Y-%H:%M:%S")
#
# logger = logging.getLogger('TestFramework')
# logger.setLevel(logging.DEBUG)
#
# if not os.path.exists('./logs'):
#     os.makedirs('./logs')
#
# # formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
# formatter = logging.Formatter('%(asctime)s [line:%(lineno)d] %(levelname)s %(pid)s %(message)s')
#
# file_handler = logging.FileHandler('logs/' + LOAD_TIME + '.log')
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)
#
# console_handler = logging.StreamHandler()
# console_handler.setFormatter(formatter)
# logger.addHandler(console_handler)


class Log:
    def __init__(self):
        self.load_time = time.strftime("%b-%d-%Y-%H:%M:%S")
        self.logger = logging.getLogger('TestFramework')
        self.path = "./logs"
        self.file_extension = '.log'
        self.__setup()

    def __setup(self):
        self.logger.setLevel(logging.DEBUG)

        if not os.path.exists(self.path):
            os.makedirs(self.path)

        formatter = logging.Formatter('%(asctime)s [line:%(lineno)d] %(levelname)s %(thread)s %(message)s')

        file_handler = logging.FileHandler('{0}/{1}{2}'.format(self.path, self.load_time, self.file_extension))
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)


logger = Log().logger

