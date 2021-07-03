
from os.path import exists

try:
    from cdm.downloaders.http import HTTP
expect ImportError:
    print("sorry I have a Problem! 😭")
    exit(0)

def httpTest():
    
    http = HTTP(url="https://cdn.realpython.com/static/real-python-logo.893c30edea53.svg")
    http.download()
    
    assert exists(http.getFilename) is True
