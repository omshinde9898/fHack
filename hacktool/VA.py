
import os
import script

class golis_test():
    def __init__(self):
        print("Under Development")



class afl_test():
    def __init__(self):
        print("Under Development")



class open_vas_test():
    def __init__(self):
        self.install()

    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install openvas')
            self.run()
        else:
            self.run()

    def vldt(self):
        print("Choose Correct Options")
        open_vas_test()

    def chk_install(self):
        return os.path.isfile('/bin/openvas') or os.path.isdir('/usr/bin/openvas')

    def run(self):
        print('1 OpenVAS Start')
        print('2 OpenVAS Stop')
        print('3 OpenVAS Initial Setup')
        print('99 Back')
        try:
            open_inp = input(':I:N:P:U:T:> ')
        except KeyboardInterrupt:
            script.vuln_anl()
        if open_inp == '1':
            os.system('openvas-start')
            open_vas_test()
        elif open_inp == '2':
            os.system('openvas-stop')
            open_vas_test()
        elif open_inp == '3':
            os.system('openvas-setup')
            open_vas_test()
        elif open_inp == '99':
            script.vuln_anl()
        else:
            self.vldt()




class lynis_test():
    def __init__(self):
        self.install()

    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install lynis')
            self.run()
        else:
            self.run()

    def vldt(self):
        print("Choose Correct Options")
        open_vas_test()

    def chk_install(self):
        return os.path.isfile('/bin/lynis') or os.path.isdir('/usr/bin/lynis')

    def run(self):
        print('1 Audit System')
        print('2 Audit Remote System')
        print('3 Audit Dockerfile')
        print('99 Back')
        try:
            lyn_inp = input(':I:N:P:U:T:> ')
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            script.vuln_anl()
        if lyn_inp == '1':
            os.system('lynis audit system')
            lynis_test()
        elif lyn_inp == '2':
            try:
                ltarget = input('Give Us IP Of Remote System:> ')
                os.system('lynis audit system remote '+ltarget)
                lynis_test()
            except KeyboardInterrupt:
                print("Keyboard Interrupt")
                lynis_test()
        elif lyn_inp == '3':
            try:
                doctarget = input('Give Us Path Of Docker File:> ')
                os.system('lynis audit system remote '+doctarget)
                lynis_test()
            except KeyboardInterrupt:
                print("Keyboard interrupt")
                lynis_test()
        elif lyn_inp == '99':
            script.vuln_anl()
        else:
            self.vldt()



