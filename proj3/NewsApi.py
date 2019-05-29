from ApiProxy import *


class NewsApi(ApiProxy):
    def __init__(self, myApi):
        self.country = myApi.country
        self.ip = myApi.ip
        self.status = None
        self.request = requests.get('https://api.currentsapi.services/v1/search?country={}'.format(self.country),
                         headers={
                             "Authorization": 'hcROEOsU1TNt_vt_DMXLlqQHoJszcst1DMH8p-x5xqEklPdj'
                         })
        self.do_stuff()

    def do_stuff(self):
        data = self.request.json()
        if self.check_status(self.request):
            print("All news from your country which is {}\n".format(self.country))
            print("--------------------------------------------------")
            for i in data['news']:
                author = i['author']
                title = i['title']
                url = i['url']
                print("{} by {} in {}\n".format(title, author, url))

        else:
            self.status = self.request.status_code
            print("Something Went Wrong")

        print("-----------------------------")
