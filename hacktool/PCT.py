import os
import script


class oph_crack():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install ophcrack')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/ophcrack') or os.path.isdir('usr/bin/ophcrack')

    def run(self):
        os.system('ophcrack')
        script.passwd_crack()



class john_ny():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install johnny')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/johnny') or os.path.isdir('usr/bin/johnny')

    def run(self):
        os.system('johnny')
        script.passwd_crack()



class pyrit():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install pyrit')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/pyrit') or os.path.isdir('usr/bin/pyrit')

    def run(self):
        os.system('pyrit -help')
        print("<-------------This Module Is Under Development ----------------->")
        script.passwd_crack()



class rainbow_crack():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install rainbowcrack')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/rcrack') or os.path.isdir('usr/bin/rcrack')

    def run(self):
        os.system('rcrack -help')
        print("<-------------This Module Is Under Development ----------------->")
        script.passwd_crack()




class X_hydra():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install xhydra')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/xhydra') or os.path.isdir('usr/bin/xhydra')

    def run(self):
        os.system('xhydra')
        script.passwd_crack()




class medusa():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install medusa')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/medusa') or os.path.isdir('usr/bin/medusa')

    def run(self):
        os.system('medusa -help')
        print("<-------------This Module Is Under Development ----------------->")
        script.passwd_crack()



class n_crack():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install ncrack')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/ncrack') or os.path.isdir('usr/bin/ncrack')

    def run(self):
        os.system('ncrack -help')
        print("<-------------This Module Is Under Development ----------------->")
        script.passwd_crack()




class cewl():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install cewl')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/cewl') or os.path.isdir('usr/bin/cewl')

    def run(self):
        os.system('cewl -help')
        print("<-------------This Module Is Under Development ----------------->")
        script.passwd_crack()



class crunch():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install crunch')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/crunch') or os.path.isdir('usr/bin/crunch')

    def run(self):
        os.system('crunch -help')
        print("<-------------This Module Is Under Development ----------------->")
        script.passwd_crack()




class pipal():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install pipal')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/pipal') or os.path.isdir('usr/bin/pipal')

    def run(self):
        os.system('pipal -help')
        print("<-------------This Module Is Under Development ----------------->")
        script.passwd_crack()

