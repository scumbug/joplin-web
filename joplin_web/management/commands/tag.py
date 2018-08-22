#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals
import shlex
from  subprocess import Popen, PIPE

# django
from django.conf import settings
from django.core.management.base import BaseCommand
from logging import getLogger

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
            call the command to add a tag to a note
        """

        logger.info("launch joplin to %s a tag %s to a note %s" %
                    (options['action'], options['tag'], options['note']))
        # run
        line = 'joplin --profile {profile} tag {action} {tag} {note}'.format(
            profile=settings.JOPLIN_PROFILE_PATH,
            action=options['action'],
            tag=options['tag'],
            note=options['note'])

        logger.info("%s" % line)

        args = shlex.split(line)
        # result = subprocess.run(args, shell=True)

        proc = Popen(args, stdout=PIPE, stderr=PIPE)
        out, err = proc.communicate()
        exitcode = proc.returncode

        logger.info("%s %s %s" % (out, err, exitcode))
        return out.decode()
