# -*- coding: utf-8 -*-


__author__ = 'luisramos'

from simplersa import RSAKeypair, RSAPublicKey
import os


class Ssh:

    #Create rsa file in .ssh
    @classmethod
    def createKey(self, name):
        if os.path.exists(os.getenv("HOME")+'/.ssh/'):
            key = RSAKeypair.generate()
            file = os.getenv("HOME")+'/.ssh/'+name
            key.save(file )
            return file
        else:
            return False

    #Create rsa file in optional path
    @classmethod
    def createKeyInPath(self, name, path):
        if path:
            key = RSAKeypair.generate()
            file = path+'/'+name
            key.save(file )
            return True
        else:
            return False
