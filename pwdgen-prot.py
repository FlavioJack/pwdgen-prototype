import random
import sys
  
def pwdgen(size):
    pwd = ''
    if size <= 0:
        return ""
    else:
        ch_code = 0
        password = list()
        for i in range(size):
            if random.choice([True, False]):
                ch_code = random.randint(97, 122)
            else:
                ch_code = random.randint(48, 57)
            char = chr(ch_code)
            if ch_code < 123 and ch_code > 96:
                if random.choice([True, False]):
                    char = char.upper()
            
            password.append(char) 
        for c in password:
            pwd += c
        return pwd


def main():
    length = 12
    if len(sys.argv) > 1:
        length = int(sys.argv[1])
    pwd = pwdgen(length)

    print(pwd)




if __name__ == "__main__":
    main()
