import requests
import settings
import urllib
import hashlib
import xmltodict
from uuid import uuid4

class EndPointRequest(object):
    """
    GET or POST to an url

    More data on request: http://docs.python-requests.org/en/latest/
    """
    def __init__(self, url, payload=dict(), timeout=3, cookies=dict(), headers=dict()):

        self.url = url
        self.payload = payload
        self.timeout = timeout
        self.cookies = cookies
        self.headers = headers
        self.data = None

    def _get(self):
        """ Call the url using GET """
        data = requests.get(self.url, timeout=self.timeout, cookies=self.cookies, headers=self.headers)
        self.data = data

    def _post(self):
        """ POST to the url """
        data = requests.post(self.url, data=self.payload, timeout=self.timeout, cookies=self.cookies, headers=self.headers)        
        self.data = data

    def _put(self):
        """ PUT to the url """        
        data = requests.put(self.url, data=self.payload, timeout=self.timeout, cookies=self.cookies, headers=self.headers)        
        self.data = data

    def _patch(self):
        """ PATCH to the url """
        data = requests.patch(self.url, data=self.payload, timeout=self.timeout, cookies=self.cookies, headers=self.headers)        
        self.data = data

    def _delete(self):
        data = requests.delete(self.url, data=self.payload, timeout=self.timeout, cookies=self.cookies, headers=self.headers)
        self.data = data

    def get_xml(self):
        self._get()

        if self.data:
            return xmltodict.parse(self.data.text)

    def get_json(self):
        """
        return the response data as json
        """
        self._get()

        if self.data:
            return self.data.json()

    def post(self):
        """
        Send a POST and returns the respose as json
        """
        self._post()

        if self.data:
            return self.data.json()

    def put(self):
        """
        Send a PUT and returns the respose as json
        """
        self._put()

        if self.data:
            return self.data.json()

    def patch(self):
        """
        Send a PATCH and returns the respose as json
        """
        self._patch()

        if self.data:
            return self.data.json()

    def delete(self):
        self._delete()

        if self.data:
            return self.data
