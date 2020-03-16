
from colorama import Fore
import os
import script

class nmap_scan():
    def __init__(self):
        self.inst()


    def chk_install(self):
        return os.path.isfile('/usr/bin/nmap') or os.path.isdir('/etc/bin/nmap')


    def inst(self):
        if not self.chk_install():
            os.system('sudo apt-get install nmap')
            nmap_scan()
        else:
            self.run()
            script.boot_up()
    

    def vldt(self):
        print("Choose Correct Options")
        nmap_scan()

    def run(self):
        print(Fore.RED)
        print('1 Normal Scan')
        print('2 Aggresive Scan')
        print('3 OS FingerPrinting')
        print('99 Back')
        print(Fore.RESET)

        try:
            inp_scan = input(':I:N:P:U:T:>')
        except KeyboardInterrupt :
            print("Keyboard Interrupt")
            script.info_gather()
        if inp_scan == '1':
            try:
                target = input('Give The URL Or Ip Of Target :> ')

                os.system('nmap '+target)
                nmap_scan()
            except KeyboardInterrupt:
                print("\n KeyboardInterrupt \n")
                nmap_scan()
        elif inp_scan == '2':
            try:
                target = input('Give The URL Or Ip Of Target :> ')

                os.system('nmap -A '+target)
                nmap_scan()
            except KeyboardInterrupt :
                print("Keyboard Interrupt")
                nmap_scan()
        elif inp_scan == '3':
            try:
                target = input('Give The URL Or Ip Of Target :> ')

                os.system('nmap -O '+target)
                nmap_scan()
            except KeyboardInterrupt :
                nmap_scan()
        elif inp_scan == '99':
            script.info_gather()
        else:
            self.vldt()


    


class recon_scan():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install recon-ng')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/recon-ng') or os.path.isdir('usr/bin/recon-ng')

    def run(self):
        os.system('recon-ng')
        script.info_gather()



class dmitry_scan():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install dmitry')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/dmitry') or os.path.isdir('usr/bin/dmitry')

    def vldt(self):
        print("Choosse Correct Options")
        self.run()

    def run(self):
        print('Which Scan With Dmitry \n')
        print('1 Normal Scan')
        print('2 Whois lookup')
        print('3 Retrive netcracft.com info')
        print('4 Search for possible subdomains')
        print('5 Search for possible emails')
        print('6 TCP Port scan')
        print('7 TCP Port scan for filtered ports')
        print('99 Back')
        try:
            dmitry_inp = input(':I:N:P:U:T:> ')
        except KeyboardInterrupt:
            script.info_gather()
        if dmitry_inp == '1':
            try:
                dtarget = input('Give us target IP or Domain:> ')
            except KeyboardInterrupt:
                print("Keyboard Interrupt")
                self.run()
            os.system('dmitry '+dtarget)
            dmitry_scan()
        elif dmitry_inp == '2':
            try:
                dtarget = input('Give us target IP or Domain:> ')
                who_inp = input('Target is IP Or Domain(i/d):> ')
            except KeyboardInterrupt:
                self.run()
            if who_inp == 'i':
                os.system('dmitry -i '+dtarget)
                dmitry_scan()
            elif who_inp == 'd':
                os.system('dmitry -w '+dtarget)
                dmitry_scan()
            else:
                print('Choose Correct Options')
                dmitry_scan()
        elif dmitry_inp == '3':
            try:
                dtarget = input('Give us target IP or Domain:> ')
            except KeyboardInterrupt:
                print("Keyboard Interrupt")
                dmitry_scan()
            os.system('dmitry -n '+dtarget)
            dmitry_scan()
        elif dmitry_inp == '4':
            try:
                dtarget = input('Give us target IP or Domain:> ')
            except KeyboardInterrupt:
                print("Keyboard Interrupt")
                dmitry_scan()
            os.system('dmitry -s '+dtarget)
            dmitry_scan()
        elif dmitry_inp == '5':
            try:
                dtarget = input('Give us target IP or Domain:> ')
            except KeyboardInterrupt:
                print("Keyboard Interrupt")
                dmitry_scan()
            os.system('dmitry -e '+dtarget)
            dmitry_scan()
        elif dmitry_inp == '6':
            try:
                dtarget = input('Give us target IP or Domain:> ')
            except KeyboardInterrupt:
                print("Keyboard Interrupt")
                dmitry_scan()
            os.system('dmitry -p '+dtarget)
            dmitry_scan()
        elif dmitry_inp == '7':
            try:
                dtarget = input('Give us target IP or Domain:> ')
            except KeyboardInterrupt:
                print("keyboard Interrupt")
                dmitry_scan()
            os.system('dmitry -f '+dtarget)
            dmitry_scan()
        elif dmitry_inp == '99':
            script.info_gather()
        else:
            self.vldt()



class ike_scan():
    def __init__(self):
        print("Under Development")


