#!/bin/python3

#---------------------------------------------------------------------------#
# Imports
#---------------------------------------------------------------------------#

import os
from colorama import Fore
from hacktool import IG
from hacktool import VA
from hacktool import WAA
from hacktool import ET
from hacktool import MA
from hacktool import PCT
from hacktool import PET
from hacktool import SAS
from hacktool import SS
from hacktool import WT

from decor import banner

os.system('clear')
print('<-----Hey There, Use It Only For Legal Purpose----->')
print('/////This script is for only testing///// \n/////This can '+Fore.RED+'harm'+Fore.RESET+' systems so/////\n/////use carefully/////')
#print(banner.banner())








#--------------------------------------------------------------------------------------#
#Information Gathering
#--------------------------------------------------------------------------------------#

class info_gather():
    def __init__(self):
        self.clr_scr()
        self.get_tools()
        

    def vldt(self):
        print("Choose Correct Options")
        self.clr_scr()
        self.get_tools()

    def clr_scr(self):
        os.system('clear')

    def get_tools(self):
        print("choose your tool \n")
        print('     1 Nmap')
        print('     2 Recon-ng')
        print('     3 Dmitry')
        print('     4 IKE-Scan(Under Dev)')
        print('     5 Net-Discover')
        print('     6 Wireshark')
        print('     7 Zenmap')
        print('     8 Maltego')
        print('     9 Etherape')
        print('     10 Enum4Linux')
        print('     99 Back')
        try:
            load = input(':I:N:P:U:T:> ')
            os.system('clear')
            if load == "1":
                IG.nmap_scan()
            elif load == '2':
                IG.recon_scan()
            elif load == '3':
                IG.dmitry_scan()
            elif load == '4':
                IG.ike_scan()
            elif load == '5':
                IG.netdisc_scan()
            elif load == '6':
                IG.wire_scan()
            elif load == '7':
                IG.zen_scan()
            elif load == '8':
                IG.maltego_scan()
            elif load == '9':
                IG.ether_ape_scan()
            elif load == '10':
                IG.enum_for_linux()
            elif load == '99':
                boot_up()
            else:
                self.vldt()
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            boot_up()





#--------------------------------------------------------------------------------------#
# Vulnarability Analysis
#--------------------------------------------------------------------------------------#

class vuln_anl():
    def __init__(self):
        self.get_tools()
        

    def vldt(self):
        print("Choose Correct Options")
        self.clr_scr()
        self.get_tools()

    def clr_scr(self):
        os.system('clear')

    def get_tools(self):
        print("choose your tool \n")
        print('     1 Golismero(Under Development)')
        print('     2 AFL(Under Development)')
        print('     3 OpenVAS')
        print('     4 Lynis')
        print('     99 Back')
        try:
            load = input(':I:N:P:U:T:> ')
            self.clr_scr()
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            boot_up()
        if load == "1":
            VA.golis_test()
        elif load == '2':
            VA.afl_test()
        elif load == '3':
            VA.open_vas_test()
        elif load == '4':
            VA.lynis_test()
        elif load == '99':
            boot_up()
        else:
            self.vldt()


#--------------------------------------------------------------------------------------#
# Web Aplication Analysis
#--------------------------------------------------------------------------------------#

class web_app_anl():
    def __init__(self):
        self.get_tools()
        

    def vldt(self):
        print("Choose Correct Options")
        self.clr_scr()
        self.get_tools()

    def clr_scr(self):
        os.system('clear')

    def get_tools(self):
        print("choose your tool \n")
        print('     1 Burpsuite')
        print('     2 OWASP ZAP')
        print('     3 WP Scan')
        print('     4 Commix')
        print('     5 HTtrack')
        print('     6 Skipfish')
        print('     7 WebScarab')
        print('     8 CutyCapt')
        print('     99 Back')
        try:
            load = input(':I:N:P:U:T:> ')
            self.clr_scr()
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            boot_up()
        if load == "1":
            WAA.burpsuite_scan()
        elif load == '2':
            WAA.owasp_scan()
        elif load == '3':
            WAA.wp_scan()
        elif load == '4':
            WAA.commix_scan()
        elif load == '5':
            WAA.httrack_scan()
        elif load == '6':
            WAA.skipfish_scan()
        elif load == '7':
            WAA.webscarab_scan()
        elif load == '8':
            WAA.webscarab_scan()
        elif load == '99':
            boot_up()
        else:
            self.vldt()



