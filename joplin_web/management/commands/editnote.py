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

    help = 'Edit a note to Joplin'

    def add_arguments(self, parser):
        parser.add_argument('note_id', type=str, help="id of the note")
        parser.add_argument('parent_id', type=str, help="id of the folder name")
        parser.add_argument('body', type=str, help="body of the note")
        parser.add_argument('title', type=str, help="title of the note")
        parser.add_argument('is_todo', type=int, help="Todo boolean")

    def handle(self, *args, **options):
        """
            call the command to edit a note
        """
        logger.info("launch joplin to edit the note %s" % options['note_id'])

        joplin = Joplin()
        out, err, exitcode = joplin.editnote(options['note_id'],
                                             options['parent_id'],
                                             options['title'],
                                             options['body'],
                                             options['is_todo'])
        return out.decode()
