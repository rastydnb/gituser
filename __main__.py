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
        helper.Helpers.setUser(envs, envid)
    elif menuopt=='1':
        other = 'y'
        while other == 'y' or other == '':
            envid = raw_input('Enter env id: ')
            name = raw_input('Enter name: ')
            mail = raw_input('Enter email: ')
            sshkey = raw_input('Enter your Own ssh-key or Generate one [O/G]')
            exit = 0
            while exit == 0:
                os.system('clear')
                if sshkey != 'G' and sshkey != 'O':
                    sshkey = raw_input('Incorrect option enter "O" or "G":')

                if sshkey == 'G':
                    key = ssh.Ssh.createKey(mail)
                    exit = 1
                elif sshkey == 'O':
                    key = raw_input('Enter ssh key path: ')
                    exit = 1

            envs[envid] = [mail, name, key]
            other = raw_input('Add other env[y/n]: ')
        xml.createConfigFile(envs)
        os.system('clear')
        helper.Helpers.listenv(envs)
        helper.Helpers.menu()
        menuopt = raw_input('Enter option: ')
    elif menuopt == '2':
        envid = raw_input('Enter env id tu delete: ')
        del envs[envid]
        xml.createConfigFile(envs)
        os.system('clear')
        helper.Helpers.listenv(envs)
        helper.Helpers.menu()
        menuopt = raw_input('Enter option: ')
    elif menuopt == '3':
        envid = raw_input('Enter env id tu modify: ')
        del envs[envid]
        envid = raw_input('Enter env id: ')
        name  = raw_input('Enter name: ')
        mail  = raw_input('Enter email: ')
        sshkey = raw_input('[y/n]: ')
        if sshkey == 'y':
            ssh.Ssh.createKey(mail)
        envs[envid] = [mail, name, sshkey]
        xml.createConfigFile(envs)
        os.system('clear')
        helper.Helpers.listenv(envs)
        helper.Helpers.menu()
        menuopt = raw_input('Enter option: ')
    elif menuopt == '4':
        exit()





















#xml = xmlmanager.XmlManager()
#xml.createConfigFile(envs)
#xml.loadXmlconfig()
#ssh.Ssh.createKey('olaola')



