"""
dcdm is a commend line Download Manger.
this file is main file"""

from __future__ import print_function, unicode_literals

import logging
import sys
import threading
from time import gmtime, strftime

import click
import requests

from cdm.downloaders import HTTP_Handler
from cdm.logger import log_download


@click.command(help="This command is used to download from a link.")
@click.argument("url", type=click.Path(), required=True)
@click.option("--number_of_threads", default=4, help="No of Threads")
@click.option("--name", type=click.Path(), help="Name of the file with extension")
@click.pass_context
def download_file(ctx, url, name, number_of_threads):
    r = requests.head(url)
    file_name = name if name else url.split("/")[-1]

    try:
        file_size = int(r.headers["content-length"])
    except:
        print("Invalid URL")
        sys.exit(1)
    print(
        f" {strftime('%m/%d %H:%M')} [\u001b[1mNOTICE\u001b[0m] start download \u001b[35m[\u001b[0m{file_name}\u001b[35m]\u001b[0m.file size, \u001b[35m[\u001b[0m{file_size//1024}\u001b[35m]\u001b[0m Kb"
    )
    part = int(file_size) // number_of_threads
    fp = open(file_name, "w")
    fp.write("%uFFFD" * file_size)
    fp.close()

    for i in range(0, number_of_threads):
        start = part * i
        end = start + part
        if i % 10:
            log_download(f"{i} part downloaded!")
        # create a Thread with start and end locations
        t = threading.Thread(
            target=HTTP_Handler,
            kwargs={
                "start": start,
                "end": end,
                "url": url,
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
    print("(\u001b[32;1m OK \u001b[0m):download completed.")
