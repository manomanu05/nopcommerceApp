import configparser

config=configparser.RawConfigParser()
config.read(".\Configurations\config.ini")

class ReadConfig():

    @staticmethod
    def getApplicationURL():
        url=config.get('common info','base_url')
        return url

    @staticmethod
    def getUsermail():
        usermail = config.get('common info', 'usermail')
        return usermail

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password