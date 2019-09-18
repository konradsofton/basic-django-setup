'''Registered models for the likes likes module'''

from material.admin.decorators import register
from material.admin.options import MaterialModelAdmin

from . import models


@register(models.EmployeeModel)
class EmployeeAdminModel(MaterialModelAdmin):
    '''Employee Admin Model'''
    list_display = ('name', 'created_at', 'updated_at')
    ordering = ('name',)
    icon = 'account_box'
