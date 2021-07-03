
import re

from requests import get


class HTTP:
    
    def __init__(self, url, path=""):
        self.url = url
        self.path = path
    
    
    def download (self):
        response = get(self.url, allow_redirects=True)

        filename = getFilename(response.headers.get('content-disposition')) if not None else "file"

        with open (self.path+filename, "wb") as file:
            file.write(r.content)


    @staticmethod
    def getFilename(content):
        """
        Get filename from content-disposition
        """
        if not content:
            return None
        fname = re.findall('filename=(.+)', content)
        if len(fname) == 0:
            return None
        return fname[0]
