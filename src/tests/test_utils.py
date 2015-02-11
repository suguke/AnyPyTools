# -*- coding: utf-8 -*-
"""
Created on Sun Jul 06 19:09:58 2014

@author: Morten
"""
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *
# TEST_UNICODE_LITERALS

import os
import pytest
import numpy as np

from anypytools.utils import (array2anyscript, get_anybodycon_path, 
                              define2str, path2str)



@pytest.yield_fixture(scope='module')
def fixture():
    yield True
    
    
def test_define2str():
    assert define2str('test',2) == '-def test="2"'
    assert define2str('Test','Main.MyStudy') == '-def Test="Main.MyStudy"'
    assert define2str('test','"This is a string"') == '-def test=---"\\"This is a string\\""'

def test_path2str():
    assert path2str('test','C:\hallo.txt') == '-p test=---"C:\\\\hallo.txt"'
    assert path2str('Test','C:/hallo.txt') == '-p Test=---"C:/hallo.txt"'
    

def test_array2anyscript():
    
    mat33 = array2anyscript( np.array([[1, 0, 0], [0, 1, 0], [0,0,1]]) ) 
    assert mat33 == '{{1,0,0},{0,1,0},{0,0,1}}'
    
    mat31 = array2anyscript(  np.array([[1, 0, 0]]) )
    assert mat31 == '{{1,0,0}}'
    
    mat13 = array2anyscript( np.array([[1], [0], [0]]) )
    assert mat13 == '{{1},{0},{0}}'
    
    mat3 = array2anyscript( np.array([0.333333333, -1.9999999999 , 0.0 ]) )
    assert mat3 == '{0.333333333,-1.9999999999,0}'
    
    str2 = array2anyscript( np.array(['hallo', 'world']) ) 
    assert str2 == '{"hallo","world"}'
    
    
def test_get_anybodycon_path():
    abc = get_anybodycon_path()
    
    assert os.path.exists(abc)
    

    
if __name__ == '__main__':
    test_array2anyscript() 