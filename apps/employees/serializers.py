'''Serializers for the comments app'''

from rest_framework import serializers
from .models import EmployeeModel


class EmployeeSerializer(serializers.ModelSerializer):
    '''Employee Serializer'''

    class Meta:
        '''Metadata for the EmployeeSerializer'''
        model = EmployeeModel
        fields = (
            'id',
            'name',
            'lname',
            'created_at',
            'updated_at',
        )


class CreateEmployeeSerializer(serializers.Serializer):
    '''CreateEmployee Serializer'''
    name = serializers.CharField(required=True)
    lname = serializers.CharField(required=True)
