# coding: utf-8
# std lib
import json
from logging import getLogger
import shlex
from subprocess import Popen, PIPE

# django
from django.conf import settings

# create logger
logger = getLogger("joplin_web.command")

"""
    Joplin wrapper for joplin terminal command
    # run
    # 1) joplin use notebook to point on the notebook where to store the note
    # 2) joplin mknote will returned the note id of the created note
    # 3) joplin set note_id body xxx to add the body to the note

    example:
    >>> joplin = Joplin()
    >>> joplin.mkbook('My Book')
    joplin --profile /home/foxmask/.config/joplin-desktop/ mkbook "My Book"
    (b'', b'', 0)
    >>> joplin.mknote('My Book', 'My title', 'My body')
    joplin --profile /home/foxmask/.config/joplin-desktop/ use "My Book"
    joplin --profile /home/foxmask/.config/joplin-desktop/ mknote "My title"
    joplin --profile /home/foxmask/.config/joplin-desktop/  ls -n 1 -s created_time -t n -f json
    set b7f4c  body "My body"
    joplin --profile /home/foxmask/.config/joplin-desktop/ set b7f4c  body "My body"
    (b'', b'', 0)

"""


class Joplin:

    profile_path = ''

    def __init__(self):
        """
        set the profile path of joplin
        """
        self.profile_path = settings.JOPLIN_PROFILE_PATH

    def _run(self, line):
        """
        Build the command to be running
        :param line: the command to run
        :return: message and exitcode
        """
        cmd = "joplin --profile {} {}".format(self.profile_path, line)
        logger.debug(cmd)
        args = shlex.split(cmd)
        proc = Popen(args, stdout=PIPE, stderr=PIPE)
        out, err = proc.communicate()
        exitcode = proc.returncode
        logger.info("joplin %s %s %s" % (out, err, exitcode))
        return out, err, exitcode

    #########
    # Notes #
    #########
    def ls(self, type_object):
        """
        list notes, but extract __the line__ of the new created note
        :param type_object: n = note - t = task
        :return: message and exitcode
        """
        line = " ls -n 1 -s created_time -t {} -f json".format(type_object)
        return self._run(line)

    def setp(self, note_id, **kwargs):
        """
        set properties
        :param note_id: id on the created note
        :param kwargs: can contains body and some other additionals properties
        :return: message and exitcode
        """
        out = err = ''
        exitcode = 0
        line_start = 'set {note_id} '.format(note_id=note_id)
        for key in kwargs:
            line = line_start + ' {key} "{value}"'.format(key=key, value=kwargs.get(key))
            print("SET {}", line)
            logger.debug("SET %s " % line)
            out, err, exitcode = self._run(line)

        return out, err, exitcode

    def mknote(self, notebook, title, body, type_object='n'):
        """
        Create a note
        :param notebook: notebook choosen to store the new note
        :param title: note title to create
        :param body: content of the note to add to the created note
        :param type_object: type of object to create : n = note, t = task
        :return: message and exitcode
        """
        kwargs = dict()
        out, err, exitcode = self._use(notebook)
        if exitcode == 0:
            line = 'mknote "{}"'.format(title)
            out, err, exitcode = self._run(line)
            if exitcode == 0:
                out, err, exitcode = self.ls(type_object)
                if exitcode == 0:
                    # 3) set the body of the note
                    payload = json.loads(out)
                    note_id = payload[0]['id'][:5]
                    logger.debug("note id %s " % note_id)
                    logger.debug("titre %s " % payload[0]['title'])
                    logger.debug("body  %s " % payload[0]['body'])
                    logger.debug("todo  %s " % payload[0]['is_todo'])
                    kwargs['body'] = body
                    out, err, exitcode = self.setp(note_id, **kwargs)
        return out, err, exitcode

    def editnote(self, note_id, parent_id, title, body, is_todo):
        """
        Edit a note
        :param note_id: note id to edit
        :param parent_id: notebook choosen to store the note
        :param title: note title to update
        :param body: content of the note edit the note
        :param is_todo: boolean 1 = todo 0 = note
        :return: message and exitcode
        """
        kwargs = dict()
        kwargs['parent_id'] = parent_id
        kwargs['title'] = title
        kwargs['body'] = body
        kwargs['is_todo'] = is_todo
        return self.setp(note_id, **kwargs)

    def cp(self, note_id, parent_id=0):
        """
        Copy a note to a notebook
        :param note_id: id to copy
        :param parent_id: id of the target notebook, if id is 0 copy to the current folder
        :return: message and exitcode
        """
        line = 'cp "{}" '.format(note_id)
        if parent_id > 0:
            line += ' "{}"'.format(parent_id)
        logger.debug(line)
        return self._run(line)

    def mv(self, note_id, parent_id):
        """
        Move of a note to another folder
        :param note_id: id to move
        :param parent_id: id of the target notebook
        :return: message and exitcode
        """
        line = 'mv "{}" "{}"'.format(note_id, parent_id)
        logger.debug(line)
        return self._run(line)

    def rmnote(self, note):
        """
        Remove a note
        :param note: id to delete
        :return: message and exitcode
        """
        line = 'rmnote "{}"'.format(note)
        logger.debug(line)
        return self._run(line)

    ############
    # Noteooks #
    ############
    def mkbook(self, notebook):
        """
        Create a notebook
        :param notebook: to create
        :return: message and exitcode
        """
        line = 'mkbook "{}"'.format(notebook)
        logger.debug(line)
        return self._run(line)

    def rmbook(self, notebook):
        """
        Remove a notebook
        :param notebook: to delete
        :return: message and exitcode
        """
        line = 'rmbook '.format(notebook)
        logger.debug(line)
        return self._run(line)

    def _use(self, notebook):
        """
        point to the notebook to use
        :return: message and exitcode
        """
        line = 'use "{}"'.format(notebook)
        logger.debug(line)
        return self._run(line)

    #########
    # To-do #
    #########
    def toggle(self, note_id):
        """
        set a note as a (uncomplet) To-do
        then set a To-do as complet
        then set a completed To-do as a (uncompleted) To-do
        :return: message and exitcode
        """
        line = 'todo toggle "{}"'.format(note_id)
        logger.debug(line)
        return self._run(line)

    def clear(self, note_id):
        """
        set a To-do back as note
        :return: message and exitcode
        """
        line = 'todo clear "{}"'.format(note_id)
        logger.debug(line)
        return self._run(line)

    def done(self, note_id):
        """
        Marks a to-do as completed.
        :return: message and exitcode
        """
        line = 'done "{}"'.format(note_id)
        logger.debug(line)
        return self._run(line)

    def undone(self, note_id):
        """
        Marks a to-do as non-completed.
        :return: message and exitcode
        """
        line = 'undone "{}"'.format(note_id)
        logger.debug(line)
        return self._run(line)

    ######################
    # Note and Notebooks #
    ######################
    def ren(self, note_or_folder_id, name):
        """
        Rename a note or a folder
        :param note_or_folder_id: id to rename (note or folder)
        :param name: string to use for renaming
        :return: message and exitcode
        """
        line = 'ren "{}" "{}"'.format(note_or_folder_id, name)
        logger.debug(line)
        return self._run(line)

    #######
    # Tag #
    #######
    def tag(self, action, tag_id, note_id):
        """
        deal with tag for a note
        :param action: can be add/remove/list
        :param tag_id: tag to add or remove to the note
        :param note_id: id of the note where the tag is added or deleted
        :return: message and exitcode
        """
        line = "tag {action} {tag_id} {note_id}".format(action=action, tag_id=tag_id, note_id=note_id)
        return self._run(line)

    ###############
    # Joplin info #
    ###############
    def version(self):
        """
        Version of Joplin
        :return: message and exitcode
        """
        logger.debug('joplin version ?')
        return self._run('version')

    ############
    # Settings #
    ############
    def config(self, name, value):
        """
        apply a config for `name` to `value`
        see doc at https://joplin.cozic.net/terminal/  `config [name] [value]`
        :param name: config name
        :param value: value to apply
        :return: message and exitcode
        """
        line = "config {name} {value}".format(name=name, value=value)
        return self._run(line)

