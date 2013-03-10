# -*- coding: utf-8 -*-


__author__ = 'luisramos'


from xml.dom.minidom import Document, parse
import os
import pprint

class XmlManager:

    configpath = os.getenv("HOME")+'/.GitUserConfig/'
    configfilename = 'guc.xml'
    envs = {}
    list = []

    def __init__(self):
        if os.path.exists(self.configpath) is False:
            os.mkdir(self.configpath)
        if os.path.exists(self.configpath+self.configfilename) is False:
            xml_handle = open(self.configpath+self.configfilename, 'w')
            xmlconfig = Document()
            configmaintag = xmlconfig.createElement('xmlconfig')
            xmlconfig.appendChild(configmaintag)
            xmlconfig.writexml(xml_handle, indent="\n", addindent="  ", newl="  ")

            xml_handle.close()




    @classmethod
    def createConfigFile(self, envs):
        xmlconfig = Document()
        configmaintag = xmlconfig.createElement('xmlconfig')
        xmlconfig.appendChild(configmaintag)

        for key in envs:
            env = xmlconfig.createElement('env')
            env.setAttribute('id', key )
            configmaintag.appendChild(env)

            name = xmlconfig.createElement('name')
            name.appendChild(xmlconfig.createTextNode(envs[key][1]))
            email = xmlconfig.createElement('mail')
            email.appendChild(xmlconfig.createTextNode(envs[key][0]))
            sshkey = xmlconfig.createElement('sshkey')
            sshkey.appendChild(xmlconfig.createTextNode(envs[key][2]))

            env.appendChild(name)
            env.appendChild(email)
            env.appendChild(sshkey)

            xml_handle = open(self.configpath+self.configfilename, 'wb')
            xmlconfig.writexml(xml_handle, indent="\n", addindent="  ", newl="  ")
            xml_handle.close()


    @classmethod
    def loadXmlconfig(self):
        xmlparser = parse(self.configpath+self.configfilename)
        self.handleXml(xmlparser)
        return self.envs


    @classmethod
    def handleXml(self, xml):
        subroot = xml.getElementsByTagName("env")
        self.handleEnvs(subroot)

    @classmethod
    def handleEnvs(self, configenv):
        for env in configenv:
            self.handleEnv(env)
            self.list = []

    @classmethod
    def handleEnv(self, env):
        name     = self.getElement(env.getElementsByTagName("name")[0])
        name = name.replace('\n','')
        name = name.replace(' ','')
        mail  = self.getElement(env.getElementsByTagName("mail")[0])
        mail = mail.replace('\n','')
        mail = mail.replace(' ','')
        sshkey   = self.getElement(env.getElementsByTagName("sshkey")[0])
        sshkey = sshkey.replace('\n','')
        sshkey = sshkey.replace(' ','')

        envid = self.getElement(env.getAttributeNode('id'))


        self.list.append(name)
        self.list.append(mail)
        self.list.append(sshkey)
        self.envs[envid]=[mail, name, sshkey]

    @classmethod
    def getElement(self, element):
        return self.getText(element.childNodes)

    @classmethod
    def getText(self, nodelist):
        rc = ""
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE:
                rc = rc + node.data
        return rc
    @classmethod
    def configExist(self):
        return os.path.exists(self.configpath+self.configfilename)

