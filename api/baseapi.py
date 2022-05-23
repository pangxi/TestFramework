import requests


class BaseAPI:

    def requests_http(self,req):
        r = requests.request(**req)
        return r