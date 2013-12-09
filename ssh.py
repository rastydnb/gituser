# -*- coding: utf-8 -*-


__author__ = 'luisramos'

import os
from Crypto.PublicKey import RSA
from Crypto import Random
import base64



class Ssh:

    #Create rsa file in .ssh
    @classmethod
    def createKey(self, name):
        if os.path.exists(os.getenv("HOME")+'/.ssh/'):

            file = os.getenv("HOME")+'/.ssh/'+name

            keys = self.getkeys(name)

            handlepublic = open(os.getenv('HOME')+'/.ssh/'+name+'.pub', 'a')
            handleprivate = open(os.getenv('HOME')+'/.ssh/'+name, 'a')
            handlepublic.write(keys['public'])
            handleprivate.write(keys['private'])

            os.chmod(file, 0600)
            os.chmod(file+'.pub', 0600)


            return file
        else:
            return False

    #Create rsa file in optional path
    @classmethod
    def createKeyInPath(self, name, path):
        if path:
            #key = RSAKeypair.generate()
            #file = path+'/'+name
            #key.save(file )
            return True
        else:
            return False


    #Get encrypted string for public key and return it
    @classmethod
    def getkeys(self ,name):
        random_generator = Random.new().read

        key = RSA.generate(2048, random_generator)

        private = key.exportKey()

        # Create public key.
        ssh_rsa = '00000007' + base64.b16encode('ssh-rsa')

        # Exponent.
        exponent = '%x' % (key.e, )
        if len(exponent) % 2:
            exponent = '0' + exponent

        ssh_rsa += '%08x' % (len(exponent) / 2, )
        ssh_rsa += exponent

        modulus = '%x' % (key.n, )
        if len(modulus) % 2:
            modulus = '0' + modulus

        if modulus[0] in '89abcdef':
            modulus = '00' + modulus

        ssh_rsa += '%08x' % (len(modulus) / 2, )
        ssh_rsa += modulus

        public_key = 'ssh-rsa %s' % (base64.b64encode(base64.b16decode(ssh_rsa.upper())), )

        return {'public': public_key+' '+name, 'private': private}


