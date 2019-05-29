from Log import *
from IpApi import *


def main():
    ipapi = IpApi()
    w_api = WeatherApi(ipapi)
    n_api = NewsApi(ipapi)
    Log(ipapi).check_api()
    Log(w_api).check_api()
    Log(n_api).check_api()


if __name__ == '__main__':
    main()
