# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alarms(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)  # AutoField?
    note_id = models.TextField()
    trigger_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'alarms'


class DeletedItems(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)  # AutoField?
    item_type = models.IntegerField()
    item_id = models.TextField()
    deleted_time = models.IntegerField()
    sync_target = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'deleted_items'


class Folders(models.Model):
    id = models.TextField(primary_key=True, blank=True)
    title = models.TextField()
    created_time = models.IntegerField(blank=True)
    updated_time = models.IntegerField(blank=True)
    user_created_time = models.IntegerField(blank=True)
    user_updated_time = models.IntegerField(blank=True)
    encryption_cipher_text = models.TextField(blank=True)
    encryption_applied = models.IntegerField(blank=True)
    parent_id = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'folders'


class ItemChanges(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)  # AutoField?
    item_type = models.IntegerField()
    item_id = models.TextField()
    type = models.IntegerField()
    created_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'item_changes'


class MasterKeys(models.Model):
    id = models.TextField(primary_key=True, blank=True)
    created_time = models.IntegerField()
    updated_time = models.IntegerField()
    source_application = models.TextField()
    encryption_method = models.IntegerField()
    checksum = models.TextField()
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'master_keys'


class NoteResources(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)  # AutoField?
    note_id = models.TextField()
    resource_id = models.TextField()
    is_associated = models.IntegerField()
    last_seen_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'note_resources'


class NoteTags(models.Model):
    id = models.TextField(primary_key=True, blank=True)
    # note_id = models.TextField()
    # tag_id = models.TextField()
    note = models.ForeignKey("Notes", on_delete=models.CASCADE,)
    tag = models.ForeignKey("Tags", on_delete=models.CASCADE,)
    created_time = models.IntegerField()
    updated_time = models.IntegerField()
    user_created_time = models.IntegerField()
    user_updated_time = models.IntegerField()
    encryption_cipher_text = models.TextField()
    encryption_applied = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'note_tags'


class Notes(models.Model):
    id = models.TextField(primary_key=True, blank=True)
    parent = models.ForeignKey("Folders", on_delete=models.CASCADE,)
    # parent_id = models.TextField()
    title = models.TextField()
    body = models.TextField()
    created_time = models.IntegerField(blank=True)
    updated_time = models.IntegerField(blank=True)
    is_conflict = models.IntegerField(blank=True)
    latitude = models.TextField(blank=True)  # This field type is a guess.
    longitude = models.TextField(blank=True)  # This field type is a guess.
    altitude = models.TextField(blank=True)  # This field type is a guess.
    author = models.TextField(blank=True)
    source_url = models.TextField(blank=True)
    is_todo = models.IntegerField(blank=True)
    todo_due = models.IntegerField(blank=True)
    todo_completed = models.IntegerField(blank=True)
    source = models.TextField(blank=True)
    source_application = models.TextField(blank=True)
    application_data = models.TextField(blank=True)
    order = models.IntegerField(blank=True)
    user_created_time = models.IntegerField(blank=True)
    user_updated_time = models.IntegerField(blank=True)
    encryption_cipher_text = models.TextField(blank=True)
    encryption_applied = models.IntegerField(blank=True)

    class Meta:
        managed = False
        db_table = 'notes'


class Resources(models.Model):
    id = models.TextField(primary_key=True, blank=True)
    title = models.TextField()
    mime = models.TextField()
    filename = models.TextField()
    created_time = models.IntegerField()
    updated_time = models.IntegerField()
    user_created_time = models.IntegerField()
    user_updated_time = models.IntegerField()
    file_extension = models.TextField()
    encryption_cipher_text = models.TextField()
    encryption_applied = models.IntegerField()
    encryption_blob_encrypted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'resources'


class Settings(models.Model):
    key = models.TextField(primary_key=True, blank=True)
    value = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'settings'


class SyncItems(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)  # AutoField?
    sync_target = models.IntegerField()
    sync_time = models.IntegerField()
    item_type = models.IntegerField()
    item_id = models.TextField()
    sync_disabled = models.IntegerField()
    sync_disabled_reason = models.TextField()
    force_sync = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sync_items'


class TableFields(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)  # AutoField?
    table_name = models.TextField()
    field_name = models.TextField()
    field_type = models.IntegerField()
    field_default = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'table_fields'


class Tags(models.Model):
    id = models.TextField(primary_key=True, blank=True)
    title = models.TextField()
    created_time = models.IntegerField(blank=True)
    updated_time = models.IntegerField(blank=True)
    user_created_time = models.IntegerField(blank=True)
    user_updated_time = models.IntegerField(blank=True)
    encryption_cipher_text = models.TextField(blank=True)
    encryption_applied = models.IntegerField(blank=True)

    class Meta:
        managed = False
        db_table = 'tags'


class Version(models.Model):
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'version'
