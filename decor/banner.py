import os
from colorama import Fore
import script

def banner():
    print(Fore.GREEN+'''
        __________   _________   __________  __________   __________
        |FFFFFFFFF   HH     HH   AAAAAAAAAA  CCCCCCCCCC   KK     kk |
        |FF          HH     HH   AA      AA  CC           KK   kkk  |
        |FF_____     HH_____HH   AA______AA  CC           KK kkk    |
        |FFFFFFF     HHhhhhhHH   AAaaaaaaAA  CC           KKk       |
        |FF          HH     HH   AA      AA  CC________   KK kkk    |
        |FF__________HH     HH___AA      AA__CCCCCCCCCC___KK    kkk_|
    
    '''+Fore.RESET)
    print(Fore.BLUE+"                                           ~ Developed By Om Shinde\n"+Fore.RESET)