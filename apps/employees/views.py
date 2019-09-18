'''Views for the like app'''

import logging
from typing import Any, List

from rest_framework import generics, permissions, status
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_tracking.mixins import LoggingMixin

from .models import EmployeeModel
from .serializers import EmployeeSerializer, CreateEmployeeSerializer


logger = logging.getLogger(__name__)


class EmployeeListView(LoggingMixin, generics.ListAPIView):
    '''Employee List view'''
    logging_methods = ['GET']
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.AllowAny,)


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    '''Employee Detail view'''
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.AllowAny,)


class EmployeeCreateView(generics.CreateAPIView):
    '''Employee Create view'''
    logging_methods = ['POST']
    serializer_class = CreateEmployeeSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        '''Post fn'''
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data['name']
        lastName = serializer.validated_data['lname']
        logger.info(serializer.validated_data)

        try:
            employee = EmployeeModel.objects.create(name=name, lname=lastName)
            return Response(
                status=status.HTTP_201_CREATED,
                data={
                    'id': employee.id,
                    'name': employee.name,
                    'lastName': employee.lname,
                    'createdAt': employee.created_at,
                    'updatedAt': employee.updated_at,
                }
            )

        except Exception as exception:
            logger.error('Exception {}'.format(exception))
            raise ValidationError(detail='Uknown error')
