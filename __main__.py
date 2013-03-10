#!/usr/bin/python

# -*- coding: utf-8 -*-

__author__ = 'luisramos'


import sys
import os
import ssh
import helper
import xmlmanager
import pprint


xml = xmlmanager.XmlManager()
envs = xml.loadXmlconfig()



#set command arg
if len(sys.argv)!=1:
    #Set credential
    helper.Helpers.setUser(envs, sys.argv[1])
else:
    os.system('clear')
    option=0
    #List available enviroment
    helper.Helpers.listenv(envs)
    helper.Helpers.menu()
    menuopt = raw_input('Enter option: ')

    if menuopt == '0':
        envid = raw_input('Enter envs id to set it: ')
    elif menuopt=='1':
        other = 'y'
        while other == 'y' or other == '':
            envid = raw_input('Enter env id: ')
            name = raw_input('Enter name: ')
            mail = raw_input('Enter email: ')
            sshkey = raw_input('Generate RSA public and private key[y/n]:')
            exit = True
            if sshkey == 'y':
                exit = False
            elif sshkey == 'n':
                exit = False
            while exit :
                print 'Enter[y/n]'
                sshkey = raw_input('Generate RSA public and private key[y/n]:')
                if sshkey == 'y':
                    exit = False
                elif sshkey == 'n':
                    exit = False

            print sshkey == 'Y'
            print sshkey
            if sshkey == 'y':
                print 'momia'
                ssh.Ssh.createKey(mail)
            envs[envid] = [mail, name, sshkey]
            other = raw_input('Add other env[y/n]: ')
        xml.createConfigFile(envs)
        os.system('clear')
    elif menuopt == '2':
        envid = raw_input('Enter env id tu delete: ')
        del envs[envid]
        xml.createConfigFile(envs)
        os.system('clear')
    elif menuopt == '3':
        envid = raw_input('Enter env id tu modify: ')
        del envs[envid]
        envid = raw_input('Enter env id: ')
        name  = raw_input('Enter name: ')
        mail  = raw_input('Enter email: ')
        sshkey = raw_input('[y/n]: ')
        if sshkey == 'Y':
            ssh.Ssh.createKey(mail)
        envs[envid] = [mail, name, sshkey]
        xml.createConfigFile(envs)
        os.system('clear')





















#xml = xmlmanager.XmlManager()
#xml.createConfigFile(envs)
#xml.loadXmlconfig()
#ssh.Ssh.createKey('olaola')



