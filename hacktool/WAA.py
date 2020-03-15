import os
import script


class burpsuite_scan():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install burpsuite')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/burpsuite') or os.path.isdir('usr/bin/burpsuite')

    def run(self):
        os.system('burpsuite')
        script.web_app_anl()



class owasp_scan():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install owasp-zap')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/owasp-zap') or os.path.isdir('usr/bin/owasp-zap')

    def run(self):
        os.system('owasp-zap')
        script.web_app_anl()



class wp_scan():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install wpscan')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/wpscan') or os.path.isdir('usr/bin/wpscan')

    def vldt(self):
        print("Choose Correct Options")
        self.run()

    def run(self):
        print("Choose Following Options")
        print("     1 Enumerate Target")
        print("     2 Get Password File Path")
        print("     3 Get UserName List")
        print("     99 Back")
        try:
            wp_inp = input(":I:N:P:U:T:> ")
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            script.web_app_anl()

        if wp_inp == '1':
            try:
                target = input("Give Us Target's URL :> ")
                os.system("wpscan -e -url "+target)
            except KeyboardInterrupt:
                print("Keyboard interrupt")
                self.run()
        elif wp_inp == '2':
            try:
                target = input("Give Us Target's URL :> ")
                os.system("wpscan -P -url "+target)
            except KeyboardInterrupt:
                print("Keyboard interrupt")
                self.run()
        elif wp_inp == '3':
            try:
                target = input("Give Us Target's URL :> ")
                os.system("wpscan -U -url "+target)
            except KeyboardInterrupt:
                print("Keyboard interrupt")
                self.run()
        elif wp_scan == '99':
            script.web_app_anl()
        else:
            self.vldt()

        script.web_app_anl()



class commix_scan():
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
        os.system('commix --wizard')
        script.web_app_anl()



class httrack_scan():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install httrack')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/httrack') or os.path.isdir('usr/bin/httrack')

    def run(self):
        os.system('httrack')
        script.web_app_anl()


class skipfish_scan():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install skipfish')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/skipfish') or os.path.isdir('usr/bin/skipfish')

    def run(self):
        os.system('skipfish -h')
        print("<------------This Tool Is Under development And Will Be Avilable In Next Update------------->")
        script.web_app_anl()



class webscarab_scan():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install webscarab')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/webscarab') or os.path.isdir('usr/bin/webscarab')

    def run(self):
        os.system('webscarab')
        script.web_app_anl()



class cutycapt_scan():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install cutycapt')
            self.run()
        else:
            self.run()

    def chk_install(self):
        return os.path.isfile('/bin/cutycapt') or os.path.isdir('usr/bin/cutycapt')

    def run(self):
        os.system('cutycapt -help')
        print("<------------This Tool Is Under development And Will Be Avilable In Next Update------------->")
        script.web_app_anl()



