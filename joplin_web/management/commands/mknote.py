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

    help = 'Add a note to Joplin'

    def add_arguments(self, parser):
        parser.add_argument('notebook', type=str, help="the notebook where to add the note")
        parser.add_argument('body', type=str, help="body of the note")
        parser.add_argument('title', type=str, help="title of the note")

    def handle(self, *args, **options):
        """
            call the command to add a note
        """
        logger.info("launch joplin to make a note in %s" % options['notebook'])

        joplin = Joplin()
        out, err, exitcode = joplin.mknote(options['notebook'], options['title'], options['body'])
        return out.decode()
