import requests

class DefectDojoSession(requests.Session):
    """
    DefectDojoSession class inherits from requests.Session
    """
    def __init__(self, url, key):
        requests.Session.__init__(self)
        self.url = url
        self.key = key
        self.headers = {'Content-Type': 'application/json',
                        'Accept': 'application/json',
                        'Authorization': 'Token ' + self.key}
        self.session = requests.Session()
        self.session.headers.update(self.headers)
