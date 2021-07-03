
from os.path import exists

from cdm.downloaders.http import HTTP

def httpTest():
    
    http = HTTP(url="https://cdn.realpython.com/static/real-python-logo.893c30edea53.svg")
    http.download()
    
    assert exists(http.getFilename) is True
