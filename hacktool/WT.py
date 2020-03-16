import os
import script


class air_geddon():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install airgeddon')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/airgeddon') or os.path.isdir('usr/bin/airgeddon')

    def run(self):
        os.system('airgeddon')
        script.wirels_tools()


class ghost_phisher():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install ghostphisher')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/ghostphisher') or os.path.isdir('usr/bin/ghostphisher')

    def run(self):
        os.system('ghostphisher')
        script.wirels_tools()


class wifite():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install wifite')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/wifite') or os.path.isdir('usr/bin/wifite')

    def run(self):
        os.system('wifite')
        script.wirels_tools()


class inspectrum():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install inspectrum')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/inspectrum') or os.path.isdir('usr/bin/inspectrum')

    def run(self):
        os.system('inspectrum')
        script.wirels_tools()


class reaver():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install reaver')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/reaver') or os.path.isdir('usr/bin/reaver')

    def run(self):
        os.system('reaver -help')
        print("<-------------This module is under development--------------->")
        script.wirels_tools()


class aircrack():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install aircrack-ng')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/aircrack-ng') or os.path.isdir('usr/bin/aircrack-ng')

    def run(self):
        os.system('aircrack-ng -help')
        print("<-----------This module is under development------------->")
        print("<-----------All Aircrack tools will be available after update------------->")
        script.wirels_tools()
