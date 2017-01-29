#!/usr/bin/python


import sys
import os.path
import struct

def get_u32(data, offset=0):
    return struct.unpack('<L', data[offset:offset+4])[0]

class Superblock():
    def __init__(self, data):
        self.total_inodes = get_u32(data)
        self.total_blocks = get_u32(data, 4)
        self.restricted_blocks = get_u32(data, 8)
        self.free_blocks = get_u32(data, 0xC)
        self.free_inodes = get_u32(data, 0x10)
        self.first_data_block = get_u32(data, 0x14)
        self.block_size = 2^(10 + get_u32(data, 0x18))
        self.blocks_per_group = get_u32(data, 0x20)
        self.clusters_per_group = get_u32(data, 0x24)
        self.inodes_per_group = get_u32(data, 0x28)

def usage():
    print("Usage: " + sys.argv[0] + " <image file>  <offset in sectors> \n Read superblock from an image")

def main():
    if len(sys.argv) < 3:
        usage()
# Read first sector

    if not os.path.isfile(sys.argv[1]):
        print("File " + sys.argv[1] + " cannot be opened for reading")
	exit(1) 

    with open(sys.argv[1], 'rb') as f:
        f.seek(1024 + int(sys.argv[2])*512)
        sb_raw = str(f.read(1024))
    #print sb_raw
    sb = Superblock(sb_raw)
    print ("Total Inodes: " + str(sb.total_inodes))
    print("Total Blocks: " + str(sb.total_blocks))
    print("Free Inodes: " + str(sb.free_inodes))
    print("Block Group Information")
    print("=======================")
    print("Blocks per Group: " + str(sb.blocks_per_group))
    print("Inodes per Group: " + str(sb.inodes_per_group))


if __name__=="__main__":
    main()
