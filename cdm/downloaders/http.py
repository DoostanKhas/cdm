# Importing the required packages
import threading

import requests


# The below code is used for each chunk of file handled by each thread for downloading
# the content from specified location to storage
def HTTP_Handler(start, end, url, filename):

    # specify the starting and ending of the file
    headers = {"Range": "bytes=%d-%d" % (start, end)}

    # request the specified part and get into variable
    r = requests.get(url, headers=headers, stream=True)

    # open the file and write the content of the html page
    # into file.
    with open(filename, "r+b") as f:

        f.seek(start)
        var = f.tell()
        f.write(r.content)
