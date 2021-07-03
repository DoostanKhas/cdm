from os import write
import requests
import re

def getFilename_fromCd(cd):
    """
    Get filename from content-disposition
    """
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    print(fname)
    return fname[0]
url = 'https://files.virgool.io/upload/users/303/posts/heyqjauw1cmc/uusp0vm6zsph.jpeg'
r = requests.get(url, allow_redirects=True)
print(r.status_code)
filename = getFilename_fromCd(r.headers.get('content-disposition'))
with open ('filename', "wb") as file:
    file.write(r.content)
