from rest_framework import serializers

from joplin_web.models import Folders, Notes, Tags, NoteTags, Version


class FoldersSerializer(serializers.ModelSerializer):

    nb_notes = serializers.IntegerField(read_only=True)

    class Meta:
        fields = ('id', 'title', 'parent_id', 'nb_notes', 'created_time')
        model = Folders


class NotesSerializer(serializers.ModelSerializer):

    parent = FoldersSerializer(read_only=True)
    parent_id = serializers.PrimaryKeyRelatedField(queryset=Folders.objects.using('joplin').all(),
                                                   source='folders',
                                                   write_only=True)

    class Meta:
        fields = ('id', 'parent_id', 'parent', 'title', 'body',
            'is_todo', 'todo_due',
            'created_time', 'updated_time',
            'source', 'source_application',
            'latitude', 'longitude', 'altitude',
            'author'
            )
        model = Notes


class TagsSerializer(serializers.ModelSerializer):

    nb_notes = serializers.IntegerField()

    class Meta:
        fields = '__all__'
        model = Tags


class NoteTagsSerializer(serializers.ModelSerializer):

    note = NotesSerializer(read_only=True)
    tag = TagsSerializer(read_only=True)

    note_id = serializers.PrimaryKeyRelatedField(
        queryset=Notes.objects.using('joplin').all(), source='notes', write_only=True)
    tag_id = serializers.PrimaryKeyRelatedField(
        queryset=Tags.objects.using('joplin').all(), source='tags', write_only=True)

    class Meta:
        fields = ('id', 'note_id', 'note', 'tag_id', 'tag', 'created_time',
                  'updated_time', 'user_created_time', 'user_updated_time',
                  'encryption_cipher_text', 'encryption_applied')
        model = NoteTags


class VersionSerializer(serializers.ModelSerializer):

    version = serializers.IntegerField()

    class Meta:
        fields = ('version', )
        read_only_fields = ('version', )
        model = Version
