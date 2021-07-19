import logging


def log_download(msg):
    logging.basicConfig(
        level=logging.INFO,
        format="\u001b[35m[\u001b[0m %(asctime)s [\u001b[1mNOTICE\u001b[0m] %(message)s \u001b[35m]\u001b[0m",
        datefmt="%m/%d %H:%M",
    )
    return logging.info(msg)