#--------------------------------------------------------------------------------------#
# Exploitation Tools
#--------------------------------------------------------------------------------------#

class expl_tools():
    def __init__(self):
        self.get_tools()
        

    def vldt(self):
        print("Choose Correct Options")
        self.clr_scr()
        self.get_tools()

    def clr_scr(self):
        os.system('clear')

    def get_tools(self):
        print('     1 MetaSploit Framework')
        print('     2 Termineter(Under Dev)')
        print('     3 WebSploit')
        print('     4 Hexorbase')
        print('     5 Oscanner(Under Dev)')
        print('     6 Sandi-GUI')
        print('     7 GhostPhisher')
        print('     8 Social Engineering Toolkit')
        print('     9 Commix')
        print('     10 SQL Map(Under dev)')
        print('     99 Back')
        try:
            load = input(':I:N:P:U:T:> ')
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            boot_up()
        if load == "1":
            ET.meta_sploit()
        elif load == '2':
            ET.termi_test()
        elif load == '3':
            ET.web_sploit()
        elif load == '4':
            ET.hexor_base()
        elif load == '5':
            ET.o_scanner()
        elif load == '6':
            ET.sandi_gui()
        elif load == '7':
            ET.ghost_phisher()
        elif load == '8':
            ET.s_e_toolkit()
        elif load == '9':
            ET.com_mix()
        elif load == '10':
            ET.sql_map()
        elif load == '99':
            boot_up()
        else:
            self.vldt()



#--------------------------------------------------------------------------------------#
# Maintaining Access Tools
#--------------------------------------------------------------------------------------#

class maint_accs():
    def __init__(self):
        print("<--------------This Module Is Under Development------------->")
        boot_up()
        

    def vldt(self):
        print("Choose Correct Options")
        self.clr_scr()
        self.get_tools()

    def clr_scr(self):
        os.system('clear')

    def get_tools(self):
        print("choose your tool \n")
        print('     1 Exe2Hex')
        print('     2 Shelter')
        print('     3 Backdoore Factory')
        print('     4 Proxychains')
        print('     5 Nishang')
        print('     6 Weevely')
        print('     7 BDf Proxy')
        print('     8 Windows-binaries')
        print('     99 Back')
        try:
            load = input(':I:N:P:U:T:>')
            self.clr_scr()
        except KeyboardInterrupt:
            print("Keyboard interrupt")
            boot_up()
        if load == "1":
            MA.exe_to_hex()
        elif load == '2':
            MA.shelter()
        elif load == '3':
            MA.backdoor_factory()
        elif load == '4':
            MA.proxy_chains()
        elif load == '5':
            MA.ni_shang()
        elif load == '6':
            MA.wee_vely()
        elif load == '7':
            MA.bdf_proxy()
        elif load == '8':
            MA.windows_binaries()
        elif load == '99':
            boot_up()
        else:
            self.vldt()



#--------------------------------------------------------------------------------------#
# Post Exploitation Tools
#--------------------------------------------------------------------------------------#

class post_explt():
    def __init__(self):
        print("<--------------This Module Is Under Development------------->")
        boot_up()

    def vldt(self):
        print("Choose Correct Options")
        self.clr_scr()
        self.get_tools()

    def clr_scr(self):
        os.system('clear')

    def get_tools(self):
        print("choose your tool \n")
        print('1 Nmap')
        print('2 Recon-ng')
        print('3 Dmitry')
        print('4 IKE-Scan(Under Dev)')
        print('5 Net-Discover')
        print('6 Wireshark')
        print('7 Zenmap')
        print('8 Maltego')
        print('9 Etherape')
        print('10 Enum4Linux')
        print('99 Back')
        load = input(':I:N:P:U:T:>')
        os.system('clear')
        if load == "1":
            IG.nmap_scan()
        elif load == '2':
            IG.recon_scan()
        elif load == '3':
            IG.dmitry_scan()
        elif load == '4':
            IG.ike_scan()
        elif load == '5':
            IG.netdisc_scan()
        elif load == '6':
            IG.wire_scan()
        elif load == '7':
            IG.zen_scan()
        elif load == '8':
            IG.maltego_scan()
        elif load == '9':
            IG.ether_ape_scan()
        elif load == '10':
            IG.enum_for_linux()
        elif load == '99':
            boot_up()
        else:
            self.vldt()



