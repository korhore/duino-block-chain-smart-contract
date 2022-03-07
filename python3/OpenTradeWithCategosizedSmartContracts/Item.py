'''
Created on 08.03.2022
Edited on 08.03.2022

@author: Reijo Korhonen, reijo.korhonen@gmail.com
'''

from PIL import Image as PIL_Image
from enum import Enum
import io
import math
import os
import psutil
import random
import struct
import sys

import time as systemTime
import uuid

#def enum(**enums):
#    return type('Enum', (), enums)
LIST_SEPARATOR=':'

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)


'''
Sensation is something Robot senses
'''

        

class Item(object):
    
    def __init__(self,
                 name,
                 description,
                 code,
                 id = None,
                 time = None):
        self.id=id
        self.time=time,
        self.name=name,
        self.description=description
        self.code=code
        
        if self.id is None:
            self.id = uuid.uuid4().hex
        if self.time is None:
            self.time = systemTime.time()
