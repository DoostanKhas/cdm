# -*- coding: utf-8 -*-
"""
cdm is a commend line Download Manger.
this file is version file"""

VERSION = (1, 5, 0)
PRERELEASE = "rc"  # alpha, beta or rc
REVISION = None


def generate_version(version, prerelease=None, revision=None):
    version_parts = [".".join(map(str, version))]
    if prerelease:
        version_parts.append("-{}".format(prerelease))
    if revision:
        version_parts.append(".{}".format(revision))
    return "".join(version_parts)


__title__ = "dcdm"
__description__ = "cdm is a commend line Download Manger"
__url__ = "https://github.com/DoostanKhas/cdm "
__version__ = generate_version(VERSION, prerelease=PRERELEASE, revision=REVISION)
__author__ = "doostanKhas"
__author_email__ = "doostanKhas@gmail.com"
__license__ = "Apache 2.0"
