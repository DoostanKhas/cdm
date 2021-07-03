
import re

from requests import get


class HTTP:
    
    def __init__(self, url, path=""):
        self.url = url
        self.path = path
    
    
    def download (self):
        response = get(self.url, allow_redirects=True)

        filename = self.getFilename(response.headers.get('content-disposition'))

        with open (self.path+filename, "wb") as file:
            file.write(response.content)


    @staticmethod
    def getFilename(content):
        """
        Get filename from content-disposition
        """
        if not content:
            return None
        fname = re.findall('filename=(.+)', content)
        if len(fname) == 0:
            return "file"
        return fname[0]
