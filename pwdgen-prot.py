## VEry BAsic Password Generator - VEBAPG##

import os
import sys
# import tkinter as tk
# from tkinter import messagebox

def pwdgen(size):
    pwd = ""
    characters = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    
    if size <= 0:
        return ""
    else:
        password = []
        while len(password) < size:
            randbyte = os.urandom(1)[0]

            maxlimit = 256 - (256 % len(characters)) 

            if randbyte < maxlimit:
                # from here, randbyte goes from 0 to 186
                password.append(characters[randbyte%len(characters)])

        pwd = ''.join(password)
        return pwd


def main():
    length = 12
    if len(sys.argv) > 1:
        length = int(sys.argv[1])
    pwd = pwdgen(length)

    print(pwd)
    input("Premi INVIO per chiudere...")

    # Creazione di una semplice interfaccia pop-up
    # root = tk.Tk()
    # root.withdraw() # Nasconde la finestra principale vuota di tkinter

    # Mostra il pop-up con la password generata
    # messagebox.showinfo("Generatore Password", f"La tua nuova password è:\n\n{pwd}")




if __name__ == "__main__":
    main()
