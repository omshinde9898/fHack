import os
import script


class exe_to_hex():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install exe2hex')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/exe2hex') or os.path.isdir('usr/bin/exe2hex')

    def run(self):
        os.system('exe2hex -help')
        print("<-------------This Module Is Under Development ----------------->")
        script.maint_accs()



class shelter():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install shelter')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/shelter') or os.path.isdir('usr/bin/shelter')

    def run(self):
        os.system('shelter -help')
        print("<-------------This Module Is Under Development ----------------->")
        script.maint_accs()



class backdoor_factory():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install backdoor-factory')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/backdoor-factory') or os.path.isdir('usr/bin/backdoor-factory')

    def run(self):
        os.system('backdoor-factory -help')
        print("<-------------This Module Is Under Development ----------------->")
        script.maint_accs()



class proxy_chains():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install proxychains')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/proxychains') or os.path.isdir('usr/bin/proxychains')

    def run(self):
        os.system('proxychains -help')
        print("<-------------This Module Is Under Development ----------------->")
        script.maint_accs()




class ni_shang():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install nishang')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/nishang') or os.path.isdir('usr/bin/nishang')

    def run(self):
        os.system('nishang -help')
        print("<-------------This Module Is Under Development ----------------->")
        script.maint_accs()




class wee_vely():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install weevely')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/weevely') or os.path.isdir('usr/bin/weevely')

    def run(self):
        os.system('weevely -help')
        print("<-------------This Module Is Under Development ----------------->")
        script.maint_accs()



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
        print("<-------------This Module Is Under Development ----------------->")
        script.maint_accs()




class windows_binaries():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install windows-binaries')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/windows-binaries') or os.path.isdir('usr/bin/windows-binaries')

    def run(self):
        os.system('windows-binaries -help')
        print("<-------------This Module Is Under Development ----------------->")
        script.maint_accs()



