# -*- coding: utf-8 -*-

__author__ = 'luisramos'

import commands
import pprint

class Helpers:

    @classmethod
    def listenv(self, envs):
        for key in envs.keys():
            print '\033[1;35m Id: \033[1;36m%s' % key
            print '\033[1;35m Mail: \033[1;36m' + envs[key][0]
            print '\033[1;35m User: \033[1;36m' + envs[key][1]+'\n'
    @classmethod
    def setUser(self, envs, option):
        for env in envs:
            if envs.has_key(option):
                gitmail = 'git config --global user.email "%s" ' % envs[option][0]
                gituser = 'git config --global user.user "%s" ' % envs[option][1]
                ssh_add = 'ssh-add "%s"' % envs[option][2]
                commands.getstatusoutput(gitmail)
                commands.getstatusoutput(gituser)
                commands.getstatusoutput(ssh_add.replace('"',''))

                print '\033[1;35m -Set mail: \033[1;36m ' + envs[option][0]
                print '\033[1;35m -Set user: \033[1;36m ' + envs[option][1]
                print '\033[1;35m -Identify as: \033[1;36m ' + ssh_add
                break
            else:
                print '\033[1;33m \033[41m Dont exist this git enviroment use -list to see avaliable enviroment \033[m   \n'
                break

    @classmethod
    def errors(self):
        print '\033[1;33m \033[41m Please enter some option \033[m \n'

    @classmethod
    def menu(self):
        print '\033[1;35m Set Git enviroment: \033[1;36m 0 \033[m'
        print '\033[1;35m Add Git enviroment: \033[1;36m 1 \033[m'
        print '\033[1;35m Del Git enviroment: \033[1;36m 2 \033[m'
        print '\033[1;35m Mod Git enviroment: \033[1;36m 3 \033[m'
        print '\033[1;35m Exit:               \033[1;36m 4 \033[m'

