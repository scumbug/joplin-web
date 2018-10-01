#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals

# django
from django.core.management.base import BaseCommand
from logging import getLogger

# joplin_api
from joplin_api import JoplinCmdApi

# create logger
logger = getLogger("joplin_web.jw")


class Command(BaseCommand):

    help = 'Add/list/remove a tag to/from a note in to Joplin'

    def add_arguments(self, parser):
        parser.add_argument('action', type=str, help="add, remove or list")
        parser.add_argument('tag', type=str, help="tag name")
        parser.add_argument('note', type=str, help="note id")

    def handle(self, *args, **options):
        """
            call the command to apply an action on a tag
        """
        logger.info("launch joplin to %s a tag %s to a note %s" %
                    (options['action'], options['tag'], options['note']))

        joplin = JoplinCmdApi()
        out, err, exitcode = joplin.mknote(options['action'], options['tag'], options['note'])
        return out.decode()
