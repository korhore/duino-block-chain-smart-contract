'''
Created on 08.03.2022
Edited on 08.03.2022

@author: Reijo Korhonen, reijo.korhonen@gmail.com

test Item class
python3 -m unittest tests/testSItem.py

'''
import time as systemTime
import os
import shutil as shutil
#import math as testMath
from enum import Enum
import struct
import random

from PIL import Image as PIL_Image
# for testing, get Image comparison
from PIL import ImageChops


import unittest
from Item import Item

class SensationTestCase(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def testItemCreation(self):
        item = Item(name='testItem',
                    description='testDescription',
                    code='rtestCode')
        self.assertNotEquals(item, None)

 

