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

    help = 'Rename a folder to Joplin'

    def add_arguments(self, parser):
        parser.add_argument('id', type=str, help="id of the folder name")
        parser.add_argument('name', type=str, help="new name of the folder")

    def handle(self, *args, **options):
        """
            call the command to edit of folder
        """
        logger.info("launch joplin to rename the folder %s to %s" % (options['id'], options['name']))

        joplin = Joplin()
        out, err, exitcode = joplin.ren(options['id'], options['name'])
        return out.decode()