#--------------------------------------------------------------------------------------#
# Password Cracking Tools
#--------------------------------------------------------------------------------------#

class passwd_crack():
    def __init__(self):
        print("<--------------This Module Is Under Development------------->")
        boot_up()
        

    def vldt(self):
        print("Choose Correct Options")
        self.clr_scr()
        self.get_tools()

    def clr_scr(self):
        os.system('clear')

    def get_tools(self):
        print("choose your tool \n")
        print('1 Nmap')
        print('2 Recon-ng')
        print('3 Dmitry')
        print('4 IKE-Scan(Under Dev)')
        print('5 Net-Discover')
        print('6 Wireshark')
        print('7 Zenmap')
        print('8 Maltego')
        print('9 Etherape')
        print('10 Enum4Linux')
        print('99 Back')
        load = input(':I:N:P:U:T:>')
        os.system('clear')
        if load == "1":
            IG.nmap_scan()
        elif load == '2':
            IG.recon_scan()
        elif load == '3':
            IG.dmitry_scan()
        elif load == '4':
            IG.ike_scan()
        elif load == '5':
            IG.netdisc_scan()
        elif load == '6':
            IG.wire_scan()
        elif load == '7':
            IG.zen_scan()
        elif load == '8':
            IG.maltego_scan()
        elif load == '9':
            IG.ether_ape_scan()
        elif load == '10':
            IG.enum_for_linux()
        elif load == '99':
            boot_up()
        else:
            self.vldt()


#--------------------------------------------------------------------------------------#
# Wireless Attack Tools
#--------------------------------------------------------------------------------------#

class wirels_tools():
    def __init__(self):
        print("<--------------This Module Is Under Development------------->")
        boot_up()
        

    def vldt(self):
        print("Choose Correct Options")
        self.clr_scr()
        self.get_tools()

    def clr_scr(self):
        os.system('clear')

    def get_tools(self):
        print("choose your tool \n")
        print('1 Nmap')
        print('2 Recon-ng')
        print('3 Dmitry')
        print('4 IKE-Scan(Under Dev)')
        print('5 Net-Discover')
        print('6 Wireshark')
        print('7 Zenmap')
        print('8 Maltego')
        print('9 Etherape')
        print('10 Enum4Linux')
        print('99 Back')
        load = input(':I:N:P:U:T:>')
        os.system('clear')
        if load == "1":
            IG.nmap_scan()
        elif load == '2':
            IG.recon_scan()
        elif load == '3':
            IG.dmitry_scan()
        elif load == '4':
            IG.ike_scan()
        elif load == '5':
            IG.netdisc_scan()
        elif load == '6':
            IG.wire_scan()
        elif load == '7':
            IG.zen_scan()
        elif load == '8':
            IG.maltego_scan()
        elif load == '9':
            IG.ether_ape_scan()
        elif load == '10':
            IG.enum_for_linux()
        elif load == '99':
            boot_up()
        else:
            self.vldt()



#--------------------------------------------------------------------------------------#
# Sniffing and Spoofing Tools
#--------------------------------------------------------------------------------------#

class snif_an_spoof():
    def __init__(self):
        print("<--------------This Module Is Under Development------------->")
        boot_up()
        

    def vldt(self):
        print("Choose Correct Options")
        self.clr_scr()
        self.get_tools()

    def clr_scr(self):
        os.system('clear')

    def get_tools(self):
        print("choose your tool \n")
        print('1 Nmap')
        print('2 Recon-ng')
        print('3 Dmitry')
        print('4 IKE-Scan(Under Dev)')
        print('5 Net-Discover')
        print('6 Wireshark')
        print('7 Zenmap')
        print('8 Maltego')
        print('9 Etherape')
        print('10 Enum4Linux')
        print('99 Back')
        load = input(':I:N:P:U:T:>')
        os.system('clear')
        if load == "1":
            IG.nmap_scan()
        elif load == '2':
            IG.recon_scan()
        elif load == '3':
            IG.dmitry_scan()
        elif load == '4':
            IG.ike_scan()
        elif load == '5':
            IG.netdisc_scan()
        elif load == '6':
            IG.wire_scan()
        elif load == '7':
            IG.zen_scan()
        elif load == '8':
            IG.maltego_scan()
        elif load == '9':
            IG.ether_ape_scan()
        elif load == '10':
            IG.enum_for_linux()
        elif load == '99':
            boot_up()
        else:
            self.vldt()



