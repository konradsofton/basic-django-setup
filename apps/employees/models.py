'''Models for the employee module'''

from django.db import models
from django.conf import settings
from django.utils.timezone import now


class EmployeeModel(models.Model):
    '''Employee model class'''
    objects = models.Manager()
    name = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=now, blank=True)
    updated_at = models.DateTimeField(default=now, blank=True)

    class Meta():
        '''Metadata for the employee model'''
        db_table = 'employee'

    def __str__(self):
        return ' '.join([self.name, self.lname])

