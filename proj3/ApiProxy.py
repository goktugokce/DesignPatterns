from abc import *
import requests
from pprint import pprint


class ApiProxy(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def do_stuff(self):
        pass

    def check_status(self, request):
        if request.status_code == 200:
            return True
        else:
            return False