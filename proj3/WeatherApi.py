from ApiProxy import *


class WeatherApi(ApiProxy):
    def __init__(self, myApi):
        self.country = myApi.country
        self.latitude = myApi.latitude
        self.longitude = myApi.longitude
        self.ip = myApi.ip
        self.choice = None
        self.status = None
        self.do_stuff()

    def do_stuff(self):
        request = requests.get('https://www.metaweather.com/api/location/search/?lattlong={},{}'.format(self.latitude,
                                                                                                        self.longitude))
        data = request.json()
        if self.check_status(request):
            self.status = request.status_code
            if len(data) > 1:
                print("----------------------------------------------------------")
                pprint("We Could not Find Your City but Here are close cities'")
                print("----------------------------------------------------------")
                for i in range(len(data)):
                    title = data[i]['title']
                    woeid = data[i]['woeid']
                    print("City:{}, Woeid:{}\n".format(title, woeid))
                self.choice = input("Type woeid to look weather conditions:\n")
                print("-----------------------------------------------------")
                newRequest = requests.get('https://www.metaweather.com/api/location/{}'.format(self.choice))
                newData = newRequest.json()
                if self.check_status(newRequest):
                    self.status = newRequest.status_code
                    air_pressure = newData['consolidated_weather'][0]['air_pressure']
                    print("Air Pressure is:{}\n".format(air_pressure))
                    predict = newData['consolidated_weather'][0]['predictability']
                    temperature = newData['consolidated_weather'][0]['the_temp']
                    print("Temperature is:{} with %{} predictability\n".format(temperature, predict))
                    weather_condition = newData['consolidated_weather'][0]['weather_state_name']
                    print("Weather Condition is {}\n".format(weather_condition))
                else:
                    self.status = newRequest.status_code
                    print("Something Went Wrong")

            else:
                valid_data = data['woeid']
                request2 = requests.get('https://www.metaweather.com/api/location/{}'.format(valid_data))
                data2 = request2.json()

                if self.check_status(request2):
                    self.status = request2.status_code
                    print("Weather Conditions in {}\n".format(self.country))
                    print("Air Pressure is :{}\n".format(data2['consolidate_weather'][0]['air_pressure']))
                    print("Temperature is:{}\n".format(data2['consolidated_weather'][0]['the_temp']))
                    print("Weather Condition is {}\n".format(data2['consolidated_weather'][0]['weather_state_name']))
                else:
                    self.status = request2.status_code
                    print("Something Went Wrong")
        else:
            self.status = request.status_code
            print("Something Went Wrong")
        print("------------------------------------")
