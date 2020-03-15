from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PersonSerializer
from .models import Person


# DRF는 자주 사용하는 view 로직을 그룹화 viewset을 제공
# viewset을 사용하면 CRUD 로직을 구현하지 않고 사용할 수 있다.
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
