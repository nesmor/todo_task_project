# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib import admin


class User(models.Model):
    name = models.CharField(max_length=150, blank=True, null=False)
    password = models.CharField(max_length=32, blank=True, null=False)
    email = models.CharField(max_length=100)
    phone = models.DecimalField(max_digits=9999999, decimal_places=0, blank=True, null=True)
    creation_date = models.DateTimeField(blank=True, null=True, auto_now=True)
    status = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'user'

    def __str__(self):
        return  "%s: %s" % (self.id, self.name)

class TodoListTask(models.Model):
    task = models.CharField(max_length=250, blank=True, null=False)
    status =  models.BooleanField(verbose_name='Ended')
    updated_date = models.DateTimeField(blank=True, null=True, auto_now=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'todo_list_task'