#--------------------------------------------------------------------------------------#
# System Services
#--------------------------------------------------------------------------------------#

class sys_serv():
    def __init__(self):
        print("<--------------This Module Is Under Development------------->")
        boot_up()
        

    def vldt(self):
        print("Choose Correct Options")
        self.clr_scr()
        self.get_tools()

    def clr_scr(self):
        os.system('clear')

    def get_tools(self):
        print("choose your tool \n")
        print('1 Nmap')
        print('2 Recon-ng')
        print('3 Dmitry')
        print('4 IKE-Scan(Under Dev)')
        print('5 Net-Discover')
        print('6 Wireshark')
        print('7 Zenmap')
        print('8 Maltego')
        print('9 Etherape')
        print('10 Enum4Linux')
        print('99 Back')
        load = input(':I:N:P:U:T:>')
        os.system('clear')
        if load == "1":
            IG.nmap_scan()
        elif load == '2':
            IG.recon_scan()
        elif load == '3':
            IG.dmitry_scan()
        elif load == '4':
            IG.ike_scan()
        elif load == '5':
            IG.netdisc_scan()
        elif load == '6':
            IG.wire_scan()
        elif load == '7':
            IG.zen_scan()
        elif load == '8':
            IG.maltego_scan()
        elif load == '9':
            IG.ether_ape_scan()
        elif load == '10':
            IG.enum_for_linux()
        elif load == '99':
            boot_up()
        else:
            self.vldt()





#----------------------------------------------------------------------------------#
# Boot The Program
#----------------------------------------------------------------------------------#

class boot_up():
    def __init__(self):
        self.startup()


    
    
    def vldt(self):
        print('Choose Valid Options')
        print('For Exploring The Program type y or n for exit')
        try:
            vld =  input(':I:N:P:U:T:>')
        except KeyboardInterrupt:
            self.clr_scr()
            print("Keyboard Interrupt")
            exit()
        if vld == 'y':
            self.startup()
        elif vld == 'n':
            self.clr_scr()
            exit()
        else:
            self.vldt()
    


    def startup(self):
        print('     1 Information Gathering')
        print('     2 Valnurability Analysis')
        print('     3 Web Aplication Analysis')
        print('     4 Exploitation Tools')
        print('     5 Maintaining Access(Under Dev)')
        print('     6 Post Exploitation(Under Dev)')
        print('     7 Password Cracking Tools(Under Dev)')
        print('     8 Wireless Tools(Under Dev)')
        print('     9 Sniffing And Spoofing(Under Dev)')
        print('     10 System Services(Under Dev)')
        print('     99 Exit')
        try:
            load = input(':I:N:P:U:T:> ')
            self.clr_scr()
        except KeyboardInterrupt:
            self.clr_scr()
            print("Keyboard Interrupt")
            exit()
        if load == "1":
            info_gather()
        elif load == '2':
            vuln_anl()
        elif load == '3':
            web_app_anl()
        elif load == '4':
            expl_tools()
        elif load == '5':
            maint_accs()
        elif load == '6':
            post_explt()
        elif load == '7':
            passwd_crack()
        elif load == '8':
            wirels_tools()
        elif load == '9':
            snif_an_spoof()
        elif load == '10':
            sys_serv()
        elif load == '99':
            exit()
        else:
            self.vldt()


    def clr_scr(self):
        os.system('clear')


#----------------------------------------------------------------------#
# Permissions
#----------------------------------------------------------------------#
def ask_permission():
    print(Fore.RED+' if you want to continue type'+Fore.GREEN+' y'+Fore.RED+' or'+Fore.GREEN+' n'+Fore.RED+' for exit\n'+Fore.RESET)
    try:
        chk = input(':I:N:P:U:T:> ')
    except KeyboardInterrupt:
        exit()
    if chk == 'y':
        boot_up()
    elif chk == 'n':
        exit()
    else:
        vldt()


def vldt():
    print("Choose Correct Options")
    ask_permission()

#----------------------------------------------------------------------------#
# Main Functon
#----------------------------------------------------------------------------#

if __name__ == "__main__":
    banner.banner()
    ask_permission()
    boot_up()
#---------------------------------------------------------------------------#
#
# THE END
#
#---------------------------------------------------------------------------#
