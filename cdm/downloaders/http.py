
import re

from requests import get


class HTTP:
    
    def __init__(self, url, path=""):
        self.url = url
        self.path = path
    
    
    def download (self):
        response = get(url, allow_redirects=True)

        filename = getFilename_fromCd(response.headers.get('content-disposition'))

        with open (path+filename, "wb") as file:
            file.write(r.content)


    @staticmethod
    def getFilename(content):
        """
        Get filename from content-disposition
        """
        if not cd:
            return None
        fname = re.findall('filename=(.+)', cd)
        if len(fname) == 0:
            return None
        return fname[0]
