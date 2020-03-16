import os
import script


class bdf_proxy():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install bdfproxy')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/bdfproxy') or os.path.isdir('usr/bin/bdfproxy')

    def run(self):
        os.system('bdfproxy -help')
        print("<-----------This module is under development------------->")
        script.snif_an_spoof()


class better_cap():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install bettercap')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/bettercap') or os.path.isdir('usr/bin/bettercap')

    def run(self):
        os.system('bettercap -help')
        print("<--------This module is under development---------->")
        script.snif_an_spoof()


class ether_ape():
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
        script.snif_an_spoof()


class ettercap_graphical():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install ettercap-graphical')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/ettercap-graphical') or os.path.isdir('usr/bin/ettercap-graphical')

    def run(self):
        os.system('ettercap-graphical')
        script.snif_an_spoof()


class hamster():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install hamster')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/hamster') or os.path.isdir('usr/bin/hamster')

    def run(self):
        os.system('hamster')
        script.snif_an_spoof()


class kayak():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install kayak')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/kayak') or os.path.isdir('usr/bin/kayak')

    def run(self):
        os.system('kayak')
        script.snif_an_spoof()


class mac_changer():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install macchanger')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/macchanger') or os.path.isdir('usr/bin/macchanger')

    def run(self):
        os.system('macchanger -help')
        print("<----------This module is under development------------>")
        script.snif_an_spoof()


class mitm_proxy():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install mitmproxy')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/mitmproxy') or os.path.isdir('usr/bin/mitmproxy')

    def run(self):
        os.system('mitmproxy')
        script.snif_an_spoof()


class responder():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install responder')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/responder') or os.path.isdir('usr/bin/responder')

    def run(self):
        os.system('responder -help')
        print("<----------This module is under development---------->")
        script.snif_an_spoof()


class wireshark():
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
        script.snif_an_spoof()


class netsniff_ng():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install netsniff-ng')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/netsniff-ng') or os.path.isdir('usr/bin/netsniff-ng')

    def run(self):
        os.system('netsniff-ng -help')
        print("<----------This module is under development------------->")
        script.snif_an_spoof()
