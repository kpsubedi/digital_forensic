#!/usr/bin/python

import struct
import time
import subprocess
import os.path
import sys



def get_u8(data, offset=0):
    return struct.unpack('B', data[offset:offset+1])[0]
def get_u16(data, offset=0):
    return struct.unpack('<H', data[offset:offset+2])[0]
def get_u32(data, offset=0):
    return struct.unpack('<L', data[offset:offset+4])[0]
def get_u64(data, offset=0):
    return struct.unpack('<Q', data[offset:offset+8])[0]

#
def get_u128(data, offset=0):
    return data[offset:offset+16]

def print_uuid(data):
    ret_str = format(struct.unpack('<Q', data[8:16])[0], 'X').zfill(16) 
		+ format(struct.unpack('<Q', data[0:8])[0],'X').zfill(16)
    return ret_str

