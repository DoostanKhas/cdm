import logging

logging.basicConfig(
    level=logging.INFO,
    format=" \u001b[32m[\u001b[0m %(asctime)s \u001b[32m][\u001b[0m%(message)s\u001b[32m]\u001b[0m",
    datefmt="%I:%M:%S",
)


def logger(msg):
    return logging.info(msg)
