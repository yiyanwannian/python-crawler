"""
Created on Apr 11, 2018

@author: houfa.zhou
"""

import time
import re
import sys
from decimal import *

sys.path.append("../")

from utility.logger import logger


def camel_to_snake(class_name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', class_name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def float_to_int(value):
    return int(Decimal(value))


def dict_to_list(input: dict):
    outputs = []
    for key in input.keys():
        outputs.append(input[key])
    
    return outputs

def func_executor(func, **kwargs):
    return func(**kwargs)

def show_api_info(node, has_restful = False):
    logger.info("{0} rpc: {1}".format(node.mode, node.rpc.url))
    logger.info("{0} jarserver: {1}".format(node.mode, node.jarserver.url))
    if has_restful:
        logger.info("{0} restful: {1}".format(node.mode, node.restful.url))


def show_obj_info(obj):
    return str(obj.__dict__)
    # return '\n'.join(['%s:%s' % item for item in obj.__dict__.items()])