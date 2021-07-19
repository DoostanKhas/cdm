"""
cdm is a commend line Download Manger.
this file is main file"""

from __future__ import print_function, unicode_literals

import threading

import click
import requests

from downloaders.http import HTTP_Handler
from logger import logger


@click.command(help="It downloads the specified file with specified name")
@click.option("--number_of_threads", default=4, help="No of Threads")
@click.option("--name", type=click.Path(), help="Name of the file with extension")
@click.argument("url_of_file", type=click.Path())
@click.pass_context
def download_file(ctx, url_of_file, name, number_of_threads):
    r = requests.head(url_of_file)
    if name:
        file_name = name
    else:
        file_name = url_of_file.split("/")[-1]
    try:
        file_size = int(r.headers["content-length"])
    except:
        print("Invalid URL")
        return

    part = int(file_size) // number_of_threads
    fp = open(file_name, "w")
    fp.write("%uFFFD" * file_size)
    fp.close()

    for i in range(0, number_of_threads):
        start = part * i
        end = start + part
        if i % 10:
            logger(f"{i} part downloaded!")
        # create a Thread with start and end locations
        t = threading.Thread(
            target=HTTP_Handler,
            kwargs={
                "start": start,
                "end": end,
                "url": url_of_file,
                "filename": file_name,
            },
        )
        t.setDaemon(True)
        t.start()
        main_thread = threading.current_thread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        t.join()
    logger(f"{file_name} download Complete ")


if __name__ == "__main__":
    download_file(obj={})
