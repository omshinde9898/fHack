
import os
import script

class beef():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install beef')
            self.run()
        else:
            self.run()

    def vldt(self):
        print("Choose Correct Options")
        self.run()

    def chk_install(self):
        return os.path.isfile('/bin/beef') or os.path.isdir('usr/bin/beef')

    def run(self):
        print("Choose Action :")
        print("     1 Start beef")
        print("     2 Stop beef")
        print("     99 Back")
        try:
            loab = input(":I:N:P:U:T:> ")
            os.system("clear")
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            script.sys_serv()
        if loab == '1':
            os.system('beef start')
            script.sys_serv()
        elif loab == '2':
            os.system('beef stop')
        elif loab == '99':
            script.sys_serv()
        else:
            self.vldt()



class dradis():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install dradis')
            self.run()
        else:
            self.run()

    def vldt(self):
        print("Choose Correct Options")
        self.run()

    def chk_install(self):
        return os.path.isfile('/bin/dradis') or os.path.isdir('usr/bin/dradis')

    def run(self):
        print("Choose Action :")
        print("     1 Start dradis")
        print("     2 Stop dradis")
        print("     99 Back")
        try:
            loab = input(":I:N:P:U:T:> ")
            os.system("clear")
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            script.sys_serv()
        if loab == '1':
            os.system('dradis start')
            script.sys_serv()
        elif loab == '2':
            os.system('dradis stop')
        elif loab == '99':
            script.sys_serv()
        else:
            self.vldt()


class apache_two():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install apache2')
            self.run()
        else:
            self.run()

    def vldt(self):
        print("Choose Correct Options")
        self.run()

    def chk_install(self):
        return os.path.isfile('/bin/apache2') or os.path.isdir('usr/bin/apache2')

    def run(self):
        print("Choose Action :")
        print("     1 Start Apache2 server")
        print("     2 Stop Apache2 server")
        print("     99 Back")
        try:
            loab = input(":I:N:P:U:T:> ")
            os.system("clear")
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            script.sys_serv()
        if loab == '1':
            os.system('apache2 start')
            script.sys_serv()
        elif loab == '2':
            os.system('apache2 stop')
        elif loab == '99':
            script.sys_serv()
        else:
            self.vldt()



class open_vas():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install openvas')
            self.run()
        else:
            self.run()

    def vldt(self):
        print("Choose Correct Options")
        self.run()

    def chk_install(self):
        return os.path.isfile('/bin/openvas') or os.path.isdir('usr/bin/openvas')

    def run(self):
        print("Choose Action :")
        print("     1 Start OpenVAS")
        print("     2 Stop OpenVAS")
        print("     99 Back")
        try:
            loab = input(":I:N:P:U:T:> ")
            os.system("clear")
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            script.sys_serv()
        if loab == '1':
            os.system('openvas start')
            script.sys_serv()
        elif loab == '2':
            os.system('openvas stop')
        elif loab == '99':
            script.sys_serv()
        else:
            self.vldt()




class sshd():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install sshd')
            self.run()
        else:
            self.run()

    def vldt(self):
        print("Choose Correct Options")
        self.run()

    def chk_install(self):
        return os.path.isfile('/bin/sshd') or os.path.isdir('usr/bin/sshd')

    def run(self):
        print("Choose Action :")
        print("     1 Start SSH")
        print("     2 Stop SSH")
        print("     99 Back")
        try:
            loab = input(":I:N:P:U:T:> ")
            os.system("clear")
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            script.sys_serv()
        if loab == '1':
            os.system('sshd start')
            script.sys_serv()
        elif loab == '2':
            os.system('sshd stop')
        elif loab == '99':
            script.sys_serv()
        else:
            self.vldt()



class post_gre_sql():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install postgresql')
            self.run()
        else:
            self.run()

    def vldt(self):
        print("Choose Correct Options")
        self.run()

    def chk_install(self):
        return os.path.isfile('/bin/postgresql') or os.path.isdir('usr/bin/postgresql')

    def run(self):
        print("Choose Action :")
        print("     1 Start postgresql")
        print("     2 Stop postgresql")
        print("     99 Back")
        try:
            loab = input(":I:N:P:U:T:> ")
            os.system("clear")
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            script.sys_serv()
        if loab == '1':
            os.system('postgresql start')
            script.sys_serv()
        elif loab == '2':
            os.system('postgresql stop')
        elif loab == '99':
            script.sys_serv()
        else:
            self.vldt()



class x_plico():
    def __init__(self):
        os.system('clear')
        self.install()


    def install(self):
        if not self.chk_install():
            os.system('sudo apt-get install xplico')
            self.run()
        else:
            self.run()

    def vldt(self):
        print("Choose Correct Options")
        self.run()

    def chk_install(self):
        return os.path.isfile('/bin/xplico') or os.path.isdir('usr/bin/xplico')

    def run(self):
        print("Choose Action :")
        print("     1 Start xplico")
        print("     2 Stop xplico")
        print("     99 Back")
        try:
            loab = input(":I:N:P:U:T:> ")
            os.system("clear")
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            script.sys_serv()
        if loab == '1':
            os.system('xplico start')
            script.sys_serv()
        elif loab == '2':
            os.system('xplico stop')
        elif loab == '99':
            script.sys_serv()
        else:
            self.vldt()
