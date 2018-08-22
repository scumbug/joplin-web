#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals
import json
import shlex
from subprocess import Popen, PIPE

# django
from django.conf import settings
from django.core.management.base import BaseCommand
from logging import getLogger

# create logger
logger = getLogger("joplin_web.jw")


class Command(BaseCommand):

    help = 'Add a note to Joplin'

    def _run(self, line):
        """
        run a joplin command
        :return: message and exitcode
        """
        args = shlex.split(line)
        proc = Popen(args, stdout=PIPE, stderr=PIPE)
        out, err = proc.communicate()
        exitcode = proc.returncode
        logger.info("joplin use %s %s %s" % (out, err, exitcode))
        return out, err, exitcode

    def add_arguments(self, parser):
        parser.add_argument('notebook', type=str, help="the notebook where to add the note")
        parser.add_argument('body', type=str, help="body of the note")
        parser.add_argument('title', type=str, help="title of the note")

    def handle(self, *args, **options):
        """
            call the command to add a note
        """
        logger.info("launch joplin to make a note")
        # run
        # 1) joplin use notebook to point on the notebook where to store the note
        # 2) joplin mknote will returned the note id of the created note
        # 3) joplin set note_id body xxx to add the body to the note

        # use notebook
        line = 'joplin --profile {} use "{}"'.format(settings.JOPLIN_PROFILE_PATH,
                                                     options['notebook'])
        logger.debug(line)
        out, err, exitcode = self._run(line)
        logger.debug("joplin use %s %s %s" % (out, err, exitcode))

        if exitcode == 0:
            # 2) create the note with its title only
            line = 'joplin --profile {} mknote "{}"'.format(settings.JOPLIN_PROFILE_PATH,
                                                          options['title'])
            logger.debug(line)
            out, err, exitcode = self._run(line)
            logger.debug("joplin mknote %s %s %s" % (out, err, exitcode))

            if exitcode == 0:
                # get the last created note (id)
                # see jolin help ls for details about each options
                line = "joplin --profile {} ls -n 1 -s created_time -t n -f json".format(settings.JOPLIN_PROFILE_PATH)
                logger.debug(line)
                out, err, exitcode = self._run(line)

                logger.debug("joplin ls -f json %s %s %s" % (out, err, exitcode))

                if exitcode == 0:
                    # 3) set the body of the note
                    payload = json.loads(out)
                    note_id = payload[0]['id'][:5]
                    logger.debug("note id %s " % note_id)
                    logger.debug("titre %s " % payload[0]['title'])
                    logger.debug("body  %s " % payload[0]['body'])
                    line = 'joplin --profile {} set {} body "{}"'.format(settings.JOPLIN_PROFILE_PATH,
                                                                          note_id,
                                                                          options['body'])
                    logger.info(line)
                    out, err, exitcode = self._run(line)

                logger.debug("joplin set %s %s %s" % (out, err, exitcode))
        return out.decode()