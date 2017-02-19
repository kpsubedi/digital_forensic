def val2addr(val):
    addr = ""
    for ch in val:
	addr += ("%02x "% ord(ch))
    addr = addr.strip(" ").replace(" ",":")[0:17]
    print addr


val2addr("\x00\x11\x50\x24\x68\x7F\x00\x00")