class netdisc_scan():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install netdiscover')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/netdiscover') or os.path.isdir('usr/bin/netdiscover')

    def vldt(self):
        print("Choose Correct Options")
        netdisc_scan()

    def run(self):
        print('Choose Options From Following')
        print('1 Device : Your Network Interface')
        print('2 Range : scan given range')
        print('3 File : scan list of ranges')
        print('4 Passive Mode : do not send annything')
        print('5 File : scan list of MACs')
        print('6 AutoScan')
        print('99 Back')
        try:
            net_inp = input(':I:N:P:U:T:> ')
        except KeyboardInterrupt:
            print("Keyboard Interrupt\n")
            script.info_gather()
        if net_inp == '1':
            try:
                net_interface = input('Network Device :> ')
                os.system('netdiscover -i '+net_interface)
                netdisc_scan()
            except KeyboardInterrupt:
                print("Keyboard interrupt\n")
                netdisc_scan()
        elif net_inp == '2':
            try:
                net_ip = input('Enter Range (ex. 0.0.0.0/24,/16):> ')
                os.system('netdiscover -r '+net_ip)
                netdisc_scan()
            except KeyboardInterrupt:
                print("Keyboard Interrupt\n")
                netdisc_scan()
        elif net_inp == '3':
            try:
                net_ipath = input('Enter path of file:> ')
                os.system('netdiscover -l '+net_ipath)
                netdisc_scan()
            except KeyboardInterrupt:
                print("Keyboard Interrupt")
                netdisc_scan()
        elif net_inp == '4':
            try:
                net_pass = input('Enter Target :> ')
                os.system('netdiscover -p '+net_pass)
                netdisc_scan()
            except KeyboardInterrupt:
                print("Keyboard Interrupt")
                netdisc_scan()
        elif net_inp == '5':
            try:
                net_mpass = input('Enter Path of File :> ')
                os.system('netdiscover -m '+net_mpass)
                netdisc_scan()
            except KeyboardInterrupt:
                print("Keyboard Interrupt")
                netdisc_scan
        elif net_inp == '99':
            script.info_gather()
        else:
            self.vldt()



class wire_scan():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install wireshark')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/wireshark') or os.path.isdir('usr/bin/wireshark')

    def run(self):
        os.system('wireshark')
        script.info_gather()




class zen_scan():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install zenmap')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/zenmap') or os.path.isdir('usr/bin/zenmap')

    def run(self):
        os.system('zenmap')
        script.info_gather()




class maltego_scan():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install maltego')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/maltego') or os.path.isdir('usr/bin/maltego')

    def run(self):
        os.system('maltego')
        script.info_gather()




class ether_ape_scan():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install etherape')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/etherape') or os.path.isdir('usr/bin/etherape')

    def run(self):
        os.system('etherape')
        script.info_gather()



class enum_for_linux():
    def __init__(self):
        
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install enum4linux')
            self.run()
        else:
            self.run()

    def vldt(self):
        print("Choose Correct Options")
        enum_for_linux()

    def chk_install(self):
        return os.path.isfile('/bin/enum4linux') or os.path.isdir('usr/bin/enum4linux')

    def run(self):
        print('Choose Correct Options')
        print('1 For full scan')
        print('2 Get Userlist')
        print('3 Get Machine list')
        print('4 Get Sharelist')
        print('5 Get Group & Member list')
        print('6 Combined 2 & 4')
        print('7 Get OS Information')
        print('8 Get Printer information')
        print('9 Do nmblookup')
        print('99 Back')
        try:
            enum_inp = input(':I:N:P:U:T:> ')
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            script.info_gather()
        
        if enum_inp == '1':
            try:
                etarget = input('Give Us Target:> ')
                os.system('enum4linux -a '+etarget)
                enum_for_linux()
            except KeyboardInterrupt:
                print("Keyboard Interrupt")
                enum_for_linux()
        elif enum_inp == '2':
            try:
                etarget = input('Give Us Target:> ')
                os.system('enum4linux -U '+etarget)
                enum_for_linux()
            except KeyboardInterrupt:
                print("Keyboard Interrupt")
                enum_for_linux()
        elif enum_inp == '3':
            try:
                etarget = input('Give Us Target:> ')
                os.system('enum4linux -M '+etarget)
                enum_for_linux()
            except KeyboardInterrupt:
                print("Keyboard Interrupt")
                enum_for_linux()
        elif enum_inp == '4':
            try:
                etarget = input('Give Us Target:> ')
                os.system('enum4linux -S '+etarget)
                enum_for_linux()
            except KeyboardInterrupt:
                print("Keyboard Interrupt")
                enum_for_linux()
        elif enum_inp == '5':
            try:
                etarget = input('Give Us Target:> ')
                os.system('enum4linux -G '+etarget)
                enum_for_linux()
            except KeyboardInterrupt:
                print("Keyboard Interrupt")
                enum_for_linux()
        elif enum_inp == '6':
            try:
                etarget = input('Give Us Target:> ')
                os.system('enum4linux -d '+etarget)
                enum_for_linux()
            except KeyboardInterrupt:
                print("Keyboard Interrupt")
                enum_for_linux()
        elif enum_inp == '7':
            try:
                etarget = input('Give Us Target:> ')
                os.system('enum4linux -o '+etarget)
                enum_for_linux()
            except KeyboardInterrupt:
                print("Keyboard Interrupt")
                enum_for_linux()
        elif enum_inp == '8':
            try:
                etarget = input('Give Us Target:> ')
                os.system('enum4linux -i '+etarget)
                enum_for_linux()
            except KeyboardInterrupt:
                print("Keyboard Interrupt")
                enum_for_linux()
        elif enum_inp == '9':
            try:
                etarget = input('Give Us Target:> ')
                os.system('enum4linux -n '+etarget)
                enum_for_linux()
            except KeyboardInterrupt:
                print("Keyboard Interrupt")
                enum_for_linux()
        elif enum_inp == '99':
            script.info_gather()
        else:
            self.vldt()

