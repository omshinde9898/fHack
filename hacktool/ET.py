import os
import script


class meta_sploit():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install metasploit')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/metasploit') or os.path.isdir('usr/bin/metasploit')

    def run(self):
        os.system('msfconsole')
        script.expl_tools()



class termi_test():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install termineter')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/termineter') or os.path.isdir('usr/bin/termineter')

    def run(self):
        os.system('termineter -help')
        print("<----------This Is Under Development------------>")
        script.expl_tools()



class web_sploit():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install websploit')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/websploit') or os.path.isdir('usr/bin/websploit')

    def run(self):
        os.system('websploit')
        script.expl_tools()



class hexor_base():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install hexorbase')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/hexorbase') or os.path.isdir('usr/bin/hexorbase')

    def run(self):
        os.system('hexorbase')
        script.expl_tools()



class o_scanner():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install oscanner')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/oscanner') or os.path.isdir('usr/bin/oscanner')

    def run(self):
        os.system('oscanner -help')
        print("<-------------This Is Under Development-------------->")
        script.expl_tools()


class sandi_gui():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install sandi-gui')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/sandi-gui') or os.path.isdir('usr/bin/sandi-gui')

    def run(self):
        os.system('sandi-gui')
        script.expl_tools()



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
        script.expl_tools()



class s_e_toolkit():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install setoolkit')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/setoolkit') or os.path.isdir('usr/bin/setoolkit')

    def run(self):
        os.system('setoolkit')
        script.expl_tools()



class com_mix():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install commix')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/commix') or os.path.isdir('usr/bin/commix')

    def run(self):
        os.system('commix --wazard')
        script.expl_tools()


class sql_map():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install sqlmap')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/sqlmap') or os.path.isdir('usr/bin/sqlmap')

    def run(self):
        os.system('sqlmap -help')
        print("<-------------This Module Is Under Development ----------------->")
        script.expl_tools()



