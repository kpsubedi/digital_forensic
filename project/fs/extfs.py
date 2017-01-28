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
    ret_str = format(struct.unpack('<Q', data[8:16])[0], 'X').zfill(16)		+ format(struct.unpack('<Q', data[0:8])[0],'X').zfill(16)
    return ret_str

def get_compatible_feature_list(u32):
    ret_list = []
    if u32 & 0x1:
        ret_list.append('Directory Preallocate')
    if u32 & 0x2:
        ret_list.append('Imagic Inodes')
    if u32 & 0x4:
        ret_list.append('Has Journal')
    if u32 & 0x8:
        ret_list.append('Extended Attributes')
    if u32 & 0x10:
	ret_list.append('Resize Inode')
    if u32 & 0x20:
        ret_list.append('Directory Index')
    if u32 & 0x40:
	ret_list.append('Lazy Block Groups')
    if u32 & 0x80:
        ret_list.append('Exclude Inode')
    if u32 & 0x100:
	ret_list.append('Exclude Bitmap') 
    if u32 & 0x200:
       ret_list.append('Sparse Super2')
    return ret_list

def get_incompatible_features_list(u32):
    ret_list = []
    if u32 & 0x1:
	ret_list.append('Compression')
    if u32 & 0x2:
	ret_list.append('Filetype')
    if u32 & 0x4:
        ret_list.append('Recover')
    if u32 & 0x8:
        ret_list.append('Journal Device')
    if u32 & 0x10:
        ret_list.append('Meta Block Groups')
    if u32 & 0x40:
        ret_list.append('Extents')
    if u32 & 0x80:
        ret_list.append('64-bit')

    if u32 & 0x100:
	ret_list.append('Multiple Mount Protection')
    if u32 & 0x200:
	ret_list.append('Flexible Block Groups')
    if u32 & 0x400:
	ret_list.append('Extended Attributes in Inodes')
    if u32 & 0x1000:
	ret_list.append('Directory Data')
    if u32 & 0x2000:
	ret_list.append('Block Group Metadata Checksum')
    if u32 & 0x4000:
	ret_list.append('Large Directory')
    if u32 & 0x8000:
        ret_list.append('Inline Data')
    if u32 & 0x10000:
        ret_list.append('Encrypted Inodes')
    return ret_list

def get_read_only_compatible_features_list(u32):
    ret_list = []

    if u32 & 0x1:
        ret_list.append('Sparse Super')
    if u32 & 0x2:
        ret_list.append('Large File')
    if u32 & 0x4:
        ret_list.append('Btree Directory')
    if u32 & 0x8:
        ret_list.append('Huge File')
    if u32 & 0x10:
        ret_list.append('Group Descriptor Table Checksum')
    if u32 & 0x20:
        ret_list.append('Directory Nlink')
    if u32 & 0x40:
        ret_list.append('Extra Isize')
    if u32 & 0x80:
        ret_list.append('Has Snapshot')
    if u32 & 0x100:
        ret_list.append('Quota')
    if u32 & 0x200:
        ret_list.append('Big Alloc')
    if u32 & 0x400:
        ret_list.append('Metadata Checksum')
    if u32 & 0x800:
        ret_list.append('Replica')
    if u32 & 0x1000:
        ret_list.append('Read-Only')

    return ret_list


# this class will parse the data in a superblock

class Superblock():
    def __init__(self, data):
        self.total_inodes = get_u32(data)

def usage():
    print("Usage " + sys.argv[0] + " <image file>    <offset in sectors> \nReads superblock from an image")


def main():
    if len(sys.argv) < 3:
        usage()

#Read first sector

    if not os.path..isfile(sys.argv[1]):
        print("File " + sys.argv[1] + " cannot be open for reading")
        exit(1)

    with open(sys.argv[1], 'rb') as f:
        f.seek(1024 + int(sys.argv[2]) * 512)
        sb_raw = str(f.read(1024))
    sb = Superblock(sb_raw)
    sb.preety_print()

if __name__=="__main__":
    main()

