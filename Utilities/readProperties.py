import configparser

config=configparser.RawConfigParser()
config.read("C:\\Users\\lijin\\PycharmProjects\\Zoopla\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getLocation():
        place=config.get('common info','location')
        return place

