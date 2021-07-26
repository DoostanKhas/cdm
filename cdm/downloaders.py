# Importing the required packages
"""
dcdm is a commend line Download Manger.
this file is dowloader classes"""

import requests


def HTTP_Handler(start, end, url, filename):

    # specify the starting and ending of the file
    headers = {"Range": "bytes=%d-%d" % (start, end)}

    # request the specified part and get into variable
    r = requests.get(url, headers=headers, stream=True)

    # open the file and write the content of the html page
    # into file.
    with open(filename, "r+b") as file:

        file.seek(start)
        var = file.tell()
        file.write(r.content)
