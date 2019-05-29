from ApiProxy import *
from Log import *


class IpApi(ApiProxy):
    def __init__(self):
        self.request = requests.get('https://ipapi.co/json/')
        self.ip = None
        self.city = None
        self.country = None
        self.latitude = None
        self.longitude = None
        self.status = self.request.status_code
        self.do_stuff()

    def do_stuff(self):
        data = self.request.json()
        if self.check_status(self.request):
            self.city = data['city']
            self.country = data['country']
            self.ip = data['ip']
            self.latitude = data['latitude']
            self.longitude = data['longitude']
            print("Welcome! You Are in {},{}\n".format(self.city, self.country))
            print("Trying to get your weather conditions...\n")

        else:
            self.status = self.request.status_code
            print("Something Went Wrong")
