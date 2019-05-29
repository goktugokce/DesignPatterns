from ApiProxy import *
from IpApi import *
from NewsApi import *
from WeatherApi import *
import datetime


class weatherLog():
    def __init__(self):
        self.date = datetime.date.today()
        self.time = datetime.datetime.now()

    def writeLog(self, api):
        weatherfile = open("weatherapi.log", "a")
        weatherfile.write("-------------------------------------------\n")
        weatherfile.write("User With IP:{}\n".format(api.ip))
        weatherfile.write("Date:{}/\n".format(self.time))
        weatherfile.write("User's woeid:{}\n".format(api.choice))
        weatherfile.write("STATUS:{}\n".format(api.status))
        weatherfile.write("-------------------------------------------\n")


class ipLog:
    def __init__(self):
        self.date = datetime.date.today()
        self.time = datetime.datetime.now()

    def writeLog(self, api):
        ipapifile = open("ipapi.log", "a")
        ipapifile.write("-------------------------------------------\n")
        ipapifile.write("User With IP:{}\n".format(api.ip))
        ipapifile.write("Date:{}/\n".format(self.time))
        ipapifile.write("STATUS:{}\n".format(api.status))
        ipapifile.write("-------------------------------------------\n")


class newLog:
    def __init__(self):
        self.date = datetime.date.today()
        self.time = datetime.datetime.now()

    def writeLog(self, api):
        newsfile = open("newsapi.log", "a")
        newsfile.write("-------------------------------------------\n")
        newsfile.write("User With IP:{}\n".format(api.ip))
        newsfile.write("Date:{}\n".format(self.time))
        newsfile.write("STATUS:{}\n".format(api.status))
        newsfile.write("-------------------------------------------\n")


class Log(ApiProxy):
    def __init__(self, api):
        self.api = api
        self.n_log = newLog()
        self.w_log = weatherLog()
        self.ip_log = ipLog()

    def check_api(self):
        if isinstance(self.api, NewsApi):
            self.n_log.writeLog(self.api)
        elif isinstance(self.api, WeatherApi):
            self.w_log.writeLog(self.api)
        elif isinstance(self.api, IpApi):
            self.ip_log.writeLog(self.api)
