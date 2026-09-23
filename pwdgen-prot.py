## VEry BAsic Password Generator - VEBAPG##

import os
import random
import sys

CHARNUM = 93 # this is the amount of printable characters to ensure randchar is within the printable range from 33 to 126 in ASCII
FIRSTCHAR = 33 # this is the first printable character in ASCII

def pwdgen(size):
    pwd = ''
    if size <= 0:
        return ""
    else:
        password = []
        while len(password) < size:
            randbyte = os.urandom(1)
            randval = randbyte[0]
            maxlimit = 256 - (256 % CHARNUM) 
            if randval < maxlimit:
                # da qua ho un valore che va da 0 a 186
                password.append(chr(randchar))

        pwd = ''.join(password)
        return pwd


def main():
    length = 12
    if len(sys.argv) > 1:
        length = int(sys.argv[1])
    pwd = pwdgen(length)

    print(pwd)




if __name__ == "__main__":
    main()
