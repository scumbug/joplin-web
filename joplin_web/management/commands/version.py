#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals

# django
from django.core.management.base import BaseCommand
from logging import getLogger

# joplin_web
from joplin_web.joplin import Joplin

# create logger
logger = getLogger("joplin_web.jw")


class Command(BaseCommand):

    help = 'Display the Joplin version'

    def handle(self, *args, **options):
        """
            call the command to get the joplin version
        """
        logger.info("launch joplin to get the version")

        joplin = Joplin()
        out, err, exitcode = joplin.version()
        return out.decode()
